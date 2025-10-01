import os

def create_file(path, lines):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Create the file and write lines if provided
    with open(path, 'w') as f:
        if lines:
            for line in lines:
                f.write(line + '\n')

def write_program(path, robots, programs):

    for robot in robots:
        new_robot_dir = os.path.join(path, robot["Robot Full Name"])
        os.makedirs(new_robot_dir, exist_ok=True)

        for program in programs:
            if robot["robot_id"] == program["robot_id"]:
                lines = []
                print("Writing program:", program["Program Name"], "for robot:", robot["Robot Full Name"])

                lines.append(write_attributes_section(program))
                if program["Applications exists"]:
                    lines.append(write_applications_section(program))

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
    print(program["Applications"])
    if program["Applications"]:
        for app_line in program["Applications"]:
            lines.append(app_line)

    output = "\n".join(lines)
    return output

def write_main_section(program):

    lines = []
    lines.append("/MN")
    # Add main section content here if needed

    output = "\n".join(lines)
    return output