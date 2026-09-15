"""
FRIDAY AI
System Service

Wrapper around the Desktop Observer Engine.
"""

from desktop.system_monitor import system_monitor


def get_system_info():
    """
    Returns complete live system information collected
    by the Desktop Observer Engine.
    """
    return system_monitor.get_info()