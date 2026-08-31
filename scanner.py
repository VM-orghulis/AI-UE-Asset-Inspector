import os
import json

folder = input("Asset folder: ")

asset_data = {
    "asset_folder": folder,
    "instances": [],
    "materials": [],
    "textures": [],
    "tree_assets": []
}

for root, dirs, files in os.walk(folder):

    for file in files:
        path = os.path.join(root, file)

        relative_path = os.path.relpath(path, folder)
        first_folder = relative_path.split(os.sep)[0]

        if first_folder == "Instances":
            asset_data["instances"].append(file)

        elif first_folder == "Materials":
            asset_data["materials"].append(file)

        elif first_folder == "Textures":
            asset_data["textures"].append(file)

        else:
            asset_data["tree_assets"].append(file)

with open("asset_report.json", "w", encoding="utf-8") as f:
    json.dump(asset_data, f, indent=2, ensure_ascii=False)

print("Asset report saved to asset_report.json")