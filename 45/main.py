from bs4 import BeautifulSoup

with open("./46/website.html", 'r', encoding='utf-8-sig') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)
print(soup.p) # prints first paragraph
all_anchor_tags = soup.find_all(name="a") # výběr ze všech anchor tabs
print(all_anchor_tags)

for tag in all_anchor_tags: # tisk jen textu z anchor tags
    print(tag.getText())

for tag in all_anchor_tags: # tisk jen links
    print(tag.get("href"))

heading = soup.find(name = "h1", id = "name") # najde první h1 s danými parametry (for class use class_=)
print(heading)

company_url = soup.select_one(selector = "p a") # specifikace toho co hledám 
print(company_url)

headings = soup.select(".heading") # filtrovat dle
print(headings)