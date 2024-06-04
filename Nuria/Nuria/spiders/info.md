# css selectors

allbooks = response.css('div.product-wrapper')
next_page = response.css('a.next.page-numbers::attr(href)').get()

book_name = response.css('h3.wd-entities-title>a::text').get() 
book_author = 
book_category = response.css('div.wd-product-cats>a::text').get()
currency = response.css('span.woocommerce-Price-currencySymbol::text').get()
book_price = response.css('span.woocommerce-Price-amount.amount::text').get() 
book_link = response.css('a.product-image-link::attr(href)').get()