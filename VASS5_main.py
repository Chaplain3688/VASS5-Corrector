import os
import pandas as pd
import json
import dicts_creator as dicre
import auto_adjust_columns as aac
import program_writer as pw

input_path = "C:\\Users\\inzun\\OneDrive\\Persona Fisica\\Proyectos\\Puebla VW\\VW371 Jetta\\05 Tasks\\2025 CW40 USTW5\\Correciones_USTW5"
robots_path = os.path.join(input_path, "Robots")
datalists_path = os.path.join(input_path, "Data Lists")
output_file_path = os.path.join(input_path, "Corrected_Programs")

robotsdata_filename_path = os.path.join(datalists_path, "robots_data.xlsx")
robot_json_file = os.path.join(datalists_path, "robots_data.json")

programslist_filename_path = os.path.join(datalists_path, "programs_list.xlsx")
programs_json_file = os.path.join(datalists_path, "programs_list.json")

points_parameterslist_filename_path = os.path.join(datalists_path, "points_parameters_list.xlsx")
points_parameters_json_file = os.path.join(datalists_path, "points_parameters_list.json")

points_logic_list_filename_path = os.path.join(datalists_path, "points_logic_list.xlsx")
points_logic_list_json_file = os.path.join(datalists_path, "points_logic_list.json")

points_positions_list_filename_path = os.path.join(datalists_path, "points_positions_list.xlsx")
points_positions_list_json_file = os.path.join(datalists_path, "points_positions_list.json")

if __name__ == "__main__":

    robots_list = dicre.create_robots_list(robots_path)
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

    points_parameters_list = dicre.create_points_parameters_list(robots_list, programs_list)
    points_parameters_list_df = pd.DataFrame(points_parameters_list)
    points_parameters_list_df.to_excel(points_parameterslist_filename_path, index=False)
    aac.auto_adjust_columns(points_parameterslist_filename_path)

    with open(points_parameters_json_file, 'w') as json_file:
        json.dump(points_parameters_list, json_file, indent=4)

    points_logic_list = dicre.create_points_logic_list(robots_list, programs_list)
    points_logic_list_df = pd.DataFrame(points_logic_list)
    points_logic_list_df.to_excel(points_logic_list_filename_path, index=False)
    aac.auto_adjust_columns(points_logic_list_filename_path)

    with open(points_logic_list_json_file, 'w') as json_file:
        json.dump(points_logic_list, json_file, indent=4)

    points_positions_list = dicre.create_points_positions_list(robots_list, programs_list)
    points_positions_list_df = pd.DataFrame(points_positions_list)
    points_positions_list_df.to_excel(points_positions_list_filename_path, index=False)
    aac.auto_adjust_columns(points_positions_list_filename_path)

    with open(points_positions_list_json_file, 'w') as json_file:
        json.dump(points_positions_list, json_file, indent=4)

    pw.write_program(output_file_path, robots_list, programs_list, points_parameters_list, points_logic_list, points_positions_list)