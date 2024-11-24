import subprocess

try:
    # Command to install the Azure SDK for Python
    print("Installing Azure SDK for Python...")
    subprocess.check_call(["python", "-m", "pip", "install", "azure"])
    print("Azure SDK installed successfully!")
except subprocess.CalledProcessError as e:
    print("An error occurred during the installation of Azure SDK:", e)
