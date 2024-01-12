import spacy
from transformers import AutoModelForTokenClassification, AutoTokenizer
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter 

nlp_sci = spacy.load("en_core_sci_sm")
nlp_bc5 = spacy.load("en_ner_bc5cdr_md")
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-v1.1")

nlp_sci.max_length = 10**9
nlp_bc5.max_length = 10**9



def extract_entities(text, model_name):
    doc = nlp_sci(text) if model_name == "scispaCy" else nlp_bc5(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ("DISEASE", "CHEMICAL")]
    return entities

def compare_entities(entities1, entities2):
    total_sci = len(entities1)
    total_biobert = len(entities2)
    common = set(entities1) & set(entities2)
    unique_sci = set(entities1) - set(entities2)
    unique_biobert = set(entities2) - set(entities1)
    common_words_sci = get_common_words(entities1)
    common_words_biobert = get_common_words(entities2)

    return total_sci, total_biobert, common, unique_sci, unique_biobert, common_words_sci, common_words_biobert

def get_common_words(entities):
    all_words = [word.lower() for entity, _ in entities for word in entity.split()]
    most_common_words = Counter(all_words).most_common(10) #Adjustable Number
    return most_common_words

def process_chunk(chunk, model_sci, model_biobert):
    entities_sci = extract_entities(chunk, model_sci)
    entities_biobert = extract_entities(chunk, model_biobert)

    result_tuple = compare_entities(entities_sci, entities_biobert)
    total_sci, total_biobert, common, unique_sci, unique_biobert, common_words_sci, common_words_biobert = result_tuple

    return total_sci, total_biobert, common, unique_sci, unique_biobert, common_words_sci, common_words_biobert

with open("X:\\Python\\text.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Processing text...")
start_time = time.time()

chunks = text.split(".")
num_chunks = len(chunks)
batch_size = 10  # Adjustable Number


with ThreadPoolExecutor() as executor:
    futures = []
    completed_count = 0

    for i in range(0, num_chunks, batch_size):
        batch = chunks[i:i + batch_size]
        future = executor.submit(process_chunk, ".".join(batch), "scispaCy", "BioBERT")
        futures.append(future)

    for future in as_completed(futures):
        result_tuple = future.result()
        total_sci, total_biobert, common, unique_sci, unique_biobert, common_words_sci, common_words_biobert = result_tuple

        # Print progress:
        print("\n**Comparison of entities for batch {}:**".format(completed_count + 1))
        print("Total entities detected by scispaCy: {}".format(total_sci))
        print("Total entities detected by BioBERT: {}".format(total_biobert))
        print("Common entities: {}".format(common))
        print("Unique entities in scispaCy: {}".format(unique_sci))
        print("Unique entities in BioBERT: {}".format(unique_biobert))
        print("Most common words in scispaCy entities: {}".format(common_words_sci))
        print("Most common words in BioBERT entities: {}".format(common_words_biobert))

        completed_count += 1
        progress_percentage = (completed_count / (num_chunks / batch_size)) * 100
        print("\rProcessed batches {}/{} ({:.2f}%)".format(completed_count, num_chunks // batch_size, progress_percentage), end="")

print("\nProcessing completed in {:.2f} seconds.".format(time.time() - start_time))
