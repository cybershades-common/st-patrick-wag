from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from .models import HomePage

HomePage.content_panels = [
    FieldPanel('title', classname='title'),
    MultiFieldPanel([
        FieldPanel('hero_section'),
    ], heading="Hero Section"),
    FieldPanel('body'),
]
