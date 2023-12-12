import os
import shutil
import time


def get_files_in_current_directory():
    return [f for f in os.listdir() if os.path.isfile(f)]


def is_file_modified_in_last_24_hours(file):
    file_time = max(os.path.getmtime(file), os.path.getctime(file))
    return (time.time() - file_time) / 3600 <= 24


def update_file(file):
    with open(file, "a") as f:
        f.write(f"\nUpdated at {time.ctime()}")


def move_file_to_directory(file, directory):
    shutil.move(file, directory)


def main():
    files = get_files_in_current_directory()
    for file in files:
        if is_file_modified_in_last_24_hours(file):
            update_file(file)
            if not os.path.exists("last_24hours"):
                os.makedirs("last_24hours")
            move_file_to_directory(file, "last_24hours")


if __name__ == "__main__":
    main()

