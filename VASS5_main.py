import os
import pandas as pd
import json
import dicts_creator as dicre
import auto_adjust_columns as aac
import program_writer as pw

input_path = r"C:\Users\inzun\OneDrive\Persona Fisica\Proyectos\Puebla VW\VW371 Jetta\05 Tasks\2025 CW40 USTW5\Correciones_USTW5"
robots_path = os.path.join(input_path, "01 Corrected_Programs_Manually")
datalists_path = os.path.join(input_path, "02 Data Lists")
output_file_path = os.path.join(input_path, "03 Corrected_Programs")

robotsdata_filename_path = os.path.join(datalists_path, "01_robots_data.xlsx")
robot_json_file = os.path.join(datalists_path, "01_robots_data.json")

programslist_filename_path = os.path.join(datalists_path, "02_programs_list.xlsx")
programs_json_file = os.path.join(datalists_path, "02_programs_list.json")

points_parameterslist_filename_path = os.path.join(datalists_path, "03_points_parameters_list.xlsx")
points_parameters_json_file = os.path.join(datalists_path, "03_points_parameters_list.json")

points_logic_list_filename_path = os.path.join(datalists_path, "04_points_logic_list.xlsx")
points_logic_list_json_file = os.path.join(datalists_path, "04_points_logic_list.json")

points_positions_list_filename_path = os.path.join(datalists_path, "05_points_positions_list.xlsx")
points_positions_list_json_file = os.path.join(datalists_path, "05_points_positions_list.json")

def create_dfs(list, excel_path, json_path):
    df = pd.DataFrame(list)
    df.to_excel(excel_path, index=False)
    aac.auto_adjust_columns(excel_path)
    with open(json_path, 'w') as json_file:
        json.dump(list, json_file, indent=4)

if __name__ == "__main__":

    robots_list = dicre.create_robots_list(robots_path)
    programs_list = dicre.create_programs_list(robots_list)
    points_parameters_list = dicre.create_points_parameters_list(robots_list, programs_list)
    points_logic_list = dicre.create_points_logic_list(robots_list, programs_list)
    points_positions_list = dicre.create_points_positions_list(robots_list, programs_list)

    create_dfs(robots_list, robotsdata_filename_path, robot_json_file)
    create_dfs(programs_list, programslist_filename_path, programs_json_file)
    create_dfs(points_parameters_list, points_parameterslist_filename_path, points_parameters_json_file)
    create_dfs(points_logic_list, points_logic_list_filename_path, points_logic_list_json_file)
    create_dfs(points_positions_list, points_positions_list_filename_path, points_positions_list_json_file)

    #pw.write_program(output_file_path, robots_list, programs_list, points_parameters_list, points_logic_list, points_positions_list)