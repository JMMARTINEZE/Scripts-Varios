import os
import pandas as pd

def combine_output():
    """
    Combines the titles and fields CSV files into a single output file, sorts the
    data by RiskRating, and deletes the old files.

    This function assumes that the titles and fields CSV files have been generated
    by the titles_html_to_csv.py and fields_html_to_csv.py scripts, and are
    named 'titles.csv' and 'fields.csv' respectively.

    The combined output file is named 'combined_output.csv' and is saved in the
    'html_to_excel' folder.

    If an error occurs while deleting the old files, an OSError is raised.

    If one or more input files are not found, a FileNotFoundError is raised.
    """
    try:
        titles_df = pd.read_csv('html_to_excel/titles.csv')
        fields_df = pd.read_csv('html_to_excel/fields.csv')

        combined_df = pd.concat([titles_df, fields_df], axis=1)

        combined_df['Title'] = combined_df['Title'].str.split(' - ').str[1]
        combined_df = combined_df.sort_values(by='RiskRating', key=lambda x: pd.Categorical(x, categories=['Critical', 'High', 'Medium', 'Low', 'Informational'], ordered=True))

        # combined_df.to_excel('html_to_excel/combined_output.xlsx', index=False)  Change it if you want an excel file
        combined_df.to_csv('html_to_excel/combined_output.csv', index=False, encoding='utf-8-sig')

        print("Output files combined successfully.")

        # Delete old files
        # os.remove('html_to_excel/titles.xlsx')  Change it if you want an excel file
        # os.remove('html_to_excel/fields.xlsx')
        os.remove('html_to_excel/fields.csv')
        os.remove('html_to_excel/fields.csv')

        print("Old files deleted successfully.")

    except FileNotFoundError:
        print("Error: One or more input files not found.")

    except OSError as e:
        print(f"Error deleting old files: {e}")


if __name__ == "__main__":
    combine_output()