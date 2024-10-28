import os
import pandas as pd
import logging
from dotenv import load_dotenv


# Carga las variables de entorno desde el archivo .env
load_dotenv('../.env')


# Configuración de logging
logging.basicConfig(level=logging.INFO)


def read_titles_file(html_file):
    try:
        return pd.read_csv(os.path.join(os.getenv('OUTPUT_FOLDER'), f"{os.path.basename(html_file).replace('.html', '_titles.csv')}"))
    except FileNotFoundError:
        logging.error(f"Error: {os.path.basename(html_file).replace('.html', '_titles.csv')} file not found")
        return None


def read_fields_file(html_file):
    try:
        return pd.read_csv(os.path.join(os.getenv('OUTPUT_FOLDER'), f"{os.path.basename(html_file).replace('.html', '_fields.csv')}"))
    except FileNotFoundError:
        logging.error(f"Error: {os.path.basename(html_file).replace('.html', '_fields.csv')} file not found")
        return None


def combine_dataframes(titles_df, fields_df):
    try:
        combined_df = pd.concat([titles_df, fields_df], axis=1)
        return combined_df
    except Exception as e:
        logging.error(f"Error combining dataframes: {e}")
        return None


def write_combined_file(combined_df, html_file):
    try:
        combined_df.to_csv(os.path.join(os.getenv('OUTPUT_FOLDER'), f"{os.path.basename(html_file).replace('.html', '_combined.csv')}"), index=False, encoding='utf-8-sig')
        logging.info(f"Output file written successfully: {os.path.basename(html_file).replace('.html', '_combined.csv')}")
    except Exception as e:
        logging.error(f"Error writing output file: {e}")


def delete_old_files(html_file):
    try:
        os.remove(os.path.join(os.getenv('OUTPUT_FOLDER'), f"{os.path.basename(html_file).replace('.html', '_fields.csv')}"))
        os.remove(os.path.join(os.getenv('OUTPUT_FOLDER'), f"{os.path.basename(html_file).replace('.html', '_titles.csv')}"))
        logging.info("Old files deleted successfully")
    except OSError as e:
        logging.error(f"Error deleting old files: {e}")


def combine_output():
    input_html_folder = os.getenv('INPUT_HTML_FOLDER')
    for file in os.listdir(input_html_folder):
        if file.endswith('.html'):
            html_file = os.path.join(input_html_folder, file)
            titles_df = read_titles_file(html_file)
            fields_df = read_fields_file(html_file)
            if titles_df is None or fields_df is None:
                continue
            combined_df = combine_dataframes(titles_df, fields_df)
            if combined_df is None:
                continue
            write_combined_file(combined_df, html_file)
            delete_old_files(html_file)


if __name__ == "__main__":
    combine_output()