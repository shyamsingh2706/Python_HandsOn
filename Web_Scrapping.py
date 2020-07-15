import requests
import bs4
import lxml

base_url =  'http://quotes.toscrape.com/page/{}/'
result = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(result.text,'lxml')

''' Pick all Authors from first page'''

author_list=[]
authors = soup.select('.author')
for j in authors:
    author_name = j.getText()
    author_list.append(author_name)

print(f' Author details from first page are : {author_list}')

''' Pick all Quotes from first page'''

quotation_list=[]
quotes=soup.select('.text')
for j in quotes:
    quote = j.getText()
    quotation_list.append(quote)

print(f' All Quotations listed on first page are : {quotation_list}')

''' Pull Top 10 Tags on first page '''

Top_10_tag_list =[]
top_10_Tags = soup.select('.tag-item')
for j in top_10_Tags:
    tag = j.getText()
    print(tag)
    # Top_10_tag_list.append(tag)

# print(f' Top 10 tags listed on first page are : {Top_10_tag_list}')

''' Browse across all pages and identify unique author'''

page = 1
All_author_set = set()
while True:

    pages = requests.get(base_url.format(page))
    soup = bs4.BeautifulSoup(pages.text, 'lxml')
    End_of_pages_check = soup.select('.col-md-8')

    if ('No quotes found!' in (End_of_pages_check[1].text) ):
        break
    else:
        page += 1
        authors = soup.select('.author')
        for j in authors:
            author_name = j.getText()
            All_author_set.add(author_name)
        continue

print(f' Unique Author List across all Pages are : {All_author_set}')