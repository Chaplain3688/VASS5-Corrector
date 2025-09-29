import os
import pandas as pd
import ast
import VASS5_patterns as vassp
import VASS5_main as vassm

robotsdata_filename_path = os.path.join(vassm.input_path, "robots_data.xlsx")

df_robots = pd.read_excel(robotsdata_filename_path)

#Read the content of a file and divide it into lines
def read_program_file(file_name):
    with open(file_name, "r") as f:
        content = f.read() 
    lines = content.splitlines()
    return lines

def get_program_main_data(program_lines):
    program_data = {
        "Program Name": None,
        "Comment": None,
        "File Name": None
    }

    for line in program_lines:
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

def safe_literal_eval(s):
    try:
        return ast.literal_eval(s)
    except (ValueError, SyntaxError):
        # Return an empty list if the string is malformed or not a list
        return []

def create_programs_list(robots):
    all_programs_data = []
    for robot in robots:
        robot_id = robot["robot_id"]
        for program_name in robot["Programs"]:
            row_data = {
            "robot_id": robot_id,
            "program_id": program_name,
            "Program": program_name
        }
        
            all_programs_data.append(row_data)

    return all_programs_data

def create_points_list(programs, robots):
    all_points_data = []
    for program in create_programs_list(robots):
            
            program_lines = read_program_file(file_name)
            program = get_program_main_data(program_lines)
            
            row_data = {
                "robot_id": robot["robot_id"],
                "program_id": robot["program_id"],
                "Program": program_name,
                "Program Name": program_data["Program Name"],
                "Comment": program_data["Comment"],
                "File Name": program_data["File Name"]
            }
        
            all_points_data.append(row_data)

    return all_points_data

