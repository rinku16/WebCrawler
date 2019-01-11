import scrapy

class LinkCheckerSpider(scrapy.Spider):
    name = 'link'
    allowed_domains = ['www.copperpodip.com']
    start_urls = ['https://www.copperpodip.com']
        

    def parse(self, response):
        print(response.url)
        page_title = response.url.split('/')[2:]
        filename = '%s.html' % page_title
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        # Get all the <a> tags
        a_selectors = response.xpath("//a")
        # Loop on each tag
        for selector in a_selectors:
            # Extract the link text
            text = selector.xpath("text()").extract_first()
            # Extract the link href
            link = selector.xpath("@href").extract_first()
            # Create a new Request object
            request = response.follow(link, callback=self.parse)
            # Return it to the crawler
            yield request

        
  	  