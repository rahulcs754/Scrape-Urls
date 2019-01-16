from urllib.request import urlopen
from bs4 import BeautifulSoup 
import sys 
#import file for Regex
import re
#import file for csv files
import csv

a = sys.argv[1]

html = urlopen(a)
bs = BeautifulSoup(html, 'html.parser')

def Checkhttps(datas):
        return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', datas)

#for link in data_url:
#        print(link)

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        if Checkhttps(link.attrs['href']): 
            print(link.attrs['href'])
            with open("test.txt", "a") as myfile:
                myfile.write(link.attrs['href']+ '\n') 
            myfile.close()

            with open('people.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(link.attrs['href'])
            
            writeFile.close()