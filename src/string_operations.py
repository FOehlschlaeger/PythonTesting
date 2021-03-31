import os


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