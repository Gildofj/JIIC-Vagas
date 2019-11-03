# -*- coding: utf-8 -*-
import scrapy


class VagasSpider(scrapy.Spider):
    name = 'Vagas'
    #allowed_domains = ['https://www.manager.com.br/empregos-desenvolvedor-javascript/']
    start_urls = ['https://www.manager.com.br/empregos-desenvolvedor-javascript//']

    def parse(self, response):
       items = response.xpath(
           '//div[@id="lista-resultado-busca-vagas"]/article[@class="vaga hlisting"]/header/h2'
       )

       for item in items:
           url = item.xpath('./a/@href').extract_first()
           yield scrapy.Request(url=url, callback=self.parse_detail)

       next_page = response.xpath('//div[contains(@class, "pagination pagination-centered hidden-print")]//a[@rel="next nofollow"]/@href')
       if next_page:
           yield  scrapy.Request(
               url=next_page.extract_first(), callback=self.parse
               )

    def parse_detail(self, response):
        title = response.xpath('//header[@class="page-header"]/meta').extract_first()
        city = response.xpath('//dl[@class="location adr"]/dd[@class="clear-none"]/span').extract_first()
        salary = response.xpath('//div[@class="sub-item"]/dl/dd/meta').extract_first()
        description = response.xpath('//div[@class="description"]/p').extract_first()
        yield{
            'Titulo': title,
            'Cidade': city,
            'Salario': salary,
            'Descricao': description,
            }