import requests
import urllib.request, urllib.parse, urllib.error
import webbrowser
import ssl
from bs4 import BeautifulSoup
import os
from pathlib import Path

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inp = input('Enter your input here: ')
website = 'http://www.mangareader.net/search/?'
main_website = 'http://www.mangareader.net'

hehe = urllib.parse.urlencode({'w':inp})

flip = requests.get(website + hehe)
flip.raise_for_status()

soup = BeautifulSoup(flip.text, 'html.parser')

tags = soup('h3')
sno = 1
alt = []

for n in tags:
    print(sno, ' ', n.getText())
    sno += 1

    alt.append(n('a')[0].get('href', None))

takin = int(input('Whats ya no: '))

webpage = requests.get(main_website + alt[takin - 1])
webpage.raise_for_status()

code = BeautifulSoup(webpage.text, 'html.parser')

column = code('td')
count = []
for n in column:
    try:
        count.append(n('a')[0].get('href', None))


    except:
        pass

count.pop(0)
count.pop(len(count) - 1)
count.pop(len(count) - 1)
print('The manga has {} chapters'.format(len(count)))

hfgh = int(input('ENTER NO...: '))
ggfg = int(input('Enter ending no...: '))
heggo = count[hfgh - 1]
flop = []

while heggo != count[ggfg]:
    fg= 0 
    m= 1
    hekk = main_website + heggo
    os.makedirs('hemmo/{}'.format(count[hfgh - 1]))
    while fg == 0:


        flip = requests.get(hekk)
        flip.raise_for_status

        sroup = BeautifulSoup(flip.text, 'html.parser')

        hing = sroup('img')
        hist = sroup('span')
        hings = hing[0].get('src', None)
        files = open('hemmo/{}/{}.jpg'.format(count[hfgh-1],m), 'wb')
        m += 1
        for chunk in requests.get(hings).iter_content(10000):
            files.write(chunk) 
        print('{} page downloaded'.format(count[hfgh - 1]))

        for n in hist:
            try: 
                if n.get('class', None)[0] == 'next':
                    heggo = n('a')[0].get('href', None)
            except:
                pass

        hekk = main_website + heggo

        if heggo == count[hfgh]:
            fg = 1


    hfgh += 1  
    heggo = count[hfgh -1 ]
    flop.append(count[hfgh - 1])

asdf = input('Do you wanna convert the downloaded images into pdf? (y/n): ')

if asdf == 'y':
    path = Path.cwd()
    alt = []
    for n in flop:
        path = path + 'hemmo/{}'.format(n)
        print(path)