import os

folder = input("Asset folder: ")

for root, dirs, files in os.walk(folder):
    for file in files:
        print(os.path.join(root, file))