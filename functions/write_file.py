import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        dir_path = os.path.dirname(target_dir)
        os.makedirs(dir_path, exist_ok=True)
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        with open(target_dir,"w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: {str(e)}'
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
