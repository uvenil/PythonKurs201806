from pathlib import Path

# Zähle die Anzahl Ordner in einem Ordner (inkl. allen Unterordnern)
def count_dirs(path):
    try:
        subdirs = [subdir for subdir in path.iterdir() if subdir.is_dir()] # Bestimme die direkten Unterordner des Ordners Path
        print(subdirs)
        count = 1
        for subdir in subdirs:
            count += count_dirs(subdir)

        return count
    except PermissionError:
        return 1

count1 = count_dirs(Path("O:\Spielwiese"))
print(count1)
print()

