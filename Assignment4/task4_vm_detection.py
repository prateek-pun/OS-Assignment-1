import subprocess
import os

def print_system_details():
    print("==== System Details ====")

    kernel = subprocess.check_output("uname -r", shell=True, text=True).strip()
    print(f"Kernel Version: {kernel}")

    user = subprocess.check_output("whoami", shell=True, text=True).strip()
    print(f"User: {user}")

    try:
        virt_info = subprocess.check_output("lscpu | grep -i 'virtual'", shell=True, text=True).strip()
        print("Hardware Virtualization Info:")
        print(virt_info if virt_info else "No virtualization flag shown.")
    except:
        print("Unable to read hardware virtualization info.")

def detect_vm():
    print("\n==== VM Detection ====")
    indicators = []
    try:
        manufacturer = subprocess.check_output("sudo dmidecode -s system-manufacturer", shell=True, text=True).lower().strip()
        if any(vm in manufacturer for vm in ["vmware", "virtualbox", "kvm", "qemu", "xen"]):
            indicators.append(f"Manufacturer indicates virtualization: {manufacturer}")
    except:
        indicators.append("DMI info not accessible (run with sudo).")
    try:
        cpu_info = subprocess.check_output("lscpu", shell=True, text=True).lower()
        if "hypervisor" in cpu_info:
            indicators.append("CPU flags show 'hypervisor' → running in VM.")
    except:
        indicators.append("Unable to read CPU info.")

    if indicators:
        print("Virtual Machine Detected")
        for item in indicators:
            print(" -", item)
    else:
        print("✔ No Virtual Machine Detected")

if __name__ == "__main__":
    print_system_details()
    detect_vm()
