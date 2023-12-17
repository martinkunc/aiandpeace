import deepl 
import os
import logging
from long_text_synthesizer import LongTextSynthesizer
from pathlib import Path
def read_file(file_name):
    #open and read the file after the appending:
    f = open(file_name, "r")
    text = f.read()
    return text

def translate(text):
    deepl_key = os.getenv('DEEPL_KEY')
    translator = deepl.Translator(deepl_key) 
    result = translator.translate_text(text, target_lang="cs")
    return result.text

def write_file(file_name, text):
    f = open(file_name, "w")
    f.write(text)
    f.close()

    

#text = read_file("aiandpeace.txt")
#translated = translate(text)
#write_file("aiandpeace_cz.txt",translated)

#text = read_file("aiandpeace.txt")

logging.basicConfig(level=logging.INFO)
text = read_file("aiandpeace_cz.txt")
s = LongTextSynthesizer(subscription=os.getenv('SPEECH_KEY'), region=os.getenv('SPEECH_REGION'))

s.synthesize_text(text, output_path=Path('./aiandpeace'))

