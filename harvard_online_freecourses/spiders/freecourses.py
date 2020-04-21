# -*- coding: utf-8 -*-
import scrapy


class FreecoursesSpider(scrapy.Spider):
    name = 'freecourses'
    allowed_domains = ['online-learning.harvard.edu']
    start_urls = ['https://online-learning.harvard.edu/catalog/free']
    base_url = 'https://online-learning.harvard.edu'

    def parse(self, response):
        courses_path = '//ul[@class="course-grid"]/li'
        courses = response.xpath(courses_path)
        for course in courses:
            course_name = course.xpath('.//a[starts-with(@href, "/course/")]/text()').get()
            course_category = course.xpath('.//a[starts-with(@href, "/subject/")]/text()').get()
            course_duration = course.xpath('.//div[@class="field field-name-field-duration"]/text()').get()
            course_link = course.xpath('.//a[starts-with(@href, "/course/")]/@href').get()
            if course_link is None:
                course_link = self.base_url
            else:
                course_link = self.base_url + course_link

            yield {
                'course_name': course_name,
                'course_category': course_category,
                'course_duration': course_duration,
                'course_link': course_link
            }

        next_page = response.xpath('//li[@class="pager-next"]')
        # print(next_page)
        if next_page:
            next_page_url = next_page.xpath('.//a/@href').get()
            # print(next_page_url)
            yield response.follow(url=next_page_url, callback=self.parse)
