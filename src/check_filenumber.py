import os
import random


random.seed(1)

def del_spaces(filepath: str) -> str:
    """
    del_spaces deletes spaces in given txt file between all characters

    Args:
        filepath (str): path to the file to be cleaned

    Returns:
        str: string to the cleaned file while keeping the original file untouched
    """
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


def make_path(filepath: str, folder: str) -> str:
    if filepath.endswith("/"):
        filepath = filepath.rsplit("/")[0]

    if not os.path.exists(f"{filepath}/{folder}"):
        os.makedirs(f"{filepath}/{folder}")
    return f"{filepath}/{folder}"


def create_files(filepath: str, number: int, limit: int) -> None: 
    path_to_folder = make_path(filepath, "test")
    print(path_to_folder)

    for i in range(number):
        with open(f"{path_to_folder}/testfile{i}.txt", "w") as file: 
            for j in range(random.randrange(limit)):
                file.write(f"tesfile{i}_{j}\n")
    return None


def more_lines_than_limit(file: str, limit: int) -> bool:
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("limit has to be an integer larger than zero. ")
    
    numlines = sum(1 for line in open(file, "r"))
    if numlines > limit:
        default = True
    else:
        default = False
    return default


def main(): 
    create_files("data", 3, 10)

    filelist = []
    d = "data/test"
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isfile(full_path):
            print(full_path)
            filelist.append(full_path)
    print(f"files to check : {filelist}")

    for files in filelist: 
        print(more_lines_than_limit(files, 5))
    
    print(more_lines_than_limit('data/test\\testfile2.txt', "a"))


if __name__ == "__main__": 
    print("starting... ")
    main()
    print("finished")