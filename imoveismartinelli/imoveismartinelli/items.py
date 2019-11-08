import scrapy


class ImoveismartinelliItem(scrapy.Item):
    price = scrapy.Field()
    area = scrapy.Field()
    id = scrapy.Field()
    locacao = scrapy.Field()
    venda = scrapy.Field()
