from services.text_analyser import TextAnalyser
from pprint import pprint
from zipfile import ZipFile

SOURCE_FILE_NAME = "text.txt"
OUTPUT_FILE_NAME = "output.txt"
ZIP_FILE_NAME = "myzip.zip"

def task2():
    with open(SOURCE_FILE_NAME, encoding="utf-8") as file:
        text = file.read()

    result = TextAnalyser.analyze_text(text)

    print('-' * 148)
    pprint(result)
    print('-' * 148)

    with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as file:
        file.write(str(result))

    with ZipFile(ZIP_FILE_NAME, 'a') as file:
        file.write(OUTPUT_FILE_NAME)

    with ZipFile(ZIP_FILE_NAME) as file:
        content = file.read(OUTPUT_FILE_NAME)

    # pprint(content)

    
    