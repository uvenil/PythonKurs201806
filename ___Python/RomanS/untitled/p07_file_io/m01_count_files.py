from pathlib import Path

# Zähle die Anzahl Ordner in einem Ordner (incl. aller Unterordner)

def count_dirs(path):
    subdirs = [subdir for subdir in path.iterdir() if subdir.is_dir()]
    count = 0
    for subdir in subdirs:
        count += count_dirs(subdir)
    return count + 1

count= count_dirs(Path("O:\Spielwiese"))
# count= count_dirs(Path("C:\Program Files"))

print(count)