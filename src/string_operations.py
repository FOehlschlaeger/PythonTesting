import os
import re
#from itertools import tee, izip


def pairwise(iterable): 
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def repair_broken_line(filepath: str) -> str:
    """
    repair_broken_line fixes lines in given file with unintentionally broken new lines

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
                #fixed_file.write(current_line)
            #while True:
            for line in orig_file:
            #for first_line, second_line in pairwise(orig_file):
                prev_line = current_line #orig_file.readline()
                current_line = line #next(orig_file, None) #orig_file.readline()
                print(f"prev_line = {prev_line}")
                print(f"current_line = {current_line}")
                if not current_line:
                    fixed_file.write(prev_line)
                    fixed_file.write(current_line)
                    break # EOF
                #if not second_line.startswith(r"^[a-zA-Z]:\\.*"):
                if not re.match(r"^[a-zA-Z]:\\.*", current_line) and re.match(r"^[a-zA-Z]:\\.*", prev_line):
                    new_line = prev_line.strip("\n") + current_line
                    print(f"newline = {new_line}")
                    fixed_file.write(new_line)
                    #current_line = line
                elif not re.match(r"^[a-zA-Z]:\\.*", prev_line) and re.match(r"^[a-zA-Z]:\\.*", current_line):
                    continue #fixed_file.write(current_line)
                else: 
                    fixed_file.write(prev_line)
                    #fixed_file.write(current_line)
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
