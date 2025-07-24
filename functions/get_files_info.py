import os






def get_files_info(working_directory, directory="."):
    dir_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    
    
    if not full_path.startswith(dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'    


    return return_string(full_path)

def return_string(full_path):
    try:
        files_info = []
        for filename in os.listdir(full_path):
            filepath = os.path.join(full_path, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"