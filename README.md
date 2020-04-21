# harvard_online_freecourses
 Simple tool to get free courses of Harvard University
 
 Prerequisites:
 - Python
 - Scrapy
 
 How to use:
 1) To crawl, just go to root folder and enter the command:
 scrapy crawl freecourses
 
 2) To crawl and export to file, use following command:
  scrapy crawl freecourses -o filename.*
  
  where:
  - filename is desired export file
  - (*) is extension. Scrapy support export to *.csv; *.json and *.xml
  
  For example: scrapy crawl freecourses -o harvardfreecourses.json
