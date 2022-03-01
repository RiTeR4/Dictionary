import jsonpickle
import codecs


class Word:
    def __init__(self, word, definition, language):
        self.word = word
        self.definition = definition
        self.language = language

class WordsStorage:
    def __init__(self):
        self.file_name = 'dictionary_data.json'

    def safe_words(self, words):
        json_data = jsonpickle.encode(words)
        FileTool().writelines(self.file_name, json_data)

class FileTool:
    def writelines(self, path, data):
        file = open(path, 'w')
        file.writelines(data)
        file.close()

    def read_file(self, path):
        file = open(path, 'r')
        file_data = file.read()
        file.close()
        return file_data

file = codecs.open("words2output.txt", "r", "utf_8")
words = file.readlines()
file.close()
print(words)

words[0] = words[0][1:]
words[len(words) - 1] = words[len(words) - 1] + '12'
for i in range(len(words)):
    words[i] = words[i][:-2]
print(words)
words_objects = []
for i in range(len(words) - 2):
    if i % 3 == 0:
        words_objects.append(Word(words[i], words[i + 1], words[i + 2]))
WordsStorage().safe_words(words_objects)
print(words_objects[1].word)
