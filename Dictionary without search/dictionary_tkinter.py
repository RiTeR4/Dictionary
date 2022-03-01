import jsonpickle
from tkinter import *
from difflib import SequenceMatcher


class Word:
    def __init__(self, word, definition, language):
        self.word = word
        self.definition = definition
        self.language = language


class WordsStorage:
    def __init__(self):
        self.file_name = 'dictionary_data.json'

    def find_word(self, user_word):
        self.get_words()

        file_data = FileTool().read_file('dictionary_data.json')
        words = jsonpickle.decode(file_data)
        words_array = []
        for i in range(len(words)):
            words_array.append(words[i].word)
        max_ratio = 0
        likeable_word = ''

        for i in range(len(words)):
            if user_word.lower() == words[i].word:
                label1['text'] = f'{words[i].definition} \n' \
                                f'Язык(и): {words[i].language}'
                break
            elif SequenceMatcher(None, user_word, words_array[i]).ratio() > max_ratio:
                max_ratio = SequenceMatcher(None, user_word, words_array[i]).ratio()
                likeable_word = words_array[i]
            elif i == len(words) - 1:
                if max_ratio > 0:
                    label1['text'] = f'Возможно вы имели в виду {likeable_word}'
                else:
                    label1['text'] = 'Данное слово не найдено'
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

words_storage = WordsStorage()

root = Tk()
root.title('Dictionaty')
root.geometry('980x620')




frame = Frame(root, bg='#1a62b7')
frame.place(relwidth=1, relheight=1)

# label = Label(frame, bg='#ABAFAF', fg='white')
# label.pack() #1BA659 #D9e000

label = Label(frame, text='Enter Word', font=('Calibri', 16, 'bold'), bg='#1a62b7', fg='white')
label.pack()

entry_find = Entry(frame, bg='#FFFFFF', bd=0, width=22, font=('Calibri', 16, 'bold'), fg='black')
entry_find.pack()

label = Label(frame, bg='#1a62b7', fg='white')
label.pack()

button = Button(frame, text='FIND', bg='#F4CD3D', bd=0, font=('Calibri', 16, 'bold'), fg='black', padx=10, pady=5, command=lambda: words_storage.find_word(entry_find.get()))
button.pack()

label = Label(frame, bg='#1a62b7', fg='white')
label.pack()

label1 = Label(frame, bg='#1a62b7', wraplength=700, font=('Calibri', 16, 'bold'), fg='white')
label1.pack()


root.mainloop()
