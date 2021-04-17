# AutoBackuper

Python3 script for backing up files. Intended use is to passively back up word or latex files in case of corruption or need to reference an older version of a file.

# Usage

Navigate to the folder where you want git repository to be located and execute: 

`python3 [path to autobackuper.py] [poll interval in seconds] [file name]`

Code will init a git repository and every `[poll interval in seconds]` check for file changes in `[file name]`, in case of a file change it will create a commit with the updated version.

# Requirements

- git
- python3