from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from server import mcp

from services.system_service import get_system_info
from services.process_service import open_app, close_app

from friday_core import process_message

from ai.memory import extract_memory
from ai.conversation import conversation

from memory.manager import memory_manager

app = FastAPI(title="FRIDAY API")

# Mount MCP SSE server
app.mount("/sse", mcp.sse_app())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===========================================
# REQUEST MODELS
# ===========================================

class AppRequest(BaseModel):
    app: str


class ChatRequest(BaseModel):
    message: str


class MemoryRequest(BaseModel):
    category: str
    key: str
    value: str


class ForgetRequest(BaseModel):
    key: str


# ===========================================
# HOME
# ===========================================

@app.get("/")
def home():

    return {
        "message": "FRIDAY API Running ðŸš€"
    }


# ===========================================
# SYSTEM
# ===========================================

@app.get("/system")
def system():

    return get_system_info()


# ===========================================
# APP CONTROL
# ===========================================

@app.post("/open-app")
def launch_app(data: AppRequest):

    return open_app(data.app)


@app.post("/close-app")
def kill_app(data: AppRequest):

    return close_app(data.app)


# ===========================================
# AI CHAT
# ===========================================

@app.post("/chat")
def chat(data: ChatRequest):

    # Save memories automatically
    extract_memory(data.message)

    # Save user message
    conversation.add_user(data.message)

    # Load memories
    memories = memory_manager.recall()

    memory_text = ""

    for item in memories:

        memory_text += (
            f"{item['category']} : "
            f"{item['key']} = "
            f"{item['value']}\n"
        )

    # Run Agent Loop
    result = process_message(
        data.message,
        memory_text,
        conversation.get_history()
    )

    # Save final AI reply
    if result.get("message"):
        conversation.add_ai(result["message"])

    return result


# ===========================================
# MEMORY
# ===========================================

@app.post("/memory/remember")
def remember(data: MemoryRequest):

    return memory_manager.remember(
        data.category,
        data.key,
        data.value
    )


@app.get("/memory")
def recall(category: str = None):

    return memory_manager.recall(category)


@app.delete("/memory")
def forget(data: ForgetRequest):

    return memory_manager.forget(data.key)

