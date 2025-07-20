import os






def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    print(os.path.abspath(directory))
    if working_directory not in os.path.abspath(directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    return full_path
print(get_files_info("calculator", "pkg"))
