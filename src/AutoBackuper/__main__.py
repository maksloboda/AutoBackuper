import subprocess
import sys
import time

# https://stackoverflow.com/a/3431838
# https://creativecommons.org/licenses/by-sa/4.0/
####
import hashlib
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
####

def printerr(msg):
    print(msg, file=sys.stderr)


def parse_arguments():
    if len(sys.argv) != 3:
        printerr("Incorrect arguments!")
        printerr("Correct use: command [check delay in seconds] [file name]")
        sys.exit(1)

    delay_str = sys.argv[1]
    file_str = sys.argv[2]
    delay = None
    try:
        delay = int(delay_str)
    except ValueError:
        printerr("Invalid time specified!")
        sys.exit(1)

    return (delay, file_str)

def can_read_file(file_name):
    try:
        with open(file_name, "r") as f:
            pass
    except OSError:
        return False
    return True

def main():
    delay, file_name = parse_arguments()
    try:
        subprocess.run(["git", "init"])
    except CalledProcessError:
        printerr("git init failed!")
        sys.exit(1)
    last_md5 = ""
    while True:
        if not can_read_file(file_name):
            print(f"File is mising or cant be read at {file_name}")
        else:
            value = md5(file_name)
            if last_md5 == value:
                print("md5 match, nothing to do")
            else:
                try:
                    subprocess.run(["git", "add", "--", file_name])
                    subprocess.run(["git", "commit", "-m", f'"Auto Backup md5 {value}"',
                            "-o", "--", file_name])
                    last_md5 = value
                except CalledProcessError:
                    printerr("git commit failed!")
        time.sleep(delay)



if __name__ == "__main__":
    main()
