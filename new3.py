import scrapy

class LinkCheckerSpider(scrapy.Spider):
    #name of the spider which is used in command 'scrapy crawl link' in anaconda prompt
    name = 'link'
    #only this domain is allowed
    allowed_domains = ['www.copperpodip.com']
    #all the links attached to this start_urls are visited and there html page is downloaded
    start_urls = ['https://www.copperpodip.com']
        

    def parse(self, response):
        print(response.url) #print url on console of anaconda prompt
        page_title = response.url.split('/')[2:] #to make the file name as split make list element of url after spliting with /
        filename = '%s.html' % page_title
        with open(filename, 'wb') as f:         #line 14-18 is to save the visited downloaded html page to local system
            f.write(response.body)
        self.log('Saved file %s' % filename)
        # Get all the <a> tags
        a_selectors = response.xpath("//a")   #line 20-30 nake recursive call to send response with url in start_urls
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

        
  	  
