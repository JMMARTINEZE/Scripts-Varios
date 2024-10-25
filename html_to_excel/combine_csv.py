import os
import pandas as pd

def combine_output():
    try:
        titles_df = pd.read_excel('html_to_excel/titles.xlsx')
        fields_df = pd.read_excel('html_to_excel/fields.xlsx')

        combined_df = pd.concat([titles_df, fields_df], axis=1)

        combined_df['Title'] = combined_df['Title'].str.split(' - ').str[1]
        combined_df = combined_df.sort_values(by='RiskRating', key=lambda x: pd.Categorical(x, categories=['Critical', 'High', 'Medium', 'Low', 'Informational'], ordered=True))

        combined_df.to_excel('html_to_excel/combined_output.xlsx', index=False)
        combined_df.to_csv('html_to_excel/combined_output.csv', index=False, encoding='utf-8-sig')

        print("Output files combined successfully.")

        # Delete old files
        os.remove('html_to_excel/titles.xlsx')
        os.remove('html_to_excel/fields.xlsx')

        print("Old files deleted successfully.")

    except FileNotFoundError:
        print("Error: One or more input files not found.")

    except OSError as e:
        print(f"Error deleting old files: {e}")


if __name__ == "__main__":
    combine_output()