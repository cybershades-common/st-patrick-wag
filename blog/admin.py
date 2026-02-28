from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from .models import BlogIndexPage

BlogIndexPage.content_panels = Page.content_panels + [
    InlinePanel('blogpage_hero', label='Hero Images', panels=[
        FieldPanel('title'),
        FieldPanel('text'),
    ],max_num=1),
    FieldPanel('body'),
]
