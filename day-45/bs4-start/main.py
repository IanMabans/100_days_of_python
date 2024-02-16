from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_titles = []
article_links = []
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = []
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

max_points_index = article_upvotes.index(max(article_upvotes))
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)








# # import lxml
#
# with open('website.html') as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.name)
# # print(soup.prettify())
#
# print(soup.p)
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.get('href'))
#
# heading = soup.find(name='h1', id='name')
# print(heading)
#
# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.getText())
# name = soup.select_one(selector='#name')
# print(name)
#
# headings =soup.select('.heading')
# print(headings)
