import subprocess

def run_python_script(script_path):
    try:
        subprocess.run(['python3', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")

