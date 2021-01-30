import os
import random


random.seed(1)


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