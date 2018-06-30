from pathlib import Path

# Zaehle die Anzahl Ordner in einem Ordner (inkl. allen Unterordnern)

def count_dirs(path):
    subdirs = [subdir for subdir in path.iterdir() if subdir.is_dir()] #Bestimme die direkten Unterordner des Ordners path
    count = 1   # Spielwiese selbst
    for subdir in subdirs:
        count += count_dirs(subdir) # fuer jedes einzelne Kind
    return count

count = count_dirs(Path("O:\Spielwiese"))
print(count)


# Iterative Lösung