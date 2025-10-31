import os
import shutil

print("")
print("--------------------------------------")
print("Move all .jpg files from one folder to another")
print("--------------------------------------")
print("")

source = input("Enter the source folder path: ").strip()
destination = input("Enter the destination folder path: ").strip()
print("")

if not os.path.exists(source):
    print("Source folder does not exist. Please check the path.")
else:
    os.makedirs(destination, exist_ok=True)
    count = 0

    for file in os.listdir(source):
        if file.lower().endswith(".jpg"):
            src_path = os.path.join(source, file)
            dest_path = os.path.join(destination, file)
            shutil.move(src_path, dest_path)
            count += 1
            print(f"Moved: {file}")

    print("")
    if count == 0:
        print("No .jpg files found in the source folder.")
    else:
        print(f"{count} .jpg files moved successfully to {destination}")

