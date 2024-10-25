import os
import subprocess

def main():
    """
    Main function to process an HTML file and generate a translated Word document.

    This function performs the following steps:
    1. Prompts the user to enter the path to the original HTML file.
    2. Executes titles_html_to_excel.py to extract titles from the HTML file.
    3. Executes fields_html_to_excel.py to extract specified fields from the HTML file using a configuration file.
    4. Calls combine_csv.py to combine the extracted data into a single CSV file.
    5. Executes word_processor.py to generate a translated Word document based on the combined CSV data.
    """
    # Ask for html file
    html_filepath = input("Enter the path to the original HTML file: ")

    # Call titles_html_to_excel.py and pass the HTML file as an argument
    subprocess.run(["python", "./html_to_excel/titles_html_to_excel.py", html_filepath])

    # Call fields_html_to_excel.py and pass the HTML file and configuration file as arguments
    config_filepath = "html_to_excel/fields_config.json"
    subprocess.run(["python", "./html_to_excel/fields_html_to_excel.py", html_filepath, config_filepath])

    # Call combine_csv.py
    subprocess.run(["python", "./html_to_excel/combine_csv.py"])

    # subprocess.run(["python", "./html_to_excel/translator.py"])
    subprocess.run(["python", "./html_to_excel/word_processor.py"])

if __name__ == "__main__":
    main()