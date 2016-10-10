# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

#!/usr/bin/env python

#import scraperwiki
#import requests
#import lxml.html
#import datetime

print("test")

#demorgen.be
html = scraperwiki.scrape("http://www.demorgen.be")
root = lxml.html.fromstring(html)

data = {}

timestamp = {
    'source': 'timestamp',
    'rank': 0,
    'url': '',
    'title': datetime.datetime.utcnow().isoformat(),
    'key': 'timestamp'
    }
scraperwiki.sql.save(['key'], timestamp)

#demorgen.be
for ind,el in enumerate(root.cssselect(".widget-most-recent ol li a"), 1):
    if ind > 5: break
    key = 'demorgen' + str(ind)
    
    url = el.attrib['href']
    
    data[ind] = {
        'source': 'demorgen.be',
        'rank': ind,
        'url': el.attrib['href'],
        'title': root.cssselect(".widget-most-recent ol li a span")[ind-1].text,
        'key': key
        }
    scraperwiki.sql.save(['key'], data[ind])

#hln.be
html = scraperwiki.scrape("http://www.hln.be")
root = lxml.html.fromstring(html)

data = {}

for ind,el in enumerate(root.cssselect("#hdr_hvdn_top_list a"), 1):
    key = 'hln' + str(ind)
    data[ind] = {
        'source': 'hln.be',
        'rank': ind,
        'url': 'http://www.hln.be' + el.attrib['href'],
        'title': el.text.strip(),
        'key': key
        }
    scraperwiki.sql.save(['key'], data[ind])

#standaard.be
html = scraperwiki.scrape("http://www.standaard.be")
root = lxml.html.fromstring(html)

data = {}

for ind,el in enumerate(root.cssselect("#most-read ol li a"), 1):
    key = 'standaard' + str(ind)
    data[ind] = {
        'source': 'standaard.be',
        'rank': ind,
        'url': el.attrib['href'],
        'title': el.text.strip(),
        'key': key
        }
    scraperwiki.sql.save(['key'], data[ind])
    
#knack.be
html = scraperwiki.scrape("http://www.knack.be")
root = lxml.html.fromstring(html)

data = {}

for ind,el in enumerate(root.cssselect(".most-read.widget ol li a"), 1):
    key = 'knack' + str(ind)
    data[ind] = {
        'source': 'knack.be',
        'rank': ind,
        'url': el.attrib['href'],
        'title': el.attrib['title'],
        'key': key
        }
    scraperwiki.sql.save(['key'], data[ind])
    
#nieuwsblad.be
html = scraperwiki.scrape("http://www.nieuwsblad.be")
root = lxml.html.fromstring(html)

data = {}

for ind,el in enumerate(root.cssselect('[data-mht-widget="list-|-most-read---overall"] .widget--most-read a'), 1):
    key = 'nieuwsblad' + str(ind)
    data[ind] = {
        'source': 'nieuwsblad.be',
        'rank': ind,
        'url': el.attrib['href'],
        'title': root.cssselect('[data-mht-widget="list-|-most-read---overall"] .widget--most-read a h1')[ind-1].text.strip(),
        'key': key
        }
    scraperwiki.sql.save(['key'], data[ind])
    

#deredactie.be
html = scraperwiki.scrape("http://deredactie.be/cm/vrtnieuws")
root = lxml.html.fromstring(html)

data = {}

for ind,el in enumerate(root.cssselect('.divider.list.boxedlist .contentitem h3 a'), 1):
    key = 'deredactie' + str(ind)
    data[ind] = {
        'source': 'deredactie.be',
        'rank': ind,
        'url': 'http://www.deredactie.be' + el.attrib['href'],
        'title': el.attrib['title'].strip(),
        'key': key
        }
    scraperwiki.sql.save(['key'], data[ind])

