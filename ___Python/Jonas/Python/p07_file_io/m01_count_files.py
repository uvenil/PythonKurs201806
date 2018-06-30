from pathlib import Path

# Zähle die Anzahl Ordner in einem Ordner (inklusive allen Unterordnern)

def count_dirs(path):
    subdirs = [subdir for subdir in path.iterdir() if subdir.is_dir()] #bestimme die direkten Unterordner des Ordners path
    count = 1 #zähle ersten Ordner mit
    for subdir in subdirs:
        count += count_dirs(subdir)

    return count

count = count_dirs(Path("O:\Spielwiese"))
print(count)

