"""
FRIDAY AI
Processes Monitor Module

Responsibilities
----------------
- Running Processes
- CPU Usage
- Memory Usage

No FastAPI logic.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

import psutil

logger = logging.getLogger(__name__)


class ProcessMonitor:
    """Collect running process information."""

    def get_info(self) -> dict[str, Any]:

        try:

            processes = []

            for proc in psutil.process_iter(
                [
                    "pid",
                    "name",
                    "cpu_percent",
                    "memory_percent",
                ]
            ):

                try:

                    info = proc.info

                    processes.append(

                        {
                            "pid": info["pid"],
                            "name": info["name"],
                            "cpu_percent": round(
                                info["cpu_percent"],
                                2,
                            ),
                            "memory_percent": round(
                                info["memory_percent"],
                                2,
                            ),
                        }

                    )

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                ):
                    continue

            processes.sort(
                key=lambda x: x["memory_percent"],
                reverse=True,
            )

            return {

                "status": "ok",

                "timestamp": datetime.now().isoformat(),

                "process_count": len(processes),

                "top_processes": processes[:15],

            }

        except Exception as exc:

            logger.exception("Process Monitor Error")

            return {

                "status": "error",

                "timestamp": datetime.now().isoformat(),

                "message": str(exc),

            }


process_monitor = ProcessMonitor()


if __name__ == "__main__":

    from pprint import pprint

    pprint(process_monitor.get_info())