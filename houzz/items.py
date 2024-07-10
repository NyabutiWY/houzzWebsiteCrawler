import scrapy


class BusinessDetailsItem(scrapy.Item):
    url = scrapy.Field()
    rating = scrapy.Field()
    about_us = scrapy.Field()
    reviews = scrapy.Field()
    category = scrapy.Field()
    business_name = scrapy.Field()
    phone_number = scrapy.Field()
    website_link = scrapy.Field()
    address = scrapy.Field()
    typical_job_cost = scrapy.Field()
