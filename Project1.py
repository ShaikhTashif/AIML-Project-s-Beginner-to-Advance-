from pathlib import Path
import os

def readfileandfolder():
    path = Path('.')  # Current directory
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please enter your new file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What do you want to write in this file? ")
                fs.write(data)
            print("✅ File created successfully.")
        else:
            print("⚠️ This file already exists.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which file do you want to read? ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print("📄 File contents:\n", data)
            print("✅ File read successfully.")
        else:
            print("⚠️ The file does not exist.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file do you want to update? ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1️⃣ Rename the file")
            print("2️⃣ Overwrite the file content")
            print("3️⃣ Append to the file")

            res = int(input("Enter your choice: "))

            if res == 1:
                name2 = input("Enter the new file name: ")
                p.rename(Path(name2))
                print("✅ File renamed successfully.")

            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("Enter new content to overwrite: ")
                    fs.write(data)
                print("✅ File overwritten successfully.")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Enter content to append: ")
                    fs.write(data)
                print("✅ Content appended successfully.")
            else:
                print("⚠️ Invalid option.")
        else:
            print("⚠️ The file does not exist.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Which file do you want to delete? ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("✅ File deleted successfully.")
        else:
            print("⚠️ No such file exists.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

# Menu
print("📁 File Manager Options:")
print("1️⃣ Create a file")
print("2️⃣ Read a file")
print("3️⃣ Update a file")
print("4️⃣ Delete a file")

check = int(input("Enter your choice: "))
if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
else:
    print("⚠️ Invalid choice.");
print("Hello I'm Tashif");
