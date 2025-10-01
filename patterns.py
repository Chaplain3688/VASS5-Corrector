import re

#Group 1: Line (5 alphanumeric), Group 2: ARG (1 alphanumeric), Group 3: SK (1 alphanumeric), Group 4: Robot number (4 digits), Group 5: Robot ID (2 digits)
robot_name_pattern = re.compile(r'K([A-Za-z0-9]{5})([A-Za-z0-9]{1})([A-Za-z0-9]{1})(\d{4})R(\d{2})')

#----- Program data patterns -----
program_name_pattern = re.compile(r"^/PROG\s*(\w+)$") #Example: /PROG  FOLGE056
program_owner_pattern = re.compile(r"^OWNER\s*=\s*(.*);$") #Example: OWNER		= engenhar;
program_comment_pattern = re.compile(r"^COMMENT\s*=\s*\"(.{0,16})\";$") #Example: COMMENT		= "VW371 Jetta";
program_progsize_pattern = re.compile(r"^PROG_SIZE\s*=\s*(\d+);$") #Example: PROG_SIZE	= 1024;
program_create_pattern = re.compile(r"^CREATE\s*=\s*DATE\s*(\d{2}-\d{2}-\d{2})\s*TIME\s*(\d{2}:\d{2}:\d{2});$") #Example: CREATE		= DATE 04-04-27  TIME 08:38:34;
program_modified_pattern = re.compile(r"^MODIFIED\s*=\s*DATE\s*(\d{2}-\d{2}-\d{2})\s*TIME\s*(\d{2}:\d{2}:\d{2});$") #Example: MODIFIED	= DATE 25-09-27  TIME 14:24:46;
program_filename_pattern = re.compile(r"^FILE_NAME\s*=\s*(\w*);$") #Example: FILE_NAME	= FOLGE051;
program_version_pattern = re.compile(r"^VERSION\s*=\s*(\d+);$") #Example:   VERSION		= 0;
program_line_count_pattern = re.compile(r"^LINE_COUNT\s*=\s*(\d+);$") #Example:   LINE_COUNT	= 40;
program_memory_size_pattern = re.compile(r"^MEMORY_SIZE\s*=\s*(\d+);$") #Example:   MEMORY_SIZE	= 8326;
program_protect_pattern = re.compile(r"^PROTECT\s*=\s*(.+);$") #Example:   PROTECT		= READ_WRITE;
program_storage_pattern = re.compile(r"^STORAGE\s*=\s*(.+);$") #Example:   STORAGE		= SHADOW;
program_stack_size_pattern = re.compile(r"^TCD:\s*STACK_SIZE\s*=\s*(\d+),$") #Example:   TCD:  STACK_SIZE	= 500,
program_task_priority_pattern = re.compile(r"^\s*TASK_PRIORITY\s*=\s*(\d+),$") #Example:   TASK_PRIORITY	= 50,
program_time_slice_pattern = re.compile(r"^\s*TIME_SLICE\s*=\s*(\d+),$") #Example:   TIME_SLICE	= 0,
program_busy_lamp_off_pattern = re.compile(r"^\s*BUSY_LAMP_OFF\s*=\s*(\d+),$") #Example:   BUSY_LAMP_OFF	= 0,
program_abort_request_pattern = re.compile(r"^\s*ABORT_REQUEST\s*=\s*(\d+),$") #Example:   ABORT_REQUEST	= 0,
program_pause_request_pattern = re.compile(r"^\s*PAUSE_REQUEST\s*=\s*(\d+);$") #Example:   PAUSE_REQUEST	= 0;
program_default_group_pattern = re.compile(r"^DEFAULT_GROUP\s*=\s*(.+);$") #Example:   DEFAULT_GROUP	= 1,1,1,1,*;
program_control_code_pattern = re.compile(r"^CONTROL_CODE\s*=\s*(.+);$") #Example:   CONTROL_CODE	= 00000000 00000000;

#----- Program sections patterns -----
program_attributes_pattern = re.compile(r"^/ATTR$") #Example: /ATTR
program_applications_pattern = re.compile(r"^/APPL$") #Example: /APPL
program_main_pattern = re.compile(r"^/MN$")#Example: /MN
program_position_pattern = re.compile(r"^/POS$")#Example: /POS
program_end_pattern = re.compile(r"^/END$")#Example: /END

#----- Point data patterns -----
#Group 1: Optional line number, Group 2: Movement type (J, L, C), Group 3: Point number, Group 4: Speed value, Group 5: Speed Type, Group 6: Continuity type (CNT or CD), Group 7: Continuity value (0-999), Group 8: ACC keyword, Group 9: ACC value (0-999), Group 10: TB or DB keyword, Group 11: TB/DB value (float with 2 decimals), Group 12: TB unit (sec or mm), Group 13: Comma if there are additional parameters, Group 14: Additional parameters
point_pattern = re.compile(r"^\s*(\d*)?\s*:\s*(?:\/\/)?\s*([JLC])\s+P\[(\d+)(?:\:.*)?\]\s*(\d{1,5})(%|mm\/sec)\s*(CNT|CD)(\d{1,3})\s*(ACC)?(\d{1,3})?\s*(TB|DB)\s*(\d{0,3}\.\d{1,2})(sec|mm)(,)?(.*)?;$") # Example:   11:J P[2] 100% CNT0 ACC100 TB    .10sec,P-SPS    ;

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