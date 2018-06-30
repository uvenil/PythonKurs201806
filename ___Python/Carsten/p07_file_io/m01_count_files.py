from pathlib import Path

# Zähle die Anzahl Ordner in einerm Ordner (inkl. aller Unterordner)

def count_dirs(path):
    subdirs = [subdir for subdir in path.iterdir() if subdir.is_dir()] # Bestimme die direkten Unterordner des Ordners path
    print(subdirs)
    count = 0
    for subdir in subdirs:
        count += count_dirs(subdir)

    return count + 1

count = count_dirs(Path("O:\___python"))
print(count)
