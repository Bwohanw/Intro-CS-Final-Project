#!/usr/bin/python3
import cgi


def writeinto():
    file = open('rating.txt','a')
    fileData = cgi.FieldStorage()
    first = fileData.getvalue("first name")
    last = fileData.getvalue("last name")
    subject = fileData.getvalue("name")
    comment = fileData.getvalue("stuff")
    fullname = first + ' ' + last

    rating = fileData.getvalue("rating")

    y = subject.lower()+'word'+fullname.lower()+'word'+str(rating)+'word'+comment+'\n'
    file.write(y)
    file.close()
#saves the values from the html and writes them to the csv file
def htmlTop():
    print ('''Content-type: text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>Rate my teachers. </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')





def main():
    htmlTop()
    print('Thank you for submitting your response!')
    writeinto()
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
