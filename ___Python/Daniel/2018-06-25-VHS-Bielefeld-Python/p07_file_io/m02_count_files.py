from pathlib import Path

# Zähle die Anzahl Ordner in einem Ordner (inkl. allen Unterordnern)

def count_dirs(path):
    try:
        subdirs = [subdir for subdir in path.iterdir() if subdir.is_dir()] # Bestimmte die direkten Unterordner des Ordners path
        count = 1
        for subdir in subdirs:
            count += count_dirs(subdir)

        return count
    except PermissionError:
        return 1


#count = count_dirs(Path("C:\Program Files"))
#count = count_dirs(Path("/home/micha/Schreibtisch/fundus/PythonKurs201806"))
count = count_dirs(Path("/home/micha/Schreibtisch/fundus/PythonKurs201806/___Python"))
#count = count_dirs(Path("/home/micha/Schreibtisch/fundus/server"))
print(count)


