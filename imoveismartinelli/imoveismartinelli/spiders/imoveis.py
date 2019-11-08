# -*- coding: utf-8 -*-
import scrapy
from decimal import Decimal
import re
from imoveismartinelli.items import ImoveismartinelliItem


class ImoveisSpider(scrapy.Spider):
    name = 'imoveis'

    def __init__(self):
        self.allowed_domains = ['www.imoveismartinelli.com.br']

    def start_requests(self):
        self.start_urls = [
            'https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=',
            'https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/',
        ]
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        divs = response.xpath('//div[@class="item col-sm-6 col-md-4 col-lg-3"]')
        for div in divs:
            price = div.xpath(".//div[@class='price']//span[@class='price_lv']/text()")
            area = div.xpath('.//ul[@class="amenities"]//li[1]/text()').extract()
            id = div.xpath('.//p[@class="corta_desc"]//strong/text()').extract()
            if price:
                locacao = price[0].extract()
                venda = price[1].extract()
                yield ImoveismartinelliItem({
                    "price": '',
                    "locacao": self.decimal_price(locacao),
                    "venda": self.decimal_price(venda),
                    "area": self.decimal_area(area[0]),
                    "id": id[0],
                })
            else:
                price = div.xpath('.//div[@class="price"]//span/text()').extract()
                yield ImoveismartinelliItem({
                    "price": self.decimal_price(price[0]),
                    "area": self.decimal_area(area[0]),
                    "id": id[0]
                })
        next_page = response.xpath('//div[@class="pagination"]//li//a//@href')
        if next_page:
            next_page_url = self.start_urls[0] + next_page[-1].extract()
            # next_page_url = 'https://' + self.allowed_domains[0] + '/' + next_page[-1].extract()
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def decimal_price(self, value):
        price = re.sub('[\s.$a-zA-Z]', '', value).replace(',', '.')
        try:
            price = float(price)
        except:
            return None
        return Decimal(float(price))

    def decimal_area(self, value):
        area = re.sub('[\s,a-zA-Z]', '', value)
        try:
            area = float(area)
        except:
            return None
        return Decimal(float(area))
