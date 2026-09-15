"""
FRIDAY AI
Memory Monitor Module

Responsibilities
----------------
- RAM usage
- Virtual memory
- Swap memory

This module contains NO FastAPI logic.
It is only responsible for collecting memory information.
"""

from __future__ import annotations

import logging
from typing import Any

import psutil

logger = logging.getLogger(__name__)


class MemoryMonitor:
    """Collect Memory/RAM information."""

    def get_info(self) -> dict[str, Any]:
        """
        Return memory information.
        Never raises exceptions to the caller.
        """

        try:

            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()

            return {

                "ram": {

                    "total_gb": round(memory.total / (1024 ** 3), 2),

                    "used_gb": round(memory.used / (1024 ** 3), 2),

                    "available_gb": round(
                        memory.available / (1024 ** 3), 2
                    ),

                    "free_gb": round(memory.free / (1024 ** 3), 2),

                    "percent": memory.percent,

                },

                "swap": {

                    "total_gb": round(swap.total / (1024 ** 3), 2),

                    "used_gb": round(swap.used / (1024 ** 3), 2),

                    "free_gb": round(swap.free / (1024 ** 3), 2),

                    "percent": swap.percent,

                }

            }

        except Exception as exc:

            logger.exception("Memory Monitor Error")

            return {

                "status": "error",

                "message": str(exc)

            }


memory_monitor = MemoryMonitor()


if __name__ == "__main__":

    from pprint import pprint

    pprint(memory_monitor.get_info())