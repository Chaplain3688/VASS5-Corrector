import os
import fnmatch
import re
import VASS5_patterns as vassp

search_path = "C:\\Users\\inzun\\OneDrive\\Persona Fisica\\03 Proyectos\\Puebla VW\\VW371 Jetta\\05 Tasks\\2025 CW40 USTW5\\Correciones_USTW5"
search_pattern = "folge05?.ls"

#Find all folges for Jetta in the specified directory and its subdirectories
def search_for_jetta_folges(search_path, search_pattern):
    folges_jetta = []

    for root, dirs, files in os.walk(search_path):
        for file in files:
            filename = file.lower()
            if fnmatch.fnmatch(filename, search_pattern):
                full_path = os.path.join(root, filename)
                folges_jetta.append(full_path)

    return folges_jetta

#Read the content of a file and divide it into lines
def read_folge_file(file_name):
    with open(file_name, "r") as f:
        content = f.read() 
    lines = content.splitlines()
    return lines

def get_program_data(lines):
    program_data = {
        "Program Name": None,
        "Comment": None,
        "File Name": None
    }

    for line in lines:
        prog_name_match = vassp.program_name_pattern.match(line)
        if prog_name_match:
            program_data["Program Name"] = prog_name_match.group(1).strip()
            continue

        comment_match = vassp.program_comment_pattern.match(line)
        if comment_match:
            program_data["Comment"] = comment_match.group(1).strip()
            continue

        file_name_match = vassp.program_filename_pattern.match(line)
        if file_name_match:
            program_data["File Name"] = file_name_match.group(1).strip()
            continue

    return program_data

if __name__ == "__main__":
    folges_jetta = search_for_jetta_folges(search_path, search_pattern)