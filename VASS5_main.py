import os
import fnmatch
import re
import pandas as pd
import VASS5_patterns as vassp

input_path = "C:\\Users\\inzun\\OneDrive\\Persona Fisica\\03 Proyectos\\Puebla VW\\VW371 Jetta\\05 Tasks\\2025 CW40 USTW5\\Correciones_USTW5"
robotsdata_filename_path = os.path.join(input_path, "robots_data.xlsx")
robots= []

def store_robots(input_path, robots):
    for root, ____, files in os.walk(input_path):
        for file in files:
            robot_full_name = os.path.basename(root)
            robot_full_name = robot_full_name.upper()

            if any(r["Robot Full Name"] == robot_full_name for r in robots):
                robot["Programs"].append(file)
                continue

            match_robot = re.search(vassp.robot_name_pattern, robot_full_name)
            line = ('K'+ match_robot.group(1))
            robot_name = (match_robot.group(4) + 'R' + match_robot.group(5))
            
            robot = {
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

#Read the content of a file and divide it into lines
def read_program_file(file_name):
    with open(file_name, "r") as f:
        content = f.read() 
    lines = content.splitlines()
    return lines

if __name__ == "__main__":

    store_robots(input_path, robots)
    robots_df = pd.DataFrame(robots)
    robots_df.to_excel(robotsdata_filename_path, index=False)

