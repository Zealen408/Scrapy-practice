from urllib.parse import urlparse
import scrapy
from hockeyTeams.items import HockeyteamsItem
from scrapy.loader import ItemLoader


class HockeySpider(scrapy.Spider):
    name = 'hockey'
    allowed_domains = ['www.scrapethissite.com']
    start_urls = ['http://www.scrapethissite.com/pages/forms/']

    
    def parse(self, response):
        for team in response.css('tr.team'):
            l = ItemLoader(item= HockeyteamsItem(), selector=team)

            l.add_css('name', 'td.name')
            l.add_css('year', 'td.year')
            l.add_css('wins', 'td.wins')
            l.add_css('losses', 'td.losses')

            yield l.load_item()

        next_link = response.xpath('//a[@aria-label="Next"]').attrib['href']
        if next_link is not None:
            next_page = response.urljoin(next_link)
            yield scrapy.Request(next_page, callback=self.parse)