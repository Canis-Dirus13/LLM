import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if target_file[-2:] != 'py':
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args is not None:
            command.extend(args)
        command_subprocess = subprocess.run(command, capture_output=True, text=True, timeout=30)
        output_str = ''
        if command_subprocess.returncode != 0:
            output_str += f"Process exited with code {command_subprocess.returncode}"
        if command_subprocess.stdout == '' and command_subprocess.stderr == '':
            output_str += 'No output produced'
        else:
            output_str += f'STDOUT: {command_subprocess.stdout}, STDERR: {command_subprocess.stderr}'
        return output_str
        
    except Exception as e:
        return f"Error: executing Python file: {e}"