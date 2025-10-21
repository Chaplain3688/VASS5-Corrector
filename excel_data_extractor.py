import pandas as pd
import os
import xlwings as xw  # New import for controlling Excel
import re # New import for regular expressions
import VASS5_main as main

def run_excel_macro(filepath, macro_name):
    """
    Opens an Excel file, runs a specified macro, and saves the file.
    
    REQUIREMENTS:
    - Must be run on a Windows machine with Microsoft Excel installed.
    - The 'xlwings' library must be installed (`pip install xlwings`).
    - The Excel file must be a macro-enabled file (e.g., .xlsm).
    """
    if not macro_name:
        print("\nNo macro name provided. Skipping macro execution.")
        return True

    print(f"\nAttempting to run macro '{macro_name}' in '{filepath}'...")

    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' does not exist.")
        return False
    try:
        # Start an Excel app in the background (visible=False)
        with xw.App(visible=False) as app:
            # Open the workbook
            wb = app.books.open(filepath)
            
            # Get the macro object. The name might need to be prefixed with the module
            # name, e.g., 'Module1.YourMacroName'
            macro_to_run = wb.macro(macro_name)
            
            # Run the macro
            macro_to_run()
            
            # Save the workbook after the macro has run
            wb.save()
            print("Macro executed and workbook saved successfully.")
            
            # Close the workbook
            wb.close()
            
    except Exception as e:
        print(f"--- ERROR RUNNING MACRO ---")
        print(f"Error: {e}")
        print("Please ensure:")
        print("  - You are running on Windows with Microsoft Excel installed.")
        print(f"  - The file '{filepath}' is a macro-enabled file (e.g., .xlsm).")
        print(f"  - The macro name '{macro_name}' is correct (e.g., 'Module1.YourMacroName').")
        return False
    return True


def extract_data_from_excel(excel_file_path):
    """
    Reads all sheets from an Excel file that match a robot name pattern,
    extracts multiple specific ranges into DataFrames, and returns
    them in a nested dictionary.
    """
    # This will be our main storage for all the data.
    # Structure: { 'sheet_name': {'data_frame_name': DataFrame, ...}, ... }
    all_data = {}

    try:
        # Using pd.ExcelFile is efficient as it opens the file once.
        xls = pd.ExcelFile(excel_file_path)
        sheet_names = xls.sheet_names
        print(f"\nFound sheets: {sheet_names}")
    except FileNotFoundError:
        print(f"Error: The file '{excel_file_path}' was not found.")
        return None

    # This regex pattern will match strings that start and end with digits, 
    # with an 'R' in the middle (e.g., '512580R01').
    robot_sheet_pattern = re.compile(r'^\d+R\d+$')

    # Loop through all the sheets found in the file
    for sheet_name in sheet_names:
        # Only process sheets that match the robot name pattern
        if not robot_sheet_pattern.match(sheet_name):
            print(f"\nSkipping sheet: '{sheet_name}' (does not match robot name pattern)")
            continue

        print(f"\nProcessing sheet: '{sheet_name}'...")
        
        # Initialize the inner dictionary for the current sheet
        all_data[sheet_name] = {}

        # --- Extract each data frame based on the specified ranges ---
        # Note: header=None is used because we are just grabbing blocks of data.
        # If your first row in the selection IS a header, you can remove this.

        # Frame 1: Station Signals (Rows 7-30, Columns E-L)
        df_station_signals = pd.read_excel(
            xls,
            sheet_name=sheet_name,
            header=None,
            skiprows=6,
            nrows=24,
            usecols='E:L'
        )
        all_data[sheet_name]['station_signals'] = df_station_signals
        print(f"  - Extracted 'station_signals' with shape: {df_station_signals.shape}")

        # Frame 2: Folges (A7:B14)
        df_folges = pd.read_excel(
            xls,
            sheet_name=sheet_name,
            header=None,
            skiprows=6,
            nrows=8, # 14 - 7 + 1 = 8
            usecols='A:B'
        )
        all_data[sheet_name]['folges'] = df_folges
        print(f"  - Extracted 'folges' with shape: {df_folges.shape}")


        # Frame 3: Fertigmeldungen (A20:B33)
        df_fertigmeldungen = pd.read_excel(
            xls,
            sheet_name=sheet_name,
            header=None,
            skiprows=19,
            nrows=14, # 33 - 20 + 1 = 14
            usecols='A:B'
        )
        all_data[sheet_name]['fertigmeldungen'] = df_fertigmeldungen
        print(f"  - Extracted 'fertigmeldungen' with shape: {df_fertigmeldungen.shape}")

        # Frame 4: Machine Safety (N25:O39)
        df_machine_safety = pd.read_excel(
            xls,
            sheet_name=sheet_name,
            header=None,
            skiprows=24,
            nrows=15, # 39 - 25 + 1 = 15
            usecols='N:O'
        )
        all_data[sheet_name]['machine_safety'] = df_machine_safety
        print(f"  - Extracted 'machine_safety' with shape: {df_machine_safety.shape}")

        # Frame 5: Collision Zones Signals (N6:AE22)
        df_collision_zones = pd.read_excel(
            xls,
            sheet_name=sheet_name,
            header=None,
            skiprows=5,
            nrows=17, # 22 - 6 + 1 = 17
            usecols='N:AE'
        )
        all_data[sheet_name]['collision_zones_signals'] = df_collision_zones
        print(f"  - Extracted 'collision_zones_signals' with shape: {df_collision_zones.shape}")

    return all_data


