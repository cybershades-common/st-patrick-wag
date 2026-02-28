from django.db import models
from wagtail.images.models import Image
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from home.models import HeroAbstract
from pages.fields import generalpage_stream_fields,blog_stream_fields
from wagtail.fields import StreamField, RichTextField

class Category(models.Model):
    title = models.CharField(null=True,max_length=255,blank=False)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    weight = models.IntegerField(default=100,blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'

class BlogCategories(Orderable):
    category = models.ForeignKey(
        "blog.Category",
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    page = ParentalKey('Blog', related_name='blog_category')


# Create your models here.
class Blog(ClusterableModel):
    title = models.CharField(null=True,max_length=255,blank=False)
    slug = AutoSlugField(populate_from='title',editable=True, null=True,max_length=500)
    image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    author_name = models.CharField(null=True,blank=True)
    release_date = models.DateField()
    status = models.BooleanField(default=True)
    body = StreamField(blog_stream_fields,null=True,blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        FieldPanel('image'),
        FieldPanel('author_name'),
        FieldPanel('release_date'),
        FieldPanel('status'),
        InlinePanel('blog_category', label='Categories', panels=[
            FieldPanel('category'),
        ]),
        FieldPanel('body'),


    ]
    class Meta:
        verbose_name = 'Blog'


class BlogpageHero(HeroAbstract):
    page = ParentalKey('BlogIndexPage', related_name='blogpage_hero')

class BlogIndexPage(Page):
    body = StreamField(generalpage_stream_fields,null=True,blank=True)
    """
    We'll render blog items from SendHQ with JSON.
    """
    template = 'pages/blog_index.html'
    class Meta:
        verbose_name = "Blog Index Page"

    def get_hero_image(self):
        if self.get_hero():
            return self.get_hero()[0]

        return False


    def get_hero(self):
        if self.blogpage_hero.all():
            return self.blogpage_hero.all()
        else:
            return []