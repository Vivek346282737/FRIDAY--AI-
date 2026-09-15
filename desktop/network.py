"""
FRIDAY AI
Network Monitor Module

Responsibilities
----------------
- Upload Speed
- Download Speed
- Bytes Sent
- Bytes Received
- Network Status

No FastAPI logic.
"""

from __future__ import annotations

import logging
import time
from datetime import datetime
from typing import Any

import psutil

logger = logging.getLogger(__name__)


class NetworkMonitor:
    """Collect network statistics."""

    def get_info(self) -> dict[str, Any]:

        try:

            start = psutil.net_io_counters()

            time.sleep(1)

            end = psutil.net_io_counters()

            upload = (end.bytes_sent - start.bytes_sent) / 1024
            download = (end.bytes_recv - start.bytes_recv) / 1024

            return {

                "status": "ok",

                "source": "psutil",

                "timestamp": datetime.now().isoformat(),

                "upload_kbps": round(upload, 2),

                "download_kbps": round(download, 2),

                "bytes_sent": end.bytes_sent,

                "bytes_received": end.bytes_recv,

            }

        except Exception as exc:

            logger.exception("Network Monitor Error")

            return {

                "status": "error",

                "source": "psutil",

                "timestamp": datetime.now().isoformat(),

                "message": str(exc),

            }


network_monitor = NetworkMonitor()


if __name__ == "__main__":

    from pprint import pprint

    pprint(network_monitor.get_info())