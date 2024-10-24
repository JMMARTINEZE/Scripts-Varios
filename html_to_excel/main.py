import os
import subprocess
import sys
import pandas as pd

def run_titles_script():
    script_path = os.path.join(os.path.dirname(__file__), 'titles_html_to_excel.py')
    subprocess.run([sys.executable, script_path])

def run_fields_script():
    script_path = os.path.join(os.path.dirname(__file__), 'fields_html_to_excel.py')
    subprocess.run([sys.executable, script_path])

def combine_output():
    try:
        titles_df = pd.read_excel('html_to_excel/titles.xlsx')
        fields_df = pd.read_excel('html_to_excel/fields.xlsx')

        combined_df = pd.concat([titles_df, fields_df], axis=1)

        combined_df.to_excel('html_to_excel/combined_output.xlsx', index=False)
        combined_df.to_csv('html_to_excel/combined_output.csv', index=False)

        print("Output files combined successfully.")

        # Delete old files
        try:
            os.remove('html_to_excel/titles.xlsx')
            os.remove('html_to_excel/fields.xlsx')

            print("Old files deleted successfully.")

        except OSError as e:
            print(f"Error deleting old files: {e}")
    except FileNotFoundError:
        print("Error: One or more input files not found.")

def main():
    run_titles_script()
    run_fields_script()
    combine_output()

if __name__ == '__main__':
    main()