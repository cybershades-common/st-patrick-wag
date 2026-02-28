from django.db import models

from wagtail.models import Page
from wagtail.images.models import Image
from pages.fields import homepage_stream_fields
from wagtail.fields import StreamField
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtailseo.models import SeoMixin

class PageAbstract(SeoMixin, models.Model):
    exclude_from_sitemap = models.BooleanField(default=False,help_text="If checked, this page will be excluded from sitemap.xml and not submitted to search engines.")
    no_index = models.BooleanField(
        default=False,
        help_text="Check this to add a 'noindex' meta tag so search engines do not index this page."
    )
    exclude_from_search = models.BooleanField(default=False,help_text="If checked, this page will be excluded from the site search results.")

    promote_panels = SeoMixin.seo_panels

    def get_sitemap_urls(self, request):
        # Exclude this specific page
        if self.exclude_from_sitemap:
            return []

        return super().get_sitemap_urls(request)

    settings_panels = [
        FieldPanel('exclude_from_sitemap'),
        FieldPanel('exclude_from_search'),
        FieldPanel('no_index'),
    ]

    class Meta:
        abstract = True

class HeroAbstract(models.Model):
    pre_title = models.CharField(null=True,blank=True,max_length=255)
    title = models.CharField(null=True,blank=True,max_length=255)
    text = models.TextField(null=True,blank=True)
    image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    background_video_url = models.URLField(null=True,blank=True,help_text="mp4 video")
    popup_video_url = models.URLField(null=True,blank=True,help_text="embeded video url",max_length=1000)
    popup_button_label = models.CharField(null=True,blank=True,max_length=500)
    button_label = models.CharField(null=True,blank=True,max_length=500)
    button_url = models.URLField(null=True,blank=True)

    class Meta:
        abstract = True

class HomepageHero(HeroAbstract):
    page = ParentalKey('HomePage', related_name='homepage_hero')

class HomePage(Page):
    left_static_text= models.CharField(null=True,blank=True,max_length=255)
    right_static_text= models.CharField(null=True,blank=True,max_length=255)
    right_dynamic_text= models.CharField(null=True,blank=True,max_length=255)
    body = StreamField(homepage_stream_fields, null=True, blank=True)

    template = 'home/home_page.html'
    class Meta:
        verbose_name = 'Home Page'

    def get_hero(self):
        if self.homepage_hero.all():
            return self.homepage_hero.all()
        else:
            return False


    def get_child_pages(self):
        return self.get_children().live().filter(show_in_menus=True)
