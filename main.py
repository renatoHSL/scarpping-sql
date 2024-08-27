import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"
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
    value = extractor.extract(source)["tours"]
    return value


def send_email():
    print("Email was sent!")


def store(data):
    with open("data.txt", "a") as file:
        file.write(data + "\n")


def read(data):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scrapped = scrape(URL)
    extracted = extract(scrapped)
    print(extracted)

    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in "data.txt":
            store(extracted)
            send_email()
