import json

# Open file by entering the filename in the same directory
with open("pos_10010.png.json", "r") as f:
    data = json.load(f)

# Output list
output = []

# Input file name
input_filename = "pos_10010.png.json"

# Dataset
dataset = {
    "dataset_name": input_filename,
    "image_link": "",
    "annotation_type": "image",
    "annotation_objects": {},
    "annotation_attributes": {}
}

vehicle_present = False
license_plate_present = False

for obj in data["objects"]:
    class_title = obj["classTitle"]
    points = obj["points"]

    if class_title == "Vehicle":
        vehicle_present = True
    elif class_title == "License Plate":
        license_plate_present = True

    # annotation_objects futher information
    dataset["annotation_objects"][class_title.lower()] = {
        "presence": 1,
        "bbox": points["exterior"][0] + points["exterior"][1]
    }

    # Object's attribute
    attributes = {}

    for tag in obj["tags"]:
        attributes[tag["name"]] = tag["value"]

    dataset["annotation_attributes"][class_title.lower()] = attributes

# Vehicle and license plate not present
if not vehicle_present:
    dataset["annotation_objects"]["vehicle"] = {
        "presence": 0,
        "bbox": []
    }
if not license_plate_present:
    dataset["annotation_objects"]["license_plate"] = {
        "presence": 0,
        "bbox": []
    }

if not vehicle_present:
    dataset["annotation_attributes"]["vehicle"] = {
        "Type": None,
        "Pose": None,
        "Model": None,
        "Make": None,
        "Color": None
    }
if not license_plate_present:
    dataset["annotation_attributes"]["license_plate"] = {
        "Difficulty Score": None,
        "Value": None,
        "Occlusion": None
    }

output.append(dataset)


# Write the output
with open("formatted_"+input_filename, "w") as f:
    json.dump(output, f, indent=4)
