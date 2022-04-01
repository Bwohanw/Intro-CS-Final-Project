#!/usr/bin/python3

import cgi

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>Letter Maker </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')


fileData = cgi.FieldStorage()
title = fileData.getvalue("title")
name = fileData.getvalue("name")
item1 = fileData.getvalue("item1")
item2 = fileData.getvalue("item2")
item3 = fileData.getvalue("item3")
#stores all the values of the blanks
    
def main():
    htmlTop()
    print('Dear {} {},'.format(title,name))
    print('<br><br>')
    print('{} needs your help! They\'ve encountered {} and need YOUR help to get rid of it! To help them get rid of it, all they need are your 9-digit social security number, the last 4 numbers on the back of your credit card, and your 10 digit phone number. Plus, we\'ll send you a FREE {} for your enourmous help to your heroes!! Enjoy your completely FREE GIFT!!! They will 100% win now!'.format(item1,item2,item3))
    print('<br><br>')
    print('Sincerely')
    print('<br><br>')
    print('The Agency')
    htmlTail()
    
#prints the entire letter with the blanks filled in

if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
