from unidecode import unidecode

import string
import unidecode

def remove_punctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))

def clean_text(text):
    return unidecode.unidecode(text).lower().strip().split()

def format_text_report(report):
    cleaned_report = clean_text(report)
    cleaned_report_words = [remove_punctuation(word) for word in cleaned_report]
    return cleaned_report_words
