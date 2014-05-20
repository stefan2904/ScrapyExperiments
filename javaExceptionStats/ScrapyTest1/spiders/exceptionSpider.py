from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider
from ScrapyTest1.items import Scrapytest1Item
from scrapy.http import Request
from scrapy import log
import json

class ExceptionspiderSpider(CrawlSpider):
    name = 'exceptionSpider'
    allowed_domains = ['docs.oracle.com']
    start_urls = ['http://docs.oracle.com/javase/7/docs/api/java/lang/Exception.html']
    
    # root node
    tree = Scrapytest1Item()
     
    def parse(self, response):
        log.msg("outer callback called ...", level=log.DEBUG)
        return self.parse_child(response, self.tree)
        
    def parse_child(self, response, parent):
        log.msg("parsing ...", level=log.DEBUG)
        
        sel = Selector(response)
        refs = sel.xpath('//dl[dt/text()[contains(., "Direct Known Subclasses")]]/dd/a')
        
        ret = []
        childs = []
        
        for s in refs:            
            i= Scrapytest1Item()
            
            i['text'] = s.xpath('./text()').extract()[0]
            
            url = s.xpath('./@href').extract()[0]
            i['href'] = url.split('../')[url.find('/')]
            
            childs.append(i)
            
            absUrl = "http://docs.oracle.com/javase/7/docs/api/" + i['href'] 
                
            ret.append(Request(absUrl))
            #ret.append(Request(absUrl, lambda response, parent=i: self.parse_child(response, parent) ))
            log.msg("added "+  absUrl, level=log.DEBUG)
            
        parent['childs'] = childs
        log.msg("returning number of requwsts ..." +str(len(ret)), level=log.DEBUG)        
        
        return ret

