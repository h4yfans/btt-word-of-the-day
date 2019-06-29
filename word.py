from bs4 import BeautifulSoup
import requests


def main():
    source = requests.get('https://www.lexico.com/en').text
    soup = BeautifulSoup(source, 'lxml')
    dow = soup.find(class_='linkword').text

    defination_source = requests.get("https://www.lexico.com/en/definition/{}".format(dow)).text
    soup = BeautifulSoup(defination_source, 'lxml')
    meaning = soup.find(class_='ind').text
    sentence = soup.find(class_='ex').text

    print("{}: {}\n{}".format(dow, meaning, sentence))


if __name__ == '__main__':
    main()
