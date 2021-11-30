# this script partially uses sample code provided in the official Flair repository

from flair.data import Sentence #used for sentence
from flair.models import SequenceTagger
from flair.tokenization import SegtokSentenceSplitter
import os
import csv

directory = os.fsencode('/mnt/data/gold_standard/overlap/original_texts/')

# The model key is taken from 'https://huggingface.co/flair/ner-english-large' and automatically downloads the newest version
tagger = SequenceTagger.load('ner-large')
# initialize sentence splitter
splitter = SegtokSentenceSplitter() 

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"): 
        with open("/mnt/data/gold_standard/overlap/original_texts/"+filename,'r') as file:
            text = file.read()
        # use splitter to split text into list of sentences
        sentences = splitter.split(text)
        # predict tags for sentences
        tagger.predict(sentences)
        # write tagged tokens to file
        with open("/mnt/flair/" + filename.replace('.txt','.tsv'), 'a') as w_file:
            tsv_writer = csv.writer(w_file, delimiter='\t')
            tsv_writer.writerow(['original_word', 'ner', 'confidence'])
            for sentence in sentences:
                for token in sentence:
                    tag = token.get_tag('ner')
                    #print(f'{str(token).split()[2]} {tag.value} {round(tag.score,2)}')
                    tsv_writer.writerow([str(token).split()[2], tag.value, str(round(tag.score,2))])