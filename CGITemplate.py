#!/usr/bin/python3

import cgi

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>My first server-side script. </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')

def getData():
	formData = cgi.Fieldstorage()
	firstName = formdata.getvalue('firstname')
	return firstName

def main():
    htmlTop()
    print('hello {}'.format(getData()))
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
