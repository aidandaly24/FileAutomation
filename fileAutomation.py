import os

sourceDir = "/Users/aidandaly/Downloads"

with os.scandir(sourceDir) as entries:
    for entry in entries:
        print(entry.name)
