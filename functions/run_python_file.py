import os
import subprocess
from config import *

def run_python_file(working_directory, file_path, args=[]):
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    dir_path = os.path.abspath(working_directory)

    if not abs_path.startswith(dir_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    completed_process = subprocess.run(["uv run " + abs_path], timeout=30, stdout=True, stderr=True, shell=True)

    return_string = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\n"

    return return_string

