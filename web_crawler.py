import urllib.parse, urllib.request, urllib.error
import ssl
from bs4 import BeautifulSoup
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

take = input("Enter a url here: ")
count = 0
hekko = 0

print("Accessing {}\n".format(take))
try:
    fhand = urllib.request.urlopen(take, context = ctx).read()
    print('Retrieved {} characters\n'.format(len(fhand)))
    soup = BeautifulSoup(fhand, 'html.parser')

    print('   *What do wanna do???*     ')

    print('\n 1) See the code!!!\n') 
    print(' 2) Search a certain tag and its attribute!!!\n')
    print(' 3) Save the code!!!')

except:
    print('\n\nOppsiee Doopsie!! Wrong url!!!')
    count = 1

if count !=1: 
    hekko = int(input("Enter the no. of thing you wanna do: "))

if hekko == 1:
    print(soup)

elif hekko == 2:
    print('\n\nSo you have choosen this tag!!')
    print('\nType the tag name without ancher tags')
    try:
        tag_name = input('Here: ')
        print('\n\nDo you wanna search some attribute of it too??Type \'n\' for no')
        attr_tag = input('Here: ')
        tag = soup(tag_name)
        
        if attr_tag == 'n':
            for n in tag:
                print(n)
        
        else:
            for n in tag:
                print(n.get(attr_tag, None))

    except:
        print('Look buddy!! Either your tag is wrong or your attribute\n or their is not attribute in that python code')


elif hekko == 3:
    print('Do you wanna save the data??')
    print('Type \'y\' for yes and \'n\' for no')
    ff = input('Here: ')

    if ff == 'y':
        tagfd = soup('title')
        tagff = str(tagfd[0])
        tagff = tagff.split()
        alt = []
        for n in range(1, len(tagff) - 1):
            alt.append(tagff[n])

        hhmm = ' '.join(alt)
        hhmm = hhmm + '.txt'
        fhandy = open(hhmm, 'w')

        fhandy.write(str(soup))

        fhandy.close()             

     
    

    
