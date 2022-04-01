#!/usr/bin/python3

import cgi
import itertools

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>Anagrams </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')

fieldData = cgi.FieldStorage()
word = fieldData.getvalue("word")

source = open('/etc/dictionaries-common/words','r',encoding='utf-8')
new = source.readlines()
wao = []
for x in new:
    wao.append(x.strip())
#creates a new list of the words without \n
def permute():
    words = []
    for x in itertools.permutations(word):
        if (''.join(x).capitalize()) not in words:
            words.append(''.join(x).capitalize())
    return words
#returns all premutations of the word in a list
if len(word) <= 7:
    z = permute()#saves that list as a variable
def checkword(L):
    actualword = []
    for x in L:
        for y in wao:
            if x.lower() == y.lower():
                if x.capitalize() not in actualword:
                    actualword.append(x.capitalize())
    return actualword
#checks the elements in the dictionary to see which in the list are in the dictionary

def main():
    htmlTop()
    if len(word)>7:
        print('word too long')
    else:
        counter = 1
        print('Permutations:')
        print("<br>")
        for x in z:
            print(str(counter)+'. '+x)
            print("<br>")
            counter += 1
        counter = 1
        print('anagrams:')
        print("<br>")
        for x in checkword(z):
            print(str(counter)+'. '+x)
            print("<br>")
            counter += 1
    htmlTail()
#prints the permutations and anagrams as well as numbers next to the permutations
source.close()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
