import os
import pandas as pd
import patterns
import VASS5_main as vassm

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
            "program_id": program_data["Program Name"],
            "Program File Name": program_name,
            "Program Name": program_data["Program Name"],
            "OWNER": program_data["OWNER"],
            "COMMENT": program_data["COMMENT"],
            "PROG_SIZE": program_data["PROG_SIZE"],
            "CREATE": program_data["CREATE"],
            "MODIFIED": program_data["MODIFIED"],
            "FILE_NAME": program_data["FILE_NAME"],
            "VERSION": program_data["VERSION"],
            "LINE_COUNT": program_data["LINE_COUNT"],
            "MEMORY_SIZE": program_data["MEMORY_SIZE"],
            "PROTECT": program_data["PROTECT"],
            "STORAGE": program_data["STORAGE"],
            "STACK_SIZE": program_data["STACK_SIZE"],
            "TASK_PRIORITY": program_data["TASK_PRIORITY"],
            "TIME_SLICE": program_data["TIME_SLICE"],
            "BUSY_LAMP_OFF": program_data["BUSY_LAMP_OFF"],
            "ABORT_REQUEST": program_data["ABORT_REQUEST"],
            "PAUSE_REQUEST": program_data["PAUSE_REQUEST"],
            "DEFAULT_GROUP": program_data["DEFAULT_GROUP"],
            "CONTROL_CODE": program_data["CONTROL_CODE"],
            }

            all_programs_data.append(row_data)

    return all_programs_data

def get_program_main_data(program_lines):
    program_data = {
        "Program Name": None,
        "OWNER": None,
        "COMMENT": None,
        "PROG_SIZE": None,
        "CREATE": None,
        "MODIFIED": None,
        "FILE_NAME": None,
        "VERSION": None,
        "LINE_COUNT": None,
        "MEMORY_SIZE": None,
        "PROTECT": None,
        "STORAGE": None,
        "STACK_SIZE": None,
        "TASK_PRIORITY": None,
        "TIME_SLICE": None,
        "BUSY_LAMP_OFF": None,
        "ABORT_REQUEST": None,
        "PAUSE_REQUEST": None,
        "DEFAULT_GROUP": None,
        "CONTROL_CODE": None,
    }

    for line in program_lines:
        prog_name_match = patterns.program_name_pattern.match(line)
        if prog_name_match:
            program_data["Program Name"] = prog_name_match.group(1).strip()
            continue

        program_owner_pattern_match = patterns.program_owner_pattern.match(line)
        if program_owner_pattern_match:
            program_data["OWNER"] = program_owner_pattern_match.group(1).strip()
            continue

        create_match = patterns.program_create_pattern.match(line)
        if create_match:
            program_data["CREATE"] = create_match.group(1).strip() + " " + create_match.group(2).strip()
            continue
        
        comment_match = patterns.program_comment_pattern.match(line)
        if comment_match:
            program_data["COMMENT"] = comment_match.group(1).strip()
            continue

        prog_size_match = patterns.program_progsize_pattern.match(line)
        if prog_size_match:
            program_data["PROG_SIZE"] = int(prog_size_match.group(1).strip())
            continue
            
        modified_match = patterns.program_modified_pattern.match(line)
        if modified_match:
            program_data["MODIFIED"] = modified_match.group(1).strip() + " " + modified_match.group(2).strip()
            continue

        file_name_match = patterns.program_filename_pattern.match(line)
        if file_name_match:
            program_data["FILE_NAME"] = file_name_match.group(1).strip()
            continue

        version_match = patterns.program_version_pattern.match(line)
        if version_match:
            program_data["VERSION"] = int(version_match.group(1).strip())
            continue

        line_count_match = patterns.program_line_count_pattern.match(line)
        if line_count_match:
            program_data["LINE_COUNT"] = int(line_count_match.group(1).strip())
            continue

        memory_size_match = patterns.program_memory_size_pattern.match(line)
        if memory_size_match:
            program_data["MEMORY_SIZE"] = int(memory_size_match.group(1).strip())
            continue

        protect_match = patterns.program_protect_pattern.match(line)
        if protect_match:
            program_data["PROTECT"] = protect_match.group(1).strip()
            continue

        storage_match = patterns.program_storage_pattern.match(line)
        if storage_match:
            program_data["STORAGE"] = storage_match.group(1).strip()
            continue

        stack_size_match = patterns.program_stack_size_pattern.match(line)
        if stack_size_match:
            program_data["STACK_SIZE"] = int(stack_size_match.group(1).strip())
            continue

        task_priority_match = patterns.program_task_priority_pattern.match(line)
        if task_priority_match:
            program_data["TASK_PRIORITY"] = int(task_priority_match.group(1).strip())
            continue

        time_slice_match = patterns.program_time_slice_pattern.match(line)
        if time_slice_match:
            program_data["TIME_SLICE"] = int(time_slice_match.group(1).strip())
            continue

        busy_lamp_off_match = patterns.program_busy_lamp_off_pattern.match(line)
        if busy_lamp_off_match:
            program_data["BUSY_LAMP_OFF"] = int(busy_lamp_off_match.group(1).strip())
            continue

        abort_request_match = patterns.program_abort_request_pattern.match(line)
        if abort_request_match:
            program_data["ABORT_REQUEST"] = int(abort_request_match.group(1).strip())
            continue

        pause_request_match = patterns.program_pause_request_pattern.match(line)
        if pause_request_match:
            program_data["PAUSE_REQUEST"] = int(pause_request_match.group(1).strip())
            continue

        default_group_match = patterns.program_default_group_pattern.match(line)
        if default_group_match:
            program_data["DEFAULT_GROUP"] = default_group_match.group(1).strip()
            continue

        control_code_match = patterns.program_control_code_pattern.match(line)
        if control_code_match:
            program_data["CONTROL_CODE"] = control_code_match.group(1).strip()
            continue

    return program_data

