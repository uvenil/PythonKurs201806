from pathlib import Path

# Anzahl Ordner inkl. Unterordner
def count_dirs(path):
    subdirs = [subdir for subdir in path.iterdir() if subdir.is_dir()]
    return len(subdirs)

path = Path("O:\Spielwiese")

def alldirs(path):
    if len(subdirs(path)) == 0:
        return
    return subdirs(path)


print(subdirs)