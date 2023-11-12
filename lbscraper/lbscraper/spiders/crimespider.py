import scrapy


class CrimespiderSpider(scrapy.Spider):
    name = "crimespider"
    allowed_domains = ["www.longbeach.gov"]
    start_urls = ["https://www.longbeach.gov/police/crime-info/crime-statistics/"]

    def parse(self, response):
        table_rows = response.css("table tr")
        
        # eliminate header row
        rows = table_rows[1:]

        # get all links for monthly stats from table data
        # links = []

        for row in rows:
            all_years = row.css("td a::attr(href)").getall()
            
            # the first url it gets is some accidental repeat of a different year
            # so get rid of the first entry
            all_years.pop(0)

            # pull each url from the list of 4 or 5 to put in links list
            for month in all_years:
                yield {"url" : month}


