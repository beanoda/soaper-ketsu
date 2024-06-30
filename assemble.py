"""
This script's purpose is to assemble the files in the `src/` directory
into a json file that can be used in KETSU

- Requires Jsmin@3.0.1

P.S.

Yeah I know it's a javascript project but I don't like JS
"""

import os
import json
import sys
import re
from typing import Dict, Any, List
import jsmin


SOURCE_DIRECTORY = "src"
SOURCE_SUB_DIRECTORIES_TO_JSON_OBJECT_MAP: Dict[str, str] = {
    "MainPage": "mainPage",
    "Search": "search",
    "Info": "info",
    "Chapters": "chapters"
}
OUTPUT_INDENT_LEVEL = 4


if __name__ == "__main__":
    # this print statement just makes everything look nice
    print("\n\n--- STARTING ASSEMBLE ---\n")

    assert len(sys.argv) == 2
    output_file_name: str = sys.argv[1]

    output_file_path = f"{output_file_name}.json"
    assert os.path.exists(output_file_path)
    print(f"File path exists -> {output_file_path}")

    with open(output_file_path, "r") as output_file_read_mode:
        json_data: Dict[str, Any] = json.load(output_file_read_mode)
        print(f"Got JSON Data from -> {output_file_path}")
    
    for sub_directory, json_key in SOURCE_SUB_DIRECTORIES_TO_JSON_OBJECT_MAP.items():
        print("")

        sub_directory_path: str = os.path.join(SOURCE_DIRECTORY, sub_directory)
        
        assert os.path.exists(sub_directory_path)
        print(f"File path exists -> {sub_directory_path}")

        files_in_sub_directory: List[str] = os.listdir(sub_directory_path)

        assert len(files_in_sub_directory) > 0
        print(f"Directory, {sub_directory_path}, is not empty")

        javascript_file_path: str = os.path.join(sub_directory_path, files_in_sub_directory[0])
        print(f"Found file at path -> {javascript_file_path}")
        
        with open(javascript_file_path, "r") as javascript_file:
            file_contents: str = javascript_file.read()
            print(f"Read Javascript File contents from -> {javascript_file_path}")

        no_script_tag_pattern = r'<script\s+type="text/javascript">\s*|</script>'
        no_script_tag_main_page: str = re.sub(no_script_tag_pattern, '', file_contents)
        print(f"Removed Script Tags from -> {javascript_file_path}")

        minified_javscript_code: str = jsmin.jsmin(no_script_tag_main_page) 
        print(f"Minified Javscript at -> {javascript_file_path}")

        json_data[json_key][0]["javascriptConfig"]["javaScript"] = minified_javscript_code

    print("")

    with open(output_file_path, "w") as output_file_write_mode:
        json.dump(json_data, output_file_write_mode, indent=OUTPUT_INDENT_LEVEL)
        print(f"Wrote Json Data to -> {output_file_path}")