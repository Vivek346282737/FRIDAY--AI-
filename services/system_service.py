import psutil
import platform
import cpuinfo
import socket
import datetime
import GPUtil


def get_system_info():

    # =========================
    # MEMORY
    # =========================

    memory = psutil.virtual_memory()

    # =========================
    # DISK
    # =========================

    disk = psutil.disk_usage("/")

    # =========================
    # BATTERY
    # =========================

    battery = psutil.sensors_battery()

    if battery:
        battery_percent = battery.percent
        charging = battery.power_plugged
    else:
        battery_percent = None
        charging = None

    # =========================
    # CPU
    # =========================

    cpu = cpuinfo.get_cpu_info()

    # =========================
    # GPU
    # =========================

    gpus = GPUtil.getGPUs()

    if gpus:
        gpu = gpus[0]

        gpu_name = gpu.name
        gpu_usage = round(gpu.load * 100, 1)
        gpu_memory_total = gpu.memoryTotal
        gpu_memory_used = gpu.memoryUsed
        gpu_temperature = gpu.temperature

    else:
        gpu_name = "No GPU Detected"
        gpu_usage = 0
        gpu_memory_total = 0
        gpu_memory_used = 0
        gpu_temperature = None

    # =========================
    # BOOT TIME
    # =========================

    boot_time = datetime.datetime.fromtimestamp(
        psutil.boot_time()
    ).strftime("%d-%m-%Y %H:%M:%S")

    uptime_hours = round(
        (datetime.datetime.now().timestamp() - psutil.boot_time()) / 3600,
        2
    )

    # =========================
    # RETURN JSON
    # =========================

    return {

        # -------------------------
        # SYSTEM
        # -------------------------

        "system": platform.system(),
        "machine": platform.machine(),
        "hostname": socket.gethostname(),
        "windows_version": platform.version(),

        # -------------------------
        # CPU
        # -------------------------

        "cpu_name": cpu.get("brand_raw", "Unknown CPU"),
        "cpu_cores": psutil.cpu_count(logical=False),
        "cpu_threads": psutil.cpu_count(logical=True),
        "cpu_percent": psutil.cpu_percent(interval=1),

        # -------------------------
        # GPU
        # -------------------------

        "gpu_name": gpu_name,
        "gpu_usage": gpu_usage,
        "gpu_memory_total": gpu_memory_total,
        "gpu_memory_used": gpu_memory_used,
        "gpu_temperature": gpu_temperature,

        # -------------------------
        # RAM
        # -------------------------

        "ram_percent": memory.percent,
        "ram_used_gb": round(memory.used / (1024 ** 3), 2),
        "ram_total_gb": round(memory.total / (1024 ** 3), 2),
        "ram_available_gb": round(memory.available / (1024 ** 3), 2),

        # -------------------------
        # DISK
        # -------------------------

        "disk_percent": disk.percent,
        "disk_used_gb": round(disk.used / (1024 ** 3), 2),
        "disk_total_gb": round(disk.total / (1024 ** 3), 2),
        "disk_free_gb": round(disk.free / (1024 ** 3), 2),

        # -------------------------
        # BATTERY
        # -------------------------

        "battery_percent": battery_percent,
        "charging": charging,

        # -------------------------
        # UPTIME
        # -------------------------

        "boot_time": boot_time,
        "uptime_hours": uptime_hours,

        # -------------------------
        # NETWORK
        # -------------------------

        "network": "Connected",

        # -------------------------
        # STATUS
        # -------------------------

        "status": "Healthy"
    }