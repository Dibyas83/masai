import os  # to delete a file import os
if os.path.exists("Copy.txt"):
    os.remove("Copy.txt")
else:
    print("doesnt exist")
os.mkdir("empfold")
os.rmdir("empfold")