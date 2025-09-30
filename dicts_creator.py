import os
import pandas as pd
import patterns
import VASS5_main as vassm


robotsdata_filename_path = os.path.join(vassm.input_path, "robots_data.xlsx")

df_robots = pd.read_excel(robotsdata_filename_path)

#Read the content of a file and divide it into lines
def read_program_file(file_name):
    with open(file_name, "r") as f:
        content = f.read() 
    lines = content.splitlines()
    return lines

def create_programs_list(robots):
    all_programs_data = []
    for robot in robots:
        robot_id = robot["robot_id"]
        row_data = {}
        for program_name in robot["Programs"]:

            program_lines = read_program_file(os.path.join(robot["Saved Path"], program_name))
            program_data = get_program_main_data(program_lines)

            row_data = {
            "robot_id": robot_id,
            "program_id": program_name,
            "Program": program_name,
            "Program Name": program_data["Program Name"],
            "Comment": program_data["Comment"],
            "File Name": program_data["File Name"]
        }

            all_programs_data.append(row_data)

    return all_programs_data

def get_program_main_data(program_lines):
    program_data = {
        "Program Name": None,
        "Comment": None,
        "File Name": None
    }

    for line in program_lines:
        prog_name_match = patterns.program_name_pattern.match(line)
        if prog_name_match:
            program_data["Program Name"] = prog_name_match.group(1).strip()
            continue

        comment_match = patterns.program_comment_pattern.match(line)
        if comment_match:
            program_data["Comment"] = comment_match.group(1).strip()
            continue

        file_name_match = patterns.program_filename_pattern.match(line)
        if file_name_match:
            program_data["File Name"] = file_name_match.group(1).strip()
            continue

    return program_data

def create_points_list(robots, programs):
    all_points_data = []

    robots_by_id = {robot["robot_id"]: robot for robot in robots}
    for program in programs:            
            robot_id = program["robot_id"]
            
            current_robot = robots_by_id.get(robot_id)

            program_lines = read_program_file(os.path.join(current_robot["Saved Path"], program["Program"]))
            row_data = {}
            for line in program_lines:
                if patterns.point_pattern.match(line):
                    row_data = {
                        "robot_id": program["robot_id"],
                        "program_id": program["program_id"],
                        "point_id": patterns.point_pattern.match(line).group(2),
                        "Line Number": patterns.point_pattern.match(line).group(1) if patterns.point_pattern.match(line).group(1) else None
                    }
                    all_points_data.append(row_data)

    return all_points_data

