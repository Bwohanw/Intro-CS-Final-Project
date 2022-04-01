#!/usr/bin/python3

import cgi

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>Teacher Statistics. </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')


fileData = cgi.FieldStorage()
teacher = fileData.getvalue("fullname").lower()
subject = fileData.getvalue("name").lower()
file = open('rating.txt','r')
filelist = file.readlines()
newlist = []
for x in filelist:
    newlist.append(x.split('word'))

def getdata():
    d = {}
    for x in newlist:
        if x[1] not in list(d.keys()):
            d[x[1]] = [ [x[2]+ ','],
                        [x[3].strip('\n') + ','] ]
        else:
            d[x[1]][0].append(x[2])
            d[x[1]][1].append(x[3].strip('\n')+ ',')
    return d
#makes a dictionary where each teacher name is a key and it corresponds to
#all the ratings and comments about them
p = getdata()
pval = p.get(teacher)
###gets the values corresponding to the specific teacher searched
def main():
    htmlTop()
    if teacher not in list(p.keys()):
        print("teacher name not found")
    else:
        print('Teacher: ')
        print(teacher.title())
        print('<br>')
        print('<br>')
        print('Subject: ')
        print(subject)
        print('<br>')
        print('<br>')
        print('Rating, (1-dislike to 5-LOVE) : ')
        for i in pval[0]:
            print(i)
        print('<br>')
        print('<br>')
        print('Some comments are: ')
        for i in pval[1]:
            print(i)
###formats the data being outputted so it's more ordered
    htmlTail()

file.close()

if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()

