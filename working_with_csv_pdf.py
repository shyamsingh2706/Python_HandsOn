import csv
import requests
import wget
import PyPDF2
import re

''' Program to read csv
fetch google drive link by fetching and concatenating diagonal letters of each line of csv
download pdf from google drive
read pdf and find phone number inside pdf
'''

f = open('C:\\Users\\shyam\\Downloads\\find_the_link.csv',encoding ='utf8')
csv_reader = csv.reader(f)
data_lines = list(csv_reader)

loop = 0
url=''

for line in data_lines:
    url += line[loop]
    loop += 1

print( f"google drive url is {url}")

# way to download files from a given url
# wget.download(url,'C:\\Users\\shyam\\Downloads\\Find_the_Phone_Number.pdf')
## OR
# r = requests.get(url, stream=True)
# with open("C:\\Users\\shyam\\Downloads\\Find_the_Phone_Number.pdf", "wb") as pdf:
#     for chunk in r.iter_content(chunk_size=1024):
#         # writing one chunk at a time to pdf file
#         if chunk:
#             pdf.write(chunk)

# read PDF and extract all pages from it
all_text = ''
pdf_file = open('C:\\Users\\shyam\\Downloads\\Find_the_Phone_Number.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
for pages in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pages)
    page_text = page.extractText()
    all_text = all_text + '  ' + page_text
pdf_file.close()

# print(all_text)
# Find phone number in pdf text
pattern = re.compile(r'\d{3}[.-:]\d{3}[.-:]\d{4}')
matches = pattern.finditer(all_text)
for match in matches:
    print(match)

