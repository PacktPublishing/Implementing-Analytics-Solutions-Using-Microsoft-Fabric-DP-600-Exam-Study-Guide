import subprocess

try:
    # Command to install the Fabric SDK for Python
    print("Installing Fabric SDK for Python...")
    subprocess.check_call(["python", "-m", "pip", "install", "fabric"])
    print("Fabric SDK installed successfully!")
except subprocess.CalledProcessError as e:
    print("An error occurred during installation:", e)
