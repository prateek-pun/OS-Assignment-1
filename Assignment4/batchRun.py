import os
import subprocess
folder = "batch_project"
os.makedirs(folder, exist_ok=True)

script1 = """print("Script 1 is running...")
for i in range(3):
    print(f"Script 1 count: {i}")"""

script2 = """print("Script 2 is processing data...")
data = [10, 20, 30]
print("Sum of data =", sum(data))"""

script3 = """print("Script 3 is generating output...")
name = "Nishtha"
print(f"Hello {name}, batch processing completed!")"""

files = {
    "script1.py": script1,
    "script2.py": script2,
    "script3.py": script3,
}

for filename, content in files.items():
    with open(os.path.join(folder, filename), "w") as f:
        f.write(content)

print("All scripts created successfully.\n")

scripts = ["script1.py", "script2.py", "script3.py"]

for script in scripts:
    print(f"\nExecuting {script}...")
    subprocess.run(["python3", os.path.join(folder, script)])




