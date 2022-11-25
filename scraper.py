import os
import string
import requests
from bs4 import BeautifulSoup

EXAMPLE_URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
PROTOCOL = "https://"
DOMAIN = "www.nature.com"
PATH_ARTICLES_SORTED = string.Template("/nature/articles?sort=PubDate&year=2020&page=$number")
URL = string.Template("$protocol$domain$path$anchor")


def get_response(protocol=PROTOCOL, domain=DOMAIN, path="", anchor=""):
    url = URL.substitute(protocol=protocol, domain=domain, path=path, anchor=anchor)
    return requests.get(url)


def look_for_articles(soup, article_type):
    path_pair_title = dict()
    for article in soup.find_all("article"):
        if article.find("span", class_="c-meta__type").string != article_type:
            continue
        article_of_type = article.find("a")
        path_pair_title[article_of_type.get("href")] = article_of_type.string
    return path_pair_title


def get_file_name(title_of_article):
    file_name = title_of_article.translate(str.maketrans("", "", string.punctuation))
    file_name = file_name.replace(" ", "_")
    file_name += ".txt"
    return file_name


def create_files(dict_articles, directory=""):
    for path, title in dict_articles.items():
        r = get_response(path=path)
        if not r:
            print(r.status_code, r.url)
            continue
        soup_article = BeautifulSoup(r.content, "html.parser")
        with open("{}{}".format(directory, get_file_name(title)), "w", encoding="UTF-8") as file:
            file.write(soup_article.find("div", class_="c-article-body main-content").get_text())


def main():
    number_of_pages = int(input()) + 1
    type_of_articles = input()
    for n in range(1, number_of_pages):
        r = get_response(path=PATH_ARTICLES_SORTED.substitute(number=n))
        if not r:
            print(r.status_code, r.url)
            continue
        soup_articles_sorted = BeautifulSoup(r.content, "html.parser")
        dict_articles = look_for_articles(soup_articles_sorted, type_of_articles)

        # I wouldn't create a new directory if there isn't any article of the type selected
        # if not dict_articles:
        #     continue

        dir_name = f"Page_{n}"
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        create_files(dict_articles, directory=f"{dir_name}/")


if __name__ == "__main__":
    main()