# --- Main script execution ---
if __name__ == "__main__":
    # --- Step 1: Set your file path and macro name ---
    # !! IMPORTANT !!
    # !! CHANGE THE MACRO NAME to your actual macro.
    # The file path has been set to the one you provided.
    excel_file_to_read = r'C:\Users\inzun\OneDrive\Persona Fisica\Proyectos\Puebla VW\VW371 Jetta\05 Tasks\2025 CW40 USTW5\Verriegelungmatrix_20251014\ARG5\VW336-3_VW371_USTW_ARG5_Verriegelunguebersicht_20251014.xlsm'
    robot_json_file = os.path.join(os.path.dirname(excel_file_to_read), "extracted_data.json")
    robot_excel_file = os.path.join(os.path.dirname(excel_file_to_read), "extracted_data.xlsx")

    # Example: 'Module1.UpdateAllData'. Leave as "" if you have no macro.
    macro_to_run = "cmd_refresh" 

    # --- Step 2: Run the macro (if specified) ---
    macro_success = run_excel_macro(excel_file_to_read, macro_to_run)

    # --- Step 3: Run the extraction function if macro was successful ---
    if macro_success:
        extracted_data = extract_data_from_excel(excel_file_to_read)

        # --- Step 4: Example of how to access and use the stored DataFrames ---
        if extracted_data:
            print("\n\n--- Data Extraction Complete! ---")
            print(f"Processed sheets: {list(extracted_data.keys())}")

            # Example: Access the 'folges' DataFrame from the first processed sheet
            try:
                # We'll try to access the first processed sheet as an example
                first_sheet_name = list(extracted_data.keys())[0]
                frame_to_access = 'folges'
                
                print(f"\nExample: Displaying the '{frame_to_access}' DataFrame from the '{first_sheet_name}' sheet:")
                
                specific_df = extracted_data[first_sheet_name][frame_to_access]
                print(specific_df.head())
            
            except (KeyError, IndexError):
                print(f"\nCould not access the example data.")
                print("Please check if any sheets matched the robot name pattern and were processed.")

    print(f"\n\n")

    for sheet_name, frames in extracted_data.items():
        for frame in frames:
            print(f"Processing frame for sheet: {sheet_name}, frame: {frame}")
        #main.create_dfs(frames, robot_excel_file, robot_json_file)

