import os
from config import *

def write_file(working_directory, file_path, content):
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    dir_path = os.path.abspath(working_directory)

    if not abs_path.startswith(dir_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(abs_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error writing file:{e}"
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
   