## JSON files Exercises
import json
import sys

# Open the JSON file
def load_json(filename):
    with open(filename, "r") as jsonfile: 
        data = json.load(jsonfile)
    return data


# Write to the JSON file
def save_json(data, filename):
    with open(filename, "w") as jsonfile: 
        json.dump(data, jsonfile)


# Convert the loaded data into a list
def convert_format(data):
    annotations = data["annotations"]
    images = data["images"] 
    for annotation in annotations:
        del annotation["image_id"]
        for image in images:
            image.update({"annotations": annotation})
    return images


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please give the input and output filename of the JSON files")
        print("Example: python chap06_5_sys.py input.json output.json")
        exit()


data = load_json(sys.argv[1])
reformatted_data = convert_format(data)
save_json(reformatted_data, sys.argv[2])
