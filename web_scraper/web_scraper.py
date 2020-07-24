import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    count = 0
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find_all(title="Wikipedia:Citation needed")
    for _ in result:
        count += 1
    return f'\nThe wikipedia page: "{url}" has {count} passages where citation is needed.\n'

def get_citations_needed_report(url):
    passages = ''
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    results = soup.find_all(title="Wikipedia:Citation needed")
    for i in results:
        passages = passages + str(i.parent.parent.parent.text) + '\n'
    return f'The passages are:\n\n{passages}' 

if __name__ == '__main__':
    print('Please enter url: ')
    URL = input()
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
