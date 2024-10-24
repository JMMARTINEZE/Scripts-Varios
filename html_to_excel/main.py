import os
import subprocess

def main():
    # Ask for the original HTML file
    html_filepath = input("Enter the path to the original HTML file: ")

    # Call titles_html_to_excel.py and pass the HTML file as an argument
    subprocess.run(["python", "./html_to_excel/titles_html_to_excel.py", html_filepath])

    # Call fields_html_to_excel.py and pass the HTML file as an argument
    subprocess.run(["python", "./html_to_excel/fields_html_to_excel.py", html_filepath])

    # Call combine_csv.py
    subprocess.run(["python", "./html_to_excel/combine_csv.py"])

    # Call translator.py
    subprocess.run(["python", "./html_to_excel/translator.py"])

if __name__ == "__main__":
    main()