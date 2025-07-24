import os
from config import *

def get_file_content(working_directory, file_path):
        abs_path = os.path.abspath(os.path.join(working_directory, file_path))
        dir_path = os.path.abspath(working_directory)

        if not abs_path.startswith(dir_path):
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_path):
                return f'Error: File not found or is not a regular file: "{file_path}"'
        
        try:
            with open(abs_path, "r") as f:
                file_content_string = f.read(CHARACTER_LIMIT)
        except Exception as e:
              return f"Error reading file:{e}"
        if os.path.getsize(abs_path) > 10000:
            file_content_string += (f'\n ...File "{file_path}" truncated at 10000 characters')
        return file_content_string