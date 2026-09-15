\# 🤖 FRIDAY AI — Autonomous Multimodal Agent \& MCP Engine

\### \*Desktop Vision Perception, Multi-Step Orchestration, and System-Level Automation\*



\[!\[Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB.svg?logo=python\&logoColor=white)](https://www.python.org/)

\[!\[FastAPI Engine](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com)

\[!\[Protocol Specification](https://img.shields.io/badge/Architecture-Model%20Context%20Protocol%20(MCP)-orange.svg)](https://modelcontextprotocol.io/)

\[!\[Deep Learning Runtime](https://img.shields.io/badge/Inference-PyTorch%20%2F%20Quantized%20Tensors-EE4C2C.svg?logo=pytorch\&logoColor=white)](https://pytorch.org/)

\[!\[Concurrency](https://img.shields.io/badge/Concurrency-AsyncIO%20%2F%20Non--Blocking-darkgreen.svg)]()

\[!\[Build \& Packaging](https://img.shields.io/badge/Packaging-uv%20%2F%20pyproject.toml-blueviolet.svg)](https://github.com/astral-sh/uv)

\[!\[License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)



\*\*FRIDAY AI\*\* is an asynchronous, modular AI agent framework engineered in Python using \*\*FastAPI\*\* and the \*\*Model Context Protocol (MCP)\*\*. It bridges modern reasoning engines (LLMs / Multimodal Vision models) with deterministic local environments, enabling persistent memory state-machines, automated browser workflows, dynamic tool resolution, and automated OS-level desktop execution through structured perception-action feedback loops.



\---



\## 📑 Table of Contents

\- \[Architectural Overview](#-architectural-overview)

\- \[System Dataflow \& Component Architecture](#-system-dataflow--component-architecture)

\- \[Core Engineering Features](#-core-engineering-features)

\- \[Languages, Frameworks \& Tooling Stack](#-languages-frameworks--tooling-stack)

\- \[Directory \& Repository Structure](#-directory--repository-structure)

\- \[Verified Execution Traces (Live Logs)](#-verified-execution-traces-live-logs)

\- \[Installation \& Environment Setup](#-installation--environment-setup)

\- \[API Reference \& Endpoints](#-api-reference--endpoints)

\- \[Operational Guardrails \& Safety Mechanisms](#-operational-guardrails--safety-mechanisms)

\- \[License \& Contributions](#-license--contributions)



\---



\## 🏛️ Architectural Overview



Most standard LLM implementations operate as reactive wrappers lacking state awareness, runtime safety rails, and tool modularity. \*\*FRIDAY AI\*\* addresses these bottlenecks through a modular subsystem architecture:



1\. \*\*Decoupled Architecture:\*\* Strict separation between Agent Controller logic (`agent\_friday.py`), API Distribution Layer (`api\_server.py`), and Extensible MCP Tool Handlers (`server.py`).

2\. \*\*Model Context Protocol (MCP) Standard:\*\* Exposes and discovers operational tools dynamically without modifying core prompt templates.

3\. \*\*Execution Subsystem (`ai.executor`):\*\* Dispatches deterministic system actions (Browser controls, process hooks, shell invocations) with structured JSON receipts.

4\. \*\*Low-Latency Vision Percepts:\*\* Coordinates desktop screen analysis, coordinate mapping, and non-blocking peripheral inputs.



\---



\## 🔄 System Dataflow \& Component Architecture



```text

+---------------------------------------------------------------------------------+

|                          CLIENT \& PERIPHERAL CHANNELS                           |

|       (Interactive CLI / Terminal  •  FastAPI REST Endpoints  •  System Triggers) |

+----------------------------------------┬----------------------------------------+

&#x20;                                        │

&#x20;                                        ▼

+---------------------------------------------------------------------------------+

|                       WEB ROUTING \& API LAYER (api\_server.py)                   |

|   • FastAPI Async ASGI Core            • Pydantic V2 Strict Validation Schema   |

|   • Request Lifecycle Middleware       • Non-blocking Coroutine Worker Pools    |

+----------------------------------------┬----------------------------------------+

&#x20;                                        │

&#x20;                                        ▼

+---------------------------------------------------------------------------------+

|                       AGENT ORCHESTRATOR (agent\_friday.py)                      |

|   • Plan-and-Solve Reasoning Loop      • Task Graph \& Dependency Resolution     |

|   • Conversational Context Sliding     • Multimodal Screen State Ingestion      |

+-------------------┬-----------------------------------------┬--------------------+

&#x20;                   │                                         │

&#x20;                   ▼                                         ▼

+---------------------------------------+ +---------------------------------------+

|        REASONING PROVIDER (LLM)       | |        MCP RUNTIME (server.py)        |

|  • Google GenAI (Gemini) SDK          | |  • Dynamic Tool Schema Discovery     |

|  • Groq Fast Inference Backing        | |  • Deterministic Execution Sandbox    |

|  • Structured JSON Tool Signatures    | |  • Context Isolation \& State Handling |

+---------------------------------------+ +-------------------┬-------------------+

&#x20;                                                             │

&#x20;                                                             ▼

&#x20;                                         +---------------------------------------+

&#x20;                                         |      EXECUTION ENGINE (ai.executor)   |

&#x20;                                         |  • Browser Automation (Chrome/Focus)  |

&#x20;                                         |  • PyAutoGUI Peripheral Manipulation  |

&#x20;                                         |  • PyTorch Quantized Tensors Subsystem|

&#x20;                                         |  • Subprocess Shell Invocations       |

&#x20;                                         +---------------------------------------+

