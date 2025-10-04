

owner = "MNEDITOR"
robot_id = "VW371 Jetta"

def correct_folge(program):

    program_attributes = correct_attributes(program)



    return program_attributes

def correct_attributes(program, robot):
    if robot["Gripper 1"]:
        if program["program_id"] in ["UP051"]:
            comment = "Tomar" , program["Station"] , "371"
        if program["program_id"] in ["UP053"]:
            comment = "Dejar" , program["Station"] , "371"
        if program["program_id"] in ["UP112"]:
            comment = "Mantenimiento G1"
        if program["program_id"] in ["UP201"]:
            comment = "Cambio Herra. G1"
        if program["program_id"] in ["UP206"]:
            comment = "Chequeo TCP G1"
    
    if robot["Gripper 2"]:
        if program["program_id"] in ["UP051"]:
            comment = "Tomar" , program["Station"] , "371"
        if program["program_id"] in ["UP053"]:
            comment = "Dejar" , program["Station"] , "371"
        if program["program_id"] in ["UP113"]:
            comment = "Mantenimiento G2"
        if program["program_id"] in ["UP201"]:
            comment = "Cambio Herra. G2"
        if program["program_id"] in ["UP206"]:
            comment = "Chequeo TCP G2"

    if program["program_id"] == "FOLGE056":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "FOLGE056",
        "Program File Name": "FOLGE056",
        "Program Name": "FOLGE056",
        "OWNER": owner,
        "COMMENT": "VW371 Jetta",
        "FILE_NAME": "FOLGE056",
        }

    elif program["program_id"] == "FOLGE058":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "FOLGE058",
        "Program File Name": "FOLGE058",
        "Program Name": "FOLGE058",
        "OWNER": owner,
        "COMMENT": "VW371 Take In",
        "FILE_NAME": "FOLGE058",
        }

    elif program["program_id"] == "MAKRO050":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "MAKRO050",
        "Program File Name": "MAKRO050",
        "Program Name": "MAKRO050",
        "OWNER": owner,
        "COMMENT": "Init. Merker",
        "FILE_NAME": "MAKRO050",
        }

    elif program["program_id"] == "MAKRO051":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "MAKRO051",
        "Program File Name": "MAKRO051",
        "Program Name": "MAKRO051",
        "OWNER": owner,
        "COMMENT": "Init. Merker G1",
        "FILE_NAME": "MAKRO051",
        }

    elif program["program_id"] == "MAKRO052":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "MAKRO052",
        "Program File Name": "MAKRO052",
        "Program Name": "MAKRO052",
        "OWNER": owner,
        "COMMENT": "Init. Merker G2",
        "FILE_NAME": "MAKRO052",
        }

    elif program["program_id"] == "MAKRO057":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "MAKRO057",
        "Program File Name": "MAKRO057",
        "Program Name": "MAKRO057",
        "OWNER": owner,
        "COMMENT": "Init. Flag",
        "FILE_NAME": "MAKRO057",
        }

    elif program["program_id"] == "MAKRO058":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "MAKRO058",
        "Program File Name": "MAKRO058",
        "Program Name": "MAKRO058",
        "OWNER": owner,
        "COMMENT": "DK-Init",
        "FILE_NAME": "MAKRO058",
        }

    elif program["program_id"] == "MAKRO059":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "MAKRO059",
        "Program File Name": "MAKRO059",
        "Program Name": "MAKRO059",
        "OWNER": owner,
        "COMMENT": "Profinet Altern",
        "FILE_NAME": "MAKRO059",
        }

    elif program["program_id"] == "UP081":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "UP081",
        "Program File Name": "UP081",
        "Program Name": "UP081",
        "OWNER": owner,
        "COMMENT": "Deja G2 Toma G1",
        "FILE_NAME": "UP081",
        }

    elif program["program_id"] == "UP082":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "UP082",
        "Program File Name": "UP082",
        "Program Name": "UP082",
        "OWNER": owner,
        "COMMENT": "Deja G1 Toma G2",
        "FILE_NAME": "UP082",
        }

    elif program["program_id"] == "UP112":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "UP112",
        "Program File Name": "UP112",
        "Program Name": "UP112",
        "OWNER": owner,
        "COMMENT": comment,
        "FILE_NAME": "UP112",
        }

    elif program["program_id"] == "UP113":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "UP113",
        "Program File Name": "UP113",
        "Program Name": "UP113",
        "OWNER": owner,
        "COMMENT": comment,
        "FILE_NAME": "UP113",
        }

    elif program["program_id"] == "UP114":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "UP114",
        "Program File Name": "UP114",
        "Program Name": "UP114",
        "OWNER": owner,
        "COMMENT": comment,
        "FILE_NAME": "UP114",
        }

    elif program["program_id"] == "UP201":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "UP201",
        "Program File Name": "UP201",
        "Program Name": "UP201",
        "OWNER": owner,
        "COMMENT": comment,
        "FILE_NAME": "UP201",
        }

    elif program["program_id"] == "UP202":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "UP202",
        "Program File Name": "UP202",
        "Program Name": "UP202",
        "OWNER": owner,
        "COMMENT": comment,
        "FILE_NAME": "UP202",
        }

    elif program["program_id"] == "UP206":
        program_attributes = {
        "robot_id": robot_id,
        "program_id": "UP206",
        "Program File Name": "UP206",
        "Program Name": "UP206",
        "OWNER": owner,
        "COMMENT": comment,
        "FILE_NAME": "UP206",
        }
    else:

        program_attributes = None

    return program_attributes
