from transformers import AutoTokenizer
from collections import Counter
import os
from tqdm.auto import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def tokenize_chunks(chunks, tokenizer):
    return [tokenizer.tokenize(chunk) for chunk in chunks]

def count_unique_tokens(file_path, model_name, chunk_size=512, batch_size=5, top_n=30):
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    token_counts = Counter()

    file_size = os.path.getsize(file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        with tqdm(total=file_size, desc="Tokenizing") as pbar:
            with ThreadPoolExecutor() as executor:
                futures = []
                chunks = []
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break

                    chunks.append(chunk)

                    if len(chunks) >= batch_size:
                        future = executor.submit(tokenize_chunks, chunks, tokenizer)
                        futures.append(future)
                        chunks = []

                        if len(futures) >= batch_size:
                            for completed_future in tqdm(as_completed(futures), total=len(futures), desc="Processing batches", leave=False):
                                batch_tokens = completed_future.result()
                                for tokens in batch_tokens:
                                    token_counts.update(tokens)
                                    pbar.update(len(chunk))

                            futures = []

                # Process remaining futures
                for completed_future in tqdm(as_completed(futures), total=len(futures), desc="Processing remaining batches", leave=False):
                    batch_tokens = completed_future.result()
                    for tokens in batch_tokens:
                        token_counts.update(tokens)
                        pbar.update(len(chunk))

    return token_counts.most_common(top_n)

def main():
    txt_file = "C:\\Users\\LISE\\Desktop\\python programs\\Assignment-2\\Question 1\\text_file.txt"
    model_name = 'bert-base-uncased'
    top_tokens = count_unique_tokens(txt_file, model_name)

    print(f'Top 30 unique tokens and their counts:')
    for token, count in top_tokens:
        print(f'{token}: {count}')

if __name__ == "__main__":
    main()
