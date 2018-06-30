from pathlib import Path

def fak(n):
    if n == 0:
        return 1
    else:
        return n * fak(n - 1)

def count_dirs(path):
    try:
        subdirs = [subdir for subdir in path.iterdir() if subdir.is_dir()] # Bestimmte die direkten Unterordner des Ordners path
        count = 1
        for subdir in subdirs:
            count += count_dirs(subdir)

        return count
    except PermissionError:
        return 1


# 1) Berechne die Fakultät einer Zahl rekursiv
zahl = 4
print(zahl, "! ist:", fak(zahl))


# 2) Zähle die Ordner in einem Ordner rekursiv

#count = count_dirs(Path("C:\Program Files"))
count = count_dirs(Path("O:\Spielwiese"))
print(count)
