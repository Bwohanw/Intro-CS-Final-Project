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


file = open('rating.txt','a')
fileData = cgi.FieldStorage()
##first = fileData.getvalue("first name")
##last = fileData.getvalue("last name")
##subject = fileData.getvalue("name")
##comment = fileData.getvalue("stuff")
first = 'jumash'
last = 'aziz'
subject = 'math'
comment = 'xd'
fullname = first + ' ' + last
rating = 5
#rating = fileData.getvalue("rating")

y = subject+','+fullname+','+str(rating)+','+comment+'\n'
#file.write(y)
file.close()


file = open('rating.txt','r')
filelist = file.readlines()
newlist = []
for x in filelist:
    newlist.append(x.split(','))
print(newlist)

#subject,teacher, rating, comments
dic = {'english':[[''], [], []], 'math':[[''], [], []],'computer science':[[''], [], []],'music':[[''], [], []],'science':[[''], [], []],'history':[[''], [], []],'physical education':[[''], [], []]}


counter2 = 0
for i in newlist:
    counter = 0
    rating = newlist[counter2][2]
    comment = newlist[counter2][3]
#    print(newlist[0][2])
    if i[counter] == 'english':
        if newlist[counter][1] != i[counter]:
            (dic.get('english')[0]) = newlist[counter2][1]
            (dic.get('english')[1]).append(rating)
            (dic.get('english')[2]).append(comment.split())
            counter2 += 1
    elif i[counter] == 'math':
        if newlist[counter][1] != i[counter]:
            (dic.get('math')[0]) = newlist[counter2][1]
            (dic.get('math')[1]).append(rating)
            (dic.get('math')[2]).append(comment.split())
            counter2 += 1
    elif i[counter] == 'computer science':
        if newlist[counter][1] != i[counter]:
            (dic.get('computer science')[0]) = newlist[counter2][1]
            (dic.get('computer science')[1]).append(rating)
            (dic.get('computer science')[2]).append(comment.split())
            counter2 += 1
    elif i[counter] == 'music':
        if newlist[counter][1] != i[counter]:
            (dic.get('music')[0]) = newlist[counter2][1]
            (dic.get('music')[1]).append(rating)
            (dic.get('music')[2]).append(comment.split())
            counter2 += 1
    elif i[counter] == 'science':
        if newlist[counter][1] != i[counter]:
            (dic.get('science')[0]) = newlist[counter2][1]
            (dic.get('science')[1]).append(rating)
            (dic.get('science')[2]).append(comment.split())
            counter2 += 1
    elif i[counter] == 'history':
        if newlist[counter][1] != i[counter]:
            (dic.get('history')[0]) = newlist[counter2][1]
            (dic.get('history')[1]).append(rating)
            (dic.get('history')[2]).append(comment.split())
            counter2 += 1
    elif i[counter] == 'physical education':
        if newlist[counter][1] != i[counter]:
            (dic.get('physical education')[0]) = newlist[counter2][1]
            (dic.get('physical education')[1]).append(rating)
            (dic.get('physical education')[2]).append(comment.split())
            counter2 += 1
    counter += 1
print(dic)


def main():
    htmlTop()
    htmlTail()

file.close()

if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
