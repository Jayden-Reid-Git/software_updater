import subprocess
import platform

def update_software():
    system = platform.system() # Get the OS type (Windows, Linux, or Mac)
    
    try:
        if system == "Windows":
            print("Checking for updates on Windows...")
            subprocess.run(["winget", "upgrade", "--all"], check=True)
        elif system == "Linux":
            print("Checking for updates on Linux...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "upgrade","-y"], check=True)
        else:
            print("Unsupported OS for this script.")
    except Exception as e:
            print(f"Error updating software: {e}")
if __name__ == "__main__":
    update_software()