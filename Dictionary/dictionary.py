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

    def get_words(self):
        json_data = FileTool().read_file(self.file_name)
        words = jsonpickle.decode(json_data)
        return words

    def add_word(self):
        user_word = input('Введите слово: ')
        user_definition = input('Введите определение: ')
        user_language = input('Введите язык: ')

        file_data = FileTool().read_file('dictionary_data.json')
        words = jsonpickle.decode(file_data)
        words.append(Word(user_word, user_definition, user_language))
        self.safe_words(words)

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


WordsStorage().get_words()

user_answer = input('Хотите добавить слово?(y или n)\n')
if user_answer.lower() == 'y':
    WordsStorage().add_word()

file_data = FileTool().read_file('dictionary_data.json')
words = jsonpickle.decode(file_data)

user_word = input('Какое слово желаете найти?\n')
for i in range(len(words)):
    if user_word == words[i].word:
        print(words[i].definition, words[i].language)
        break
    elif i == len(words) - 1:
        print('Данное слово не найдено')
