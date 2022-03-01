import codecs
file = codecs.open('words2.txt', 'r', 'utf_8')
words = file.readlines()
file.close()
print(words)
for i in range(len(words)):
    if words[i] == '(Pas)\r\n':
        words[i] = 'Pas\r\n'
    elif words[i] == '(Py)\r\n':
        words[i] = 'Py\r\n'
    elif words[i] == '(Pas, Py)\r\n':
        words[i] = 'Pas, Py\r\n'
    elif words[i] == '(Pas)':
        words[i] = 'Pas'
file = codecs.open('words2output.txt', 'w', 'utf_8')
file.writelines(words)
file.close()