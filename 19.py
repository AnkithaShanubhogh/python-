import os

def display_contents(path,indent=0):
    if not os.path.exists(path):
        print("Invalid path")
        return
    items=os.listdir(path)
    for item in items:
        full_path=os.path.join(path,item)
        if os.path.isdir(full_path):
            print(" " * indent + f"[DIR]{item}")
            display_contents(full_path,indent+4)
        else:
            file_type=os.path.splitext(item)[1][1:] or "No Extension"
            print(" " * indent + f"[FILE]{item} (type:{file_type})")

folder_path=input("Enter folder path:")
display_contents(folder_path)
