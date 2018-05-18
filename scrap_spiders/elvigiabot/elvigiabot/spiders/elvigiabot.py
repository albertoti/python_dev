# -*- coding: utf-8 -*-
import scrapy


class ElvigiabotSpider(scrapy.Spider):
	name = 'elvigiabot'
	allowed_domains = ['www.elvigia.net/noticias']
	start_urls = ['http://www.elvigia.net/noticias/']
	custom_settings = {
		'FEED_URI'	:	'elvigia.csv'
	}

	def parse(self, response):
		horas	=	response.css('.hora::text').extract()
		titulos	=	response.css('.cont h5 a::text').extract()
		#resumen	=	response.xpath('.//div[contains(@class,"nota620_apaisada")]/div/p/span/following-sibling::text()').extract()
		links	=	response.css('.cont h5 a::attr(href)').extract()

		for item in zip(horas,titulos,links):
			scrap_items	=	{
				'hora':item[0],
				'titulo':item[1],
				#'resumen':item[2],
				'link':item[2],
			}
			yield scrap_items