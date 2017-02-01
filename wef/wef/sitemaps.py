from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class StaticViewSitemap(sitemaps.Sitemap):

    priority = 0.5
    changefreq = 'always'

    def items(self):
        return ['home',
                'postlist',
                'join_us',
                ]

    def location(self, item):
        return reverse(item)