def create_points_parameters_list(robots, programs):
    all_points_parameters_data = []

    robots_by_id = {robot["robot_id"]: robot for robot in robots}
    for program in programs:            
            robot_id = program["robot_id"]
            
            current_robot = robots_by_id.get(robot_id)

            program_lines = read_program_file(os.path.join(current_robot["Saved Path"], program["Program File Name"]))
            row_data = {}
            for line in program_lines:
                if patterns.point_pattern.match(line):
                    row_data = {
                        "robot_id": program["robot_id"],
                        "program_id": program["program_id"],
                        "point_id": patterns.point_pattern.match(line).group(3),
                        "Line Number": patterns.point_pattern.match(line).group(1) if patterns.point_pattern.match(line).group(1) else None,
                        "Movement Type": patterns.point_pattern.match(line).group(2),
                        "Speed Value": patterns.point_pattern.match(line).group(4),
                        "Speed Type": patterns.point_pattern.match(line).group(5),
                        "Continuity Type": patterns.point_pattern.match(line).group(6),
                        "Continuity Value": patterns.point_pattern.match(line).group(7),
                        "ACC Type": patterns.point_pattern.match(line).group(8) if patterns.point_pattern.match(line).group(8) else None,
                        "ACC Value": patterns.point_pattern.match(line).group(9) if patterns.point_pattern.match(line).group(9) else None,
                        "TB/DB Type": patterns.point_pattern.match(line).group(10) if patterns.point_pattern.match(line).group(10) else None,
                        "TB/DB Value": patterns.point_pattern.match(line).group(11) if patterns.point_pattern.match(line).group(11) else None,
                        "TB/DB Unit": patterns.point_pattern.match(line).group(12) if patterns.point_pattern.match(line).group(12) else None,
                        "Additional Parameters": patterns.point_pattern.match(line).group(13) + patterns.point_pattern.match(line).group(14) if patterns.point_pattern.match(line).group(13) else None
                    }
                    all_points_parameters_data.append(row_data)

    return all_points_parameters_data

def create_points_logic_list(robots, programs):
    all_points_logic_data = []

    robots_by_id = {robot["robot_id"]: robot for robot in robots}
    for program in programs:            
            robot_id = program["robot_id"]
            point_id = 1
            
            current_robot = robots_by_id.get(robot_id)

            program_lines = read_program_file(os.path.join(current_robot["Saved Path"], program["Program File Name"]))
            row_data = {}
            read_logic = False
            read_comments = True
            comments_lines = []
            read_lines = False
            
            for line in program_lines:
                if line != "/MN" and not read_lines:
                    continue
                elif line == "/POS":
                    break
                else:
                    read_lines = True

                if read_lines:
                    
                    if read_comments and not patterns.point_pattern.match(line) and line != "/MN":
                        comments_lines.append(line)
                        continue

                    if patterns.point_pattern.match(line):
                        point_id = patterns.point_pattern.match(line).group(3)
                        logic_lines = []
                        read_logic = True
                        read_comments = False
                        continue

                    if patterns.point_end_pattern.match(line):
                        read_logic = False
                        read_comments = True
                        row_data = {
                            "robot_id": program["robot_id"],
                            "program_id": program["program_id"],
                            "point_id": point_id,
                            "Logic": logic_lines,
                            "Comments": comments_lines
                        }
                        all_points_logic_data.append(row_data)
                        comments_lines = []
                        continue

                    if read_logic:
                        logic_lines.append(line)

                    
    return all_points_logic_data
