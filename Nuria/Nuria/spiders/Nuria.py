import scrapy
from scrapy.crawler import CrawlerProcess



class Children(scrapy.Spider):
    name = 'children'
    allowed_domains = ['nuriakenya.com']
    start_urls = ['https://nuriakenya.com/product-category/books/childrens-books-books/']

    def parse (self, response):
        for item in response.css('div.product-element-bottom.product-information'):
               yield{
                    'book_name': item.css('h3.wd-entities-title>a::text').get(), 
                    'book_category':item.css('div.wd-product-cats>a::text').get(),
                    'currency': item.css('span.woocommerce-Price-currencySymbol::text').get(),
                    'book_price': item.css('span.woocommerce-Price-amount.amount::text').get(), 
                    'book_link': response.css('a.product-image-link::attr(href)').get() 
                    }

        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
            

process = CrawlerProcess(settings={
     'FEED_URI':'children.csv',
     'FEED_FORMAT':'csv',
})
process.crawl(Children)
process.start()