from bs4 import BeautifulSoup
import requests
import time 

root_url = 'https://pastebin.com'
href_history = []

def main(): 
    
    while True:
        response = requests.get(root_url + '/archive')
        print(response.status_code)
        if response.status_code == 200: 
            print('succesfully received webpage')
            print(response.text)
            soup = BeautifulSoup(response.text, features="html.parser")
            hrefs = [tr.find('a', href=True)['href'] for tr in soup.find('table', {'class':'maintable'}).find_all('tr')[1:]]

            for href in find_new_pastes(hrefs):
                # find_keywords(href)
                print(href)
        time.sleep(10)

def find_keywords(href):
    response = requests.get(root_url + href)
    print(response.status_code)


def find_new_pastes(hrefs): 
    new_pastes = []
    for href in hrefs:
        if href not in href_history:
            new_pastes.append(href)
            href_history.append(href)
    print('found {} new pasts', len(new_pastes))
    return new_pastes

if __name__ == '__main__':
    main()