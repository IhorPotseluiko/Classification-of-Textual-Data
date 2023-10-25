"""from nltk.corpus import words
import nltk
nltk.download('words', download_dir='C:/Users/ggh76/Desktop/Classification of Textual Data/training_data')
word_list = words.words()
# prints 236736
print(len(word_list))"""

# Відкрийте текстовий файл для читання
with open('C:/Users/ggh76/Desktop/Classification of Textual Data/training_data/corpora/words/en-basic', 'r') as file:
    # Прочитайте вміст файлу
    text = file.read()

# Розділіть текст на окремі слова
words = text.split()

# Тепер 'words' містить масив слів із текстового файлу
print(words)


"""
скачать слова з look for "words" under the "Corpora" tab
"""