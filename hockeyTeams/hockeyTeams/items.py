# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_extra(value):
    return value.strip()

class HockeyteamsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(input_processor = MapCompose(remove_tags, remove_extra), output_processor = TakeFirst())
    year = scrapy.Field(input_processor = MapCompose(remove_tags, remove_extra), output_processor = TakeFirst())
    wins = scrapy.Field(input_processor = MapCompose(remove_tags, remove_extra), output_processor = TakeFirst())
    losses = scrapy.Field(input_processor = MapCompose(remove_tags, remove_extra), output_processor = TakeFirst())