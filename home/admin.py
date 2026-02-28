from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel

from .models import HomePage

HomePage.content_panels = [
    FieldPanel('title', classname='title'),
    MultiFieldPanel([
        InlinePanel('homepage_hero', label='Hero Images', panels=[
            #FieldPanel('title'),
            FieldPanel('image'),
            FieldPanel('background_video_url'),
            FieldPanel('popup_video_url'),
            FieldPanel('popup_button_label'),
        ],max_num=1),
        FieldPanel('left_static_text'),
        FieldPanel('right_static_text'),
        FieldPanel('right_dynamic_text'),
    ]),    
    FieldPanel('body'),
]
