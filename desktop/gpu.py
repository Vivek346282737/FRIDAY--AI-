"""
FRIDAY AI
GPU Monitor Module

Responsibilities
----------------
- GPU Name
- GPU Usage
- VRAM
- Temperature

Uses GPUtil.
No FastAPI logic.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

import GPUtil

logger = logging.getLogger(__name__)


class GPUMonitor:
    """Collect GPU information."""

    def get_info(self) -> dict[str, Any]:

        try:

            gpus = GPUtil.getGPUs()

            if not gpus:

                return {
                    "status": "unavailable",
                    "source": "GPUtil",
                    "timestamp": datetime.now().isoformat(),
                    "message": "No supported GPU detected.",
                    "gpus": [],
                }

            gpu_list = []

            for gpu in gpus:

                gpu_list.append({

                    "id": gpu.id,

                    "name": gpu.name,

                    "uuid": gpu.uuid,

                    "load_percent": round(gpu.load * 100, 2),

                    "temperature": gpu.temperature,

                    "memory": {

                        "total_mb": gpu.memoryTotal,

                        "used_mb": gpu.memoryUsed,

                        "free_mb": gpu.memoryFree,

                    }

                })

            return {

                "status": "ok",

                "source": "GPUtil",

                "timestamp": datetime.now().isoformat(),

                "gpu_count": len(gpu_list),

                "gpus": gpu_list,

            }

        except Exception as exc:

            logger.exception("GPU Monitor Error")

            return {

                "status": "error",

                "source": "GPUtil",

                "timestamp": datetime.now().isoformat(),

                "message": str(exc),

                "gpus": [],

            }


gpu_monitor = GPUMonitor()


if __name__ == "__main__":

    from pprint import pprint

    pprint(gpu_monitor.get_info())