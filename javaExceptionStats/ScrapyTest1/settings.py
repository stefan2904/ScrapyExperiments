# Scrapy settings for ScrapyTest1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ScrapyTest1'

SPIDER_MODULES = ['ScrapyTest1.spiders']
NEWSPIDER_MODULE = 'ScrapyTest1.spiders'

ITEM_PIPELINES = {  'ScrapyTest1.pipelines.Scrapytest1Pipeline': 300 }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ScrapyTest1 (+http://www.yourdomain.com)'
