import re


#----- Program data patterns -----
program_name_pattern = re.compile(r"^/PROG\s*(.+)$") #Example: /PROG  FOLGE056
program_comment_pattern = re.compile(r"^COMMENT\s*=\s*\"(.{1,16})\";$") #Example: COMMENT		= "VW371 Jetta";
program_filename_pattern = re.compile(r"^FILE_NAME\s*=\s*(.+);$") #Example: FILE_NAME	= FOLGE051;

#----- Point data patterns -----
#Group 1: Optional line number, Group 2: Point number
point_pattern = re.compile(r"^\s*(\d*)?\s*:\s*(?:\/\/)?\s*[JLC]\s+P\[(\d+)(?:\:.*)?\].*;$") # Example:   11:J P[2] 100% CNT0 ACC100 TB    .10sec,P-SPS    ;

point_end_pattern = re.compile(r"^\s*------\s*;$") #------ ;


#----- Point position patterns -----
#Group 1: Point number
point_coordinates_pattern = re.compile(r"^P\[(\d+)\]\s*=\s*\{$") # Example:   P[1]{
#Group 1: Group number
point_group_pattern = re.compile(r"^\s*GP(\d+):$") # Example:   GP1:
point_end_coordinates_pattern = re.compile(r"^\};$") #  };

# Coordinates patterns
#Group 1: UF number, Group 2: UT number, Group 3: First config letter, Group 4: Second config letter, Group 5: Third config letter, Group 6: Config  value 1, Group 7: Config value 2, Group 8: Config value 3
point_config_pattern = re.compile(r"^\s*UF\s*:\s*(\d+),\s*UT\s*:\s*(\d+),\s*CONFIG\s*:\s*'([A-Z])\s*([A-Z])\s*([A-Z]),\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)',\s*$") #Example: 	UF : 0, UT : 3,		CONFIG : 'F U T, 0, 0, 0',
#Group 1: X value, Group 2: Y value, Group 3: Z value
point_position_values_pattern = re.compile(r"^\s*X\s*=\s*(-?\d+\.\d+)\s*mm,\s*Y\s*=\s*(-?\d+\.\d+)\s*mm,\s*Z\s*=\s*(-?\d+\.\d+)\s*mm,\s*$") # Example:   X =  1605.421  mm,	Y =  -122.813  mm,	Z =  1722.528  mm,
#Group 1: W value, Group 2: P value, Group 3: R value
point_orientation_values_pattern = re.compile(r"^\s*W\s*=\s*(-?\d+\.\d+)\s*deg,\s*P\s*=\s*(-?\d+\.\d+)\s*deg,\s*R\s*=\s*(-?\d+\.\d+)\s*deg\s*$") # Example:   W =   159.043 deg,	P =   -43.966 deg,	R =     1.730 deg

# Axis positions patterns
#Group 1: UF number, Group 2: UT number
point_axis_frames_pattern = re.compile(r"^\s*UF\s*:\s*(\d+),\s*UT\s*:\s*(\d+),\s*$") #Example: 	UF : 0, UT : 1,
#Group 1: Axis values J1, Group 2: Axis values J2, Group 3: Axis values J3
point_axis123_values_pattern = re.compile(r"^\s*J1\s*=\s*(-?\d*\.\d+)\s*deg\s*,\s*J2\s*=\s*(-?\d*\.\d+)\s*deg\s*,\s*J3\s*=\s*(-?\d*\.\d+)\s*deg\s*,$") #Example: 	J1=   -25.000 deg,	J2=   -35.000 deg,	J3=      .000 deg,
#Group 1: Axis values J4, Group 2: Axis values J5, Group 3: Axis values J6
point_axis456_values_pattern = re.compile(r"^\s*J4\s*=\s*(-?\d*\.\d+)\s*deg\s*,\s*J5\s*=\s*(-?\d*\.\d+)\s*deg\s*,\s*J6\s*=\s*(-?\d*\.\d+)\s*deg\s*$") #Example: 	J4=   -25.000 deg,	J5=   -35.000 deg,	J6=      .000 deg
#Group 1: Axis value J1
point_external_axis_pattern = re.compile(r"^\s*J1\s*=\s*(-?\d+\.\d+)\s*mm\s*$") #Example:  	J1=   219.000  mm


#Group 1: Optional line number, Group 2: Payload number
payload_pattern = re.compile(r"^\s*(\d*)?\s*:\s*(?:\/\/)?\s*PAYLOAD\[(\d+)\]\s*;$") # Example:   7:  PAYLOAD[1] ;

#Group 1: Optional line number, Group 2: Uframe number
uframe_pattern = re.compile(r"^\s*(\d*)?\s*:\s*(?:\/\/)?\s*UFRAME_NUM\s*=\s*(\d+)\s*;$") # Example:   8:  UFRAME_NUM=0 ;

#Group 1: Optional line number, Group 2: Utool number
utool_pattern = re.compile(r"^\s*(\d*)?\s*:\s*(?:\/\/)?\s*UTOOL_NUM\s*=\s*(\d+)\s*;$") # Example:   9:  UTOOL_NUM=3 ;


