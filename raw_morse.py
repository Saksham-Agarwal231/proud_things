import json

fhand = open('moorse.json', 'r')


hello = json.load(fhand)
takein = 'hjc'
while takein != '*':
    takein = input('Enter something here(type *, if you wanna quit): ')
    takein = takein.lower()
    if takein == '*':
        break
    

    for n in range(len(takein)):
        if takein[n] in hello:
            print(hello[takein[n]], end = ' ')

        elif takein[n] == ' ':
            print('/', end = ' ')

    print('\n\n')

