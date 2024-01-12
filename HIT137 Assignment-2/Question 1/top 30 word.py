import csv
from collections import Counter
import re
from tqdm import tqdm
import os

WORD_REGEX_PATTERN = r'\b(?![0-9]+\b)\w+\b'

def get_top_words(file_path, top_n=30, chunk_size=1024):
    word_counts = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        file_size = os.path.getsize(file_path)
        with tqdm(total=file_size, unit='B', unit_scale=True, desc='Processing file') as pbar:
            for chunk in iter(lambda: file.read(chunk_size), ''):
                words = re.findall(WORD_REGEX_PATTERN, chunk.lower())
                word_counts.update(words)
                pbar.update(len(chunk))

    return word_counts.most_common(top_n)

def write_top_words_to_csv(top_words, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'Count'])
        writer.writerows(top_words)

def main():
    input_txt_file = 'X:\\Python\\text.txt'
    output_csv_file = 'Top 30 words.csv'

    top_words = get_top_words(input_txt_file)
    write_top_words_to_csv(top_words, output_csv_file)

    print(f'Top 30 words and their counts saved to {output_csv_file}')

if __name__ == "__main__":
    main()
