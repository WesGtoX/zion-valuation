# -*- coding: utf-8 -*-
import scrapy
from imoveismartinelli.items import ImoveismartinelliItem


class ImoveisSpider(scrapy.Spider):
    name = 'imoveis'
    allowed_domains = ['imoveismartinelli.com.br']
    url = 'https://www.imoveismartinelli.com.br'
    start_urls = [url + '/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=']

    def parse(self, response):
        imoveis = ImoveismartinelliItem({
            "price": response.xpath('//div[@class="price"]/span/text()').extract_first(),
            "area": response.xpath('//ul[@class="amenities"]/li/text()').extract_first(),
            "id": response.xpath('//p[@class="corta_desc"]/strong/text()').extract_first(),
        })
        print(imoveis)
        return imoveis
