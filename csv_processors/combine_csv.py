import os
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def read_titles_file():
    try:
        return pd.read_csv('../outputs/titles.csv')
    except FileNotFoundError:
        logging.error("Error: titles.csv file not found")
        return None

def read_fields_file():
    try:
        return pd.read_csv('../outputs/fields.csv')
    except FileNotFoundError:
        logging.error("Error: fields.csv file not found")
        return None

def combine_dataframes(titles_df, fields_df):
    try:
        combined_df = pd.concat([titles_df, fields_df], axis=1)
        return combined_df
    except Exception as e:
        logging.error(f"Error combining dataframes: {e}")
        return None

def write_combined_file(combined_df):
    try:
        combined_df.to_csv('../outputs/combined_output.csv', index=False, encoding='utf-8-sig')
        logging.info("Output file written successfully")
    except Exception as e:
        logging.error(f"Error writing output file: {e}")

def delete_old_files():
    try:
        os.remove('../outputs/fields.csv')
        logging.info("Old files deleted successfully")
    except OSError as e:
        logging.error(f"Error deleting old files: {e}")

def combine_output():
    titles_df = read_titles_file()
    fields_df = read_fields_file()
    if titles_df is None or fields_df is None:
        return
    combined_df = combine_dataframes(titles_df, fields_df)
    if combined_df is None:
        return
    write_combined_file(combined_df)
    delete_old_files()

if __name__ == "__main__":
    combine_output()