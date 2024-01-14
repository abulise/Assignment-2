import csv
import os
from tqdm import tqdm

def extract_text_from_csv(csv_file_path):
    text_column = []

    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        text_column = [row.get('TEXT', '') for row in reader]

    return text_column

def write_to_txt(output_file_path, text_list):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(text + '\n' for text in text_list)

def extract_and_merge_csv_files(csv_folder_path, output_txt_file):
    all_text = []
    csv_files = [filename for filename in os.listdir(csv_folder_path) if filename.endswith('.csv')]

    for filename in tqdm(csv_files, desc='Processing CSV files', unit='file'):
        csv_file_path = os.path.join(csv_folder_path, filename)
        text_column = extract_text_from_csv(csv_file_path)
        all_text.extend(text_column)

    write_to_txt(output_txt_file, all_text)
    print(f'Text extracted from CSV files and saved to {output_txt_file}')

if __name__ == "__main__":
    csv_folder = 'X:\\Python\\Assignment-2'
    output_txt_file = 'text_file.txt'

    extract_and_merge_csv_files(csv_folder, output_txt_file)
