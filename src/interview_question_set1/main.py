import glob
import subprocess

# Pattern to match files starting with 1., 2., or 3. and ending with .py
files = sorted(glob.glob("[123].*.py"))

# Execute each matching file only once, in alphabetical order
executed_files = set()  # Track executed files to avoid duplicates
for file in files:
    if file not in executed_files:
        print(f"Executing {file}...")
        subprocess.run(["python", file])
        executed_files.add(file)  # Mark file as executed
