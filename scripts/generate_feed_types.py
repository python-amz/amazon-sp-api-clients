import requests
from lxml import etree

text = requests.get('https://developer-docs.amazon.com/sp-api/docs/feed-type-values').text
html: etree.ElementTree = etree.HTML(text)
elements = html.xpath('//div[@id="content-container"]//div[contains(@class,"markdown-body")]/*')
heading: etree.Element
table: etree.Element

groups = []
for heading, table in zip(elements[:-1], elements[1:]):
    if not (heading.tag == 'h2' and table.tag == 'div'):
        continue
    group_name = ''.join(heading.xpath('./div[@class="heading-text"]//text()'))
    group_name = group_name.replace(' ', '_').lower()
    group_name = group_name.removesuffix('_feed').removesuffix('_feeds')

    feeds = []
    for tr in table.xpath('.//tbody/tr'):
        feed_name = ''.join(tr.xpath('./td[1]/p[2]/text()'))
        feed_name = feed_name.split(': ')[1]
        feeds.append(feed_name)
    groups.append((group_name, feeds))

print('class FeedTypeGroup(IntEnum):')
for index, v in enumerate(groups):
    name, feeds = v
    print(f'    {name} = {index + 1}')

print('class ReportType(__FeedTypeDefinition, Enum):')

for group_index, v in enumerate(groups):
    name, feeds = v
    for feed_index, feed in enumerate(feeds):
        print(f"    {feed.lower()} = {group_index + 1}, {feed_index + 1}, '{feed}'")
