import os
import subprocess

print("Starting DevOps automation script...")

print("Python version:")
subprocess.run(["python", "--version"])

print("Listing project files:")
for root, dirs, files in os.walk("."):
    for name in files:
        print(os.path.join(root, name))

print("Automation completed successfully.")
