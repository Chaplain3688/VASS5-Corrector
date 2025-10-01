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

    robot_id = robots[0]["robot_id"]
    for program in programs:
        if program["robot_id"] == robot_id:
            lines = []
            lines.append(write_attributes(program))
            create_file(os.path.join(path, program["Program Name"] + ".ls"), lines)

def write_attributes(program):

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