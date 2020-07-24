import requests
from bs4 import BeautifulSoup



# response = requests.get(URL)

# content = response.content

# soup = BeautifulSoup(content, 'html.parser')

# result = soup.find_all(title="Wikipedia:Citation needed")

# for i in result:
#     print('1 \n')

def get_citations_needed_count(url):
    count = 0
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find_all(title="Wikipedia:Citation needed")
    for _ in result:
        count += 1
    return count

def get_citations_needed_report(url):
    pass

if __name__ == '__main__':
    print('Please enter url: ')
    URL = input()
    print(get_citations_needed_count(URL))
