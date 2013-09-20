from django.contrib.syndication.views import Feed
from .models import Post

class LatestPostsFeed(Feed):
    '''Feed for latest 10 blog entries'''
    
    title = "Wavrin.com Feed"
    link = "feed"
    description = "Latest Blog Entries"

    def items(self):
        # Grab our posts from the model and order them by date
        return Post.objects.all().order_by('-id')[:10]

    def item_title(self, item):

        return item.title

    def item_description(self, item):

        return item.text

    def item_link(self, item):

        return "http://www.wavrin.com/%s" % item.slug