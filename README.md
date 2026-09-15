\# 🤖 FRIDAY AI



Python-based desktop and browser automation assistant integrating Model Context Protocol (MCP), LLM-driven planning, and local OS execution.



\[!\[Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python\&logoColor=white)](https://www.python.org/)

\[!\[FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)

\[!\[MCP](https://img.shields.io/badge/Protocol-MCP-orange)](https://modelcontextprotocol.io/)

\[!\[PyTorch](https://img.shields.io/badge/PyTorch-Inference-EE4C2C?logo=pytorch\&logoColor=white)](https://pytorch.org/)

\[!\[SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite\&logoColor=white)](https://www.sqlite.org/)



\---



\## Overview



\*\*FRIDAY AI\*\* is an extensible personal assistant and execution engine designed to automate desktop and web tasks via natural language. Instead of relying solely on conversational replies, FRIDAY breaks user requests into structured action plans and executes them through dedicated browser controllers, OS interaction routines, and MCP-compliant tools.



The core pipeline combines an LLM reasoning engine (Gemini/OpenAI compatible) with local agents responsible for browser workflows (Chrome orchestration, navigation, search), system operations (app launch, window focus, hardware metrics), and assistive coding tasks. State and execution history are tracked locally using SQLite.



\---



\## Key Capabilities



\- \*\*Task Planning \& Workflow Execution\*\* — Decomposes multi-step prompts into sequential operations (e.g., open app, delay, navigate, scroll).

\- \*\*Browser Automation Subsystem\*\* — Controls Chrome sessions, searches engines, navigates URLs, and handles viewport scrolling.

\- \*\*Desktop \& System Services\*\* — Launches native applications, tracks window focus, and monitors system resources (CPU, memory, processes).

\- \*\*Model Context Protocol (MCP) Server\*\* — Implements standard MCP interfaces (ListToolsRequest, CallToolRequest) over SSE transports for standardized tool execution.

\- \*\*FastAPI HTTP \& SSE Backend\*\* — Exposes REST endpoints (/chat, /system, /docs) and streaming event endpoints for external clients.

\- \*\*Local State Tracking\*\* — Persists agent activity and sessions via a local SQLite database (friday.db).

\- \*\*Safety Fail-Safes\*\* — Incorporates mouse position safeguards (PyAutoGUI fail-safe) and exception isolation across individual actions.



\---



\## Architecture



```mermaid

flowchart TD

&#x20;   User\["User / Client"] --> API\["FastAPI Server / CLI Interface"]

&#x20;   API --> Core\["FRIDAY Agent Core"]



&#x20;   subgraph Reasoning\["Reasoning and Planning"]

&#x20;       Core --> Planner\["Workflow Planner and Intent Parser"]

&#x20;       Planner --> LLM\["LLM Reasoning Layer (Gemini / OpenAI API)"]

&#x20;   end



&#x20;   subgraph Tooling\["Tooling and Protocol"]

&#x20;       Core --> MCPServer\["MCP Server (server.py)"]

&#x20;       MCPServer --> ToolRegistry\["Tool Dispatcher and SSE Handlers"]

&#x20;   end



&#x20;   subgraph Execution\["Execution Layer"]

&#x20;       Core --> Executor\["Action Executor (ai/executor.py)"]

&#x20;       Executor --> Browser\["Browser Agent (Chrome and Navigation)"]

&#x20;       Executor --> Desktop\["Desktop Agent (Window and App Controller)"]

&#x20;       Executor --> System\["System Services (Process and Resource Monitor)"]

&#x20;   end



&#x20;   subgraph Persistence\["Persistence"]

&#x20;       Core --> DB\[("SQLite (database/friday.db)")]

&#x20;   end

