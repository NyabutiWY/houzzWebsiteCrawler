# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import re


class FormatDataPipeline:
    def process_item(self, item, spider):

        if 'phone_number' in item:
            item['phone_number'] = self.format_mobile_number(
                item['phone_number'])

        if 'rating' in item:
            item['rating'] = float(item['rating'])
        if 'reviews' in item:
            # Remove non-numeric characters
            item['reviews'] = int(re.sub('[^\d]', '', item['reviews']))

        return item

    def format_mobile_number(self, number):

        parts = re.findall(r'\d+', number)
        if len(parts) == 3:
            return f'({parts[0]}) {parts[1]}-{parts[2]}'
        else:
            return number
