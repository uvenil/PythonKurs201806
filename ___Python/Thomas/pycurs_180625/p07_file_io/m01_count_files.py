from pathlib import Path

# Zähle die Anzahle Ordner in einem Ordner (inkl. Unetrordner)


def count_dirs(path):
    try:
        subdirs = [subdir for subdir in path.iterdir() if subdir.is_dir()] # Unterordner dieses Verzeichnis
        count = 1
        for subdir in subdirs:
            count += count_dirs(subdir)
        return count
    except PermissionError:
        return 1

count = count_dirs(Path("O:\Spielwiese"))
print(count)

#problem interative