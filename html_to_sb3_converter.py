import os
import json

def convert_html_to_sb3(html_file_path, sb3_file_path):
    # Read the HTML file
    with open(html_file_path, 'r') as html_file:
        html_content = html_file.read()

    # Create the sb3 file structure
    sb3_data = {
        "targets": [{
            "isStage": True,
            "name": "Stage",
            "variables": {},
            "blocks": {},
            "costumes": [],
            "sounds": [],
            "blocksPosition": {},
            "scripts": [],
            "currentCostumeIndex": 0,
            "penLayerMD5": None,
            "tempoBPM": 60,
            "videoTransparency": 50,
            "children": []
        }],
        "meta": {
            "semver": "3.0.0",
            "vm": "0.2.0",
            "agent": "https://sheeptester.github.io/htmlifier/",
            "projectId": "",
            "flashVersion": "",
            "userAgent": "",
            "hasCloudData": False
        }
    }

    # Set the HTML content as the script of the stage
    sb3_data["targets"][0]["scripts"] = [[10, 10, [["whenGreenFlag"], ["doPlaySoundAndWait", "Untitled"]]]]
    sb3_data["targets"][0]["sounds"] = [{"soundName": "Untitled", "soundID": "untitled", "md5": "f9ed3be09cc6a79e3619f29a62eb2f11.wav", "sampleCount": 124416, "rate": 44100, "format": ""}]
    sb3_data["targets"][0]["blocks"] = {}
    sb3_data["targets"][0]["blocksPosition"] = {}

    # Write the sb3 file
    with open(sb3_file_path, 'w') as sb3_file:
        json.dump(sb3_data, sb3_file, indent=2)

    print(f"Conversion successful. Output file: {sb3_file_path}")

# Example usage:
html_file_path = "example.html"
sb3_file_path = "output.sb3"
convert_html_to_sb3(html_file_path, sb3_file_path)
