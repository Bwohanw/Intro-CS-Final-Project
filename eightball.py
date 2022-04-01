#!/usr/bin/python3

import cgi
import random
def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>Eightball </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')
formData = cgi.FieldStorage()
question = formData.getvalue("question")
ballreturnes = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - Definitely", "You may rely on it.", "As I see it, yes.", "Most likely", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
def eightball():
    return random.choice(ballreturnes)
#returns a random value from the list
def main():
    htmlTop()
    print('Question: {}'.format(question))
    print('<br>')
    print('Answer: {}'.format(eightball()))#prints that value from the list
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
