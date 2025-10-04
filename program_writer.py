import os
import time

def create_file(path, lines):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Create the file and write lines if provided
    with open(path, 'w') as f:
        if lines:
            for line in lines:
                f.write(line + '\n')

def write_program(path, robots, programs, points_parameters_list, points_logic_list, points_positions_list):

    for robot in robots:
        new_robot_dir = os.path.join(path, robot["Robot Full Name"])
        os.makedirs(new_robot_dir, exist_ok=True)

        for program in programs:
            if robot["robot_id"] == program["robot_id"]:
                lines = []
                print("Writing program:", program["Program Name"], "for robot:", robot["Robot Full Name"])

                lines.append(write_attributes_section(program))
                print(program['Applications exists'])
                if program["Applications exists"]:
                    lines.append(write_applications_section(program))

                lines.append(write_main_section(program, points_parameters_list, points_logic_list))
                lines.append(write_pos_section(program, points_positions_list))

                
                create_file(os.path.join(new_robot_dir, program["Program Name"] + ".ls"), lines)

def write_attributes_section(program):

    lines = []
    lines.append("/PROG  " + program["Program Name"])
    lines.append("/ATTR")
    lines.append("OWNER\t\t= " + program["OWNER"] + ";")
    lines.append("COMMENT\t\t= \"" + program["COMMENT"] + "\";")
    lines.append("PROG_SIZE\t= " + str(program["PROG_SIZE"]) + ";")
    lines.append("CREATE\t\t= DATE " + program["CREATE"][:9] + " TIME " + program["CREATE"][9:] + ";")
    lines.append("MODIFIED\t= DATE " + program["MODIFIED"][:9] + " TIME " + program["MODIFIED"][9:] + ";")
    lines.append("FILE_NAME\t= " + program["FILE_NAME"] + ";")
    lines.append("VERSION\t\t= " + str(program["VERSION"]) + ";")
    lines.append("LINE_COUNT\t= " + str(program["LINE_COUNT"]) + ";")
    lines.append("MEMORY_SIZE\t= " + str(program["MEMORY_SIZE"]) + ";")
    lines.append("PROTECT\t\t= " + program["PROTECT"] + ";")
    if program["STORAGE"]:
        lines.append("STORAGE\t\t= " + program["STORAGE"] + ";")
    lines.append("TCD:  STACK_SIZE\t= " + str(program["STACK_SIZE"]) + ",")
    lines.append("      TASK_PRIORITY\t= " + str(program["TASK_PRIORITY"]) + ",")
    lines.append("      TIME_SLICE\t= " + str(program["TIME_SLICE"]) + ",")
    lines.append("      BUSY_LAMP_OFF\t= " + str(program["BUSY_LAMP_OFF"]) + ",")
    lines.append("      ABORT_REQUEST\t= " + str(program["ABORT_REQUEST"]) + ",")
    lines.append("      PAUSE_REQUEST\t= " + str(program["PAUSE_REQUEST"]) + ";")
    lines.append("DEFAULT_GROUP\t= " + program["DEFAULT_GROUP"] + ";")
    lines.append("CONTROL_CODE\t= " + program["CONTROL_CODE"] + ";")
    
    output = "\n".join(lines)
    return output

def write_applications_section(program):

    lines = []
    lines.append("/APPL")
    if program["Applications"]:
        for app_line in program["Applications"]:
            lines.append(app_line)

    output = "\n".join(lines)
    return output

def write_main_section(program, points_parameters, points_logic):

    program_points = []        

    for point in points_logic:
        if program["robot_id"] == point["robot_id"] and program["program_id"] == point["program_id"]:
            match_point = point.copy()
            if program["program_id"].lower().startswith("makro"):
                program_points.append(match_point)
            else:
                for point in points_parameters:
                    if program["robot_id"] == point["robot_id"] and program["program_id"] == point["program_id"] and match_point["point_id"] == point["point_id"]:
                        match_point.update(point)
                        program_points.append(match_point)

    lines = []
    lines.append("/MN")

    for point in program_points:
        if point["Comments"]:
            for comment in point["Comments"]:
                lines.append(comment)
                #print("Adding comment:", comment)

        if not program["program_id"].lower().startswith("makro"):

            spaces_line_number = 4 - int(len(point["Line Number"]))

            point_parameter = ((spaces_line_number * " ") + str(point["Line Number"]) + ":" + 
                               point["Movement Type"] + " P[" + 
                               str(point["point_id"]) + "] " + 
                               str(point["Speed Value"]) + 
                               point["Speed Type"] + " " + 
                               point["Continuity Type"] + 
                               str(point["Continuity Value"]))


            if point["ACC Type"]:
                point_parameter += " ACC" + str(point["ACC Value"])

            point_parameter += " " + point["TB/DB Type"] + "   " + str(point["TB/DB Value"]) + point["TB/DB Unit"] + point["Additional Parameters"]

            lines.append(point_parameter + ";")

        if point["Logic"]:
            for logic in point["Logic"]:
                lines.append(logic)
                #print("Adding logic:", logic)

        if not program["program_id"].lower().startswith("makro"):
            lines.append("       ------ ;")

    output = "\n".join(lines)
    return output

def write_pos_section(program, points_positions):
    lines = []

    lines.append("/POS")

    for points_positions in points_positions:

        if program["robot_id"] == points_positions["robot_id"] and program["program_id"] == points_positions["program_id"]:
            if points_positions["Positions Data"]:
                for line in points_positions["Positions Data"]:
                    lines.append(line)

    lines.append("/END")

    output = "\n".join(lines)
    return output