import os
import re
import pandas as pd
import json
import patterns
import dicts_creator as dicre
import auto_adjust_columns as aac

input_path = "C:\\Users\\inzun\\OneDrive\\Persona Fisica\\Proyectos\\Puebla VW\\VW371 Jetta\\05 Tasks\\2025 CW40 USTW5\\Correciones_USTW5"
robotsdata_filename_path = os.path.join(input_path, "robots_data.xlsx")
robot_json_file = os.path.join(input_path, "robots_data.json")

programslist_filename_path = os.path.join(input_path, "programs_list.xlsx")
programs_json_file = os.path.join(input_path, "programs_list.json")

pointslist_filename_path = os.path.join(input_path, "points_list.xlsx")
points_json_file = os.path.join(input_path, "points_list.json")

def create_robots_list(input_path):
    robots= []
    for root, ____, files in os.walk(input_path):
        for file in files:
            robot_full_name = os.path.basename(root)
            robot_full_name = robot_full_name.upper()

            if any(r["Robot Full Name"] == robot_full_name for r in robots):
                robot["Programs"].append(file)
                continue

            match_robot = re.search(patterns.robot_name_pattern, robot_full_name)
            if match_robot is None:
                continue

            line = ('K'+ match_robot.group(1))
            robot_id = (match_robot.group(1)[1:] + match_robot.group(2) + match_robot.group(4) + 'R' + match_robot.group(5))
            robot_name = (match_robot.group(4) + 'R' + match_robot.group(5))
            
            robot = {
    "robot_id": robot_id,
    "Robot Full Name": robot_full_name,
    "Line": line,
    "ARG": match_robot.group(2),
    "SK": match_robot.group(3),
    #"Line Name": line_names[line],
    "Robot": robot_name,
    "Saved Path": root,
    "Programs": [file],
}
            
            robots.append(robot)
    return robots

if __name__ == "__main__":

    robots_list = create_robots_list(input_path)
    robots_df = pd.DataFrame(robots_list)
    robots_df.to_excel(robotsdata_filename_path, index=False)
    aac.auto_adjust_columns(robotsdata_filename_path)

    with open(robot_json_file, 'w') as json_file:
        json.dump(robots_list, json_file, indent=4)

    programs_list = dicre.create_programs_list(robots_list)
    programs_list_df = pd.DataFrame(programs_list)
    programs_list_df.to_excel(programslist_filename_path, index=False)
    aac.auto_adjust_columns(programslist_filename_path)

    with open(programs_json_file, 'w') as json_file:
        json.dump(programs_list, json_file, indent=4)

