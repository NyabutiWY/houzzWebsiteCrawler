import scrapy
from houzz.items import BusinessDetailsItem


class HouzzSpider(scrapy.Spider):
    name = "houzzSpider"
    allowed_domains = ["houzz.com"]
    start_urls = ["https://www.houzz.com/professionals/"]

    def parse(self, response):
        services = response.css(
            'div.br-carousel-item__photo-container a::attr(href)').getall()

        for service_url in services:
            yield response.follow(service_url, callback=self.parse_service_page)

    def parse_service_page(self, response):
        service_page_links = response.css(
            'li.hz-pro-search-results__item a::attr(href)').getall()

        for service_url in service_page_links:
            yield response.follow(service_url, callback=self.parse_profile_page)

        next_page = response.css(
            "a.hz-pagination-link--next::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse_service_page)

    def parse_profile_page(self, response):
        item = BusinessDetailsItem()

        item['url'] = response.url
        item['rating'] = response.css(
            'span.hz-star-rate__rating-number::text').get()
        item['about_us'] = response.css('div.kimeJn::text').get()
        item['reviews'] = response.css(
            'span.hz-star-rate__review-string::text').get()

        item['business_name'] = response.xpath(
            "//div[@data-container='Business Details']//h3[text()='Business Name']/following-sibling::p/text()"
        ).get()
        item['phone_number'] = response.xpath(
            "//div[@data-container='Business Details']//h3[text()='Phone Number']/following-sibling::p/text()"
        ).get()
        item['website_link'] = response.xpath(
            "//div[@data-container='Business Details']//div[@data-component='Website']//a/@href"
        ).get()
        item['address'] = response.xpath(
            "//div[@data-container='Business Details']//h3[text()='Address']/following-sibling::div//p/span/text()"
        ).getall()
        item['typical_job_cost'] = response.xpath(
            "//div[@data-container='Business Details']//h3[text()='Typical Job Cost']/following-sibling::p/text()"
        ).get()

        yield item
