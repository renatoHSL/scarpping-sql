import requests
import selectorlib
import time

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'
}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperatures"]
    return value


def get_current_time():
    current_time = time.localtime()
    formatted_time = time.strftime("%y-%m-%d-%H-%M-%S", current_time)
    return formatted_time


def store(data, localtime):
    with open("data.txt", "a") as file:
        file.write(f"{localtime}, {data} \n")


def read(data):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scrapped = scrape(URL)
    extracted = extract(scrapped)
    time = get_current_time()
    print(extracted)

    content = read(extracted)
    store(extracted, time)

