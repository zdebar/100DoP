from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

# Use a CSS selector to select anchors inside the "titleline" class

articles = soup.select(".titleline a")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_upvotes_index = article_upvotes.index(max(article_upvotes))


# print(articles)
print(article_texts[highest_upvotes_index])
print(article_links[highest_upvotes_index])
print(article_upvotes[highest_upvotes_index])
