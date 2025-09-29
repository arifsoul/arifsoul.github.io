import os

def print_tree(path, indent=""):
    try:
        items = sorted(os.listdir(path))  # biar urut
    except PermissionError:
        return
    
    for i, item in enumerate(items):
        full_path = os.path.join(path, item)
        connector = "└── " if i == len(items) - 1 else "├── "
        print(indent + connector + item)
        if os.path.isdir(full_path):
            new_indent = indent + ("    " if i == len(items) - 1 else "│   ")
            print_tree(full_path, new_indent)

# Ganti dengan folder target
root_folder = r"D:\_pribadi\arifsoul.github.io\assets\img\work"
print(root_folder)
print_tree(root_folder)
