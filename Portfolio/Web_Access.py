from selenium import webdriver
import bs4
import re
import requests
#import browsercookie
#import json
import urllib.request
from pprint import pprint

# Access a site that requires javascript, and wait for an element to be loaded (optional)
def accessWithJavascript(direccion, waittime=12):

    driver = webdriver.PhantomJS()
    #print(timestamp())
    driver.implicitly_wait(waittime)
    driver.get(direccion)

    # page_source gets page after rendering is complete
    page = bs4.BeautifulSoup(driver.page_source, "lxml")

    #driver.save_screenshot('screenc.png')
    driver.quit()

    return str(page)

def accessWithBs(direccion):
    page = requests.get(direccion)
    attempts = 0
    while (page.status_code!=200) and (attempts < 10):
        #error occured during download, try again
        page = requests.get(direccion)
        attempts+=1
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    #data = soup.find('span', attrs={'id': 'yfs_l84_'.format(name)})
    #return soup.text
    return soup.prettify()

'''def accessAndFindValueWithBs(direccion, tag):
    r = requests.get(direccion)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    pattern = re.compile(tag)
    print(pattern)

    title = soup.find('strong', text=pattern)
    print(title)
    row = title.parent.parent
    cells = row.find_all('td')[1:] #exclude the <td> with 'Net Income'

    values = [ c.text.strip() for c in cells ]
    return values'''

# Try to access url up to 10 times
def access(direccion):
    page = read(direccion)
    attempts = 0
    while (page == "<COULDN'T ACCESS WEBSITE>") and (attempts < 10):
        page = read(direccion)
        attempts += 1
    return page

# Read page with urllib
def read(direccion):
    try:
        stream = urllib.request.urlopen(direccion)
        page = stream.read()
        stream.close()
        return page

    except IOError:
        return "<COULDN'T ACCESS WEBSITE>"


def obtenerCookies(direccion):
    r = requests.get(direccion)
    c = r.headers
    i = c.items()
    #print(c.values())
    #print(c.items())

    for name, value in i:
        if name == "Set-Cookie":
            # print(value)
            endIndex = value.find(";")
            # print(value[:endIndex])
            return str(value[:endIndex+1])
    return str(0)

#print(accessWithBs("https://ih.advfn.com/stock-market/NYSE/gen-electric-GE/financials?btn=start_date&start_date=23&mode=annual_reports"))