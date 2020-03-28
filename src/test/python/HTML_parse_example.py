import requests
from bs4 import BeautifulSoup
import frequency_data
sites = [
    'http://www.nytimes.com',
]
for url in sites:
    r = requests.get(url)
    page_source = r.text
soup = BeautifulSoup(page_source, "html.parser")


for link in soup.find_all('meta'):
    if link.get('name') == 'keywords':
        keywords = link.get('content')


p1 = frequency_data.frequency_data()
print(keywords)
keyword_list = keywords.split(',')
for i in range(len(keyword_list)):
    if keyword_list[i] == " ":
        keyword_list[i].remove

    result = page_source.count("\"vernacular\":" +"\""+keyword_list[i]+"\"")
    #print("Index {}: Keyword {}: Appears {}".format(i, keyword_list[i], result))

    p1.add(keyword_list[i], result)

print(p1.freqdict)
print(p1.Keywords()[0])
print(p1.Count()[0])

myList = p1.sort_max()
print(myList)
# Create class with the following methods:
# frequency_data.add(Keyword, Count) Adds a new keyword and count to the object
# frequency_data.Keyword() Returns an list array containing Keywords so that frequency_data.Keyword()[0] is the first keyword in the list
# FrequencyData.Count() Returns an int array of frequency counts so that frequency_data.Count()[0] is the frequency count corresponding to FrequencyData.Keyword()[0]
#
# Create src/test/python/test_frequency_data.py to test the class and provide dummy data


# Python Dictionary function and list used to create class




