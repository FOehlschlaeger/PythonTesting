import os
import re


def repair_broken_line(filepath: str) -> str:
    """
    repair_broken_line fixes lines in given file with unintentionally broken new lines
    source: https://stackoverflow.com/questions/17373118/read-previous-line-in-a-file-python
    source: https://stackoverflow.com/questions/10140281/how-to-find-out-whether-a-file-is-at-its-eof

    Args:
        filepath (str): path to file to be fixed

    Returns:
        str: path to file with fixed lines
    """
    if not isinstance(filepath, str):
        raise TypeError(f"{filepath} has to be of type str.")
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"{filepath} is not found.")
    filepath_cleaned = os.path.splitext(filepath)[0] + "_cleaned" + os.path.splitext(filepath)[1]
    with open(filepath, "r", encoding="utf-16le") as orig_file:
        with open(filepath_cleaned, "w", encoding="utf-16le") as fixed_file:
            if orig_file:
                current_line = orig_file.readline()
            for line in orig_file:
                prev_line = current_line
                current_line = line
                if not re.match(r"^[a-zA-Z]:\\.*", current_line) and re.match(r"^[a-zA-Z]:\\.*", prev_line):
                    new_line = prev_line.strip("\n") + current_line
                    print(f"newline = {new_line}")
                    fixed_file.write(new_line)
                elif not re.match(r"^[a-zA-Z]:\\.*", prev_line) and re.match(r"^[a-zA-Z]:\\.*", current_line):
                    continue
                else:
                    fixed_file.write(prev_line)
            else:
                fixed_file.write(line)
    return filepath_cleaned


def del_spaces(filepath: str) -> str:
    """
    del_spaces deletes spaces in given txt file between all characters

    Args:
        filepath (str): path to the file to be cleaned

    Returns:
        str: string to the cleaned file while keeping the original file untouched
    """
    if not isinstance(filepath, str):
        raise TypeError(f"{filepath} must be of type string.")
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"{filepath} is not found.")
    filepath_cleaned = os.path.splitext(filepath)[0] + "_cleaned" + os.path.splitext(filepath)[1]
    with open(filepath, "r", encoding="utf-16le") as orig_file:
        with open(filepath_cleaned, "w", encoding="utf-16le") as file_fixed:
            newline = ""
            for line in orig_file:
                entry_list = line.split("\t")
                fixed_entry_list = [x[::2] for x in entry_list]
                fixed_line = "\t".join(fixed_entry_list)
                file_fixed.write(newline + fixed_line)
                newline = "\n"
    return filepath_cleaned
