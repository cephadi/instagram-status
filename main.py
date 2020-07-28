from bs4 import BeautifulSoup
import requests

URL = "https://www.instagram.com/{}/"

def parsing_data(meta):
    data = {}
    meta = meta.split("-")[0]
    meta = meta.split(" ")
    data['followers'] = meta[0]
    data['following'] = meta[2]
    data['posts'] = meta[4]
    return data

def get_pages(username_ig):
    req = requests.get(URL.format(username_ig))
    html = BeautifulSoup(req.text, "html.parser")
    meta = html.find("meta", property="og:description")
    return parsing_data(meta.attrs['content'])

if __name__ == "__main__":
    username_ig = "tiktok"
    data = get_pages(username_ig)
    print("This account has", data['followers'], 'followers')
    print("This account has", data['following'], 'following')
    print("This account has", data['posts'], 'posts')