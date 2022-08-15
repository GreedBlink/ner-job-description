## Scrap 

In this project are two spiders: 

- `./scrap/spiders/remotar_spider.py`
- `./scrap/spiders/catho_spider.py`

To run the spiders:

```
scrapy crawl remotar -O output/remotar.json
scrapy crawl catho -O output/catho.json
```


The above command generates two files, `remotar.json` and `catho.json` in `output` folder, which are files with job objects collected from scraped spiders.