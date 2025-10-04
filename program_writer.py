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
    lines.append("OWNER      = " + program["OWNER"] + ";")
    lines.append("COMMENT    = \"" + program["COMMENT"] + "\";")
    lines.append("PROG_SIZE  = " + str(program["PROG_SIZE"]) + ";")
    lines.append("CREATE     = DATE " + program["CREATE"][:9] + "  TIME " + program["CREATE"][9:] + ";")
    lines.append("MODIFIED   = DATE " + program["MODIFIED"][:9] + "  TIME " + program["MODIFIED"][9:] + ";")
    lines.append("FILE_NAME  = " + program["FILE_NAME"] + ";")
    lines.append("VERSION    = " + str(program["VERSION"]) + ";")
    lines.append("LINE_COUNT = " + str(program["LINE_COUNT"]) + ";")
    lines.append("MEMORY_SIZE= " + str(program["MEMORY_SIZE"]) + ";")
    lines.append("PROTECT    = " + program["PROTECT"] + ";")
    if program["STORAGE"]:
        lines.append("STORAGE    = " + program["STORAGE"] + ";")
    lines.append("TCD:  STACK_SIZE = " + str(program["STACK_SIZE"]) + ",")
    lines.append("      TASK_PRIORITY = " + str(program["TASK_PRIORITY"]) + ",")
    lines.append("      TIME_SLICE = " + str(program["TIME_SLICE"]) + ",")
    lines.append("      BUSY_LAMP_OFF = " + str(program["BUSY_LAMP_OFF"]) + ",")
    lines.append("      ABORT_REQUEST = " + str(program["ABORT_REQUEST"]) + ",")
    lines.append("      PAUSE_REQUEST = " + str(program["PAUSE_REQUEST"]) + ";")
    lines.append("DEFAULT_GROUP = " + program["DEFAULT_GROUP"] + ";")
    lines.append("CONTROL_CODE  = " + program["CONTROL_CODE"] + ";")
    
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
        #print('robot_id:', point["robot_id"])
        #print('program_id:', point["program_id"])
        #print('point_id:', point["point_id"])
        #print('Comments:', point["Comments"])
        #print('Logic:', point["Logic"])
        #time.sleep(5)

        if point["Comments"]:
            for comment in point["Comments"]:
                lines.append(comment)
                #print("Adding comment:", comment)

        if point["Logic"]:
            for logic in point["Logic"]:
                lines.append(logic)
                #print("Adding logic:", logic)

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