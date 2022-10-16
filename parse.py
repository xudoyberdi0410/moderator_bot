import requests
from bs4 import BeautifulSoup as bs


def get_page(url) -> None:
    r = requests.get(url=url)
    return r.text


def parse_page(url) -> list:
    r = requests.get(url=url)
    soup = bs(r.text, "lxml")

    links = []
    link_tags = [j[-1].find_all('a') for j in [i.find_all('td')
                                               for i in soup.find('table').find('tbody').find_all('tr')]]
    for i in link_tags:
        for j in i:
            link = str(j.get('href')).split('/')[-2]
            links.append([j.text, link])

    return links


def main() -> list:
    # text = get_page(url="http://idum.uz/ru/archives/12209")
    return parse_page(url="http://idum.uz/ru/archives/12209")


if __name__ == "__main__":
    main()
