from django.db import models
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.images.models import Image
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from django.utils.translation import gettext_lazy as _
from wagtailmenus.models import AbstractMainMenuItem, AbstractFlatMenuItem

class CustomMainMenuItem(AbstractMainMenuItem):
    """A custom menu item model to be used by ``wagtailmenus.MainMenu``"""

    menu = ParentalKey(
        'wagtailmenus.MainMenu',
        on_delete=models.CASCADE,
        related_name="custom_main_menu_items", # important for step 3!
    )
    image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 

    # Also override the panels attribute, so that the new fields appear
    # in the admin interface
    panels = AbstractMainMenuItem.panels + [
        FieldPanel('image'),
    ] 

class CustomFlatMenuItem(AbstractFlatMenuItem):
    """A custom menu item model to be used by ``wagtailmenus.FlatMenu``"""

    menu = ParentalKey(
        'wagtailmenus.FlatMenu',
        on_delete=models.CASCADE,
        related_name="custom_flat_menu_items", # important for step 3!
    )
    image = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 

    # Also override the panels attribute, so that the new fields appear
    # in the admin interface
    panels = AbstractFlatMenuItem.panels + [
        FieldPanel('image'),
    ]



@register_setting
class ExtraStyleSettings(BaseSiteSetting):
    extra_css = models.TextField("CSS Overrides", blank=True)
    extra_js = models.TextField("JavaScript Overrides", blank=True)

    class Meta:
        verbose_name = "Global CSS/JS"
        verbose_name_plural = "Global CSS/JS"


@register_setting
class GlobalAnnouncement(BaseSiteSetting):
    status = models.BooleanField(default=False,blank=True,help_text="Check to show alert message",verbose_name="Show alert")
    text = RichTextField(blank=True,null=True,verbose_name="Text")
    
    class Meta:
        verbose_name = "Global Announcement"
        verbose_name_plural = "Global Announcement"        


@register_setting
class AdminSettings(BaseSiteSetting):
    admin_logo = models.ForeignKey(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    ) 

    class Meta:
        verbose_name = "Admin Setting"
        verbose_name_plural = "Admin Settings"        

@register_setting
class SocialLinks(BaseSiteSetting):
    facebook_url = models.URLField(
        blank=True,
        help_text="Enter the full Facebook profile or page URL."
    )
    facebook_icon = models.CharField(
        max_length=100,
        blank=True,
        help_text='Font Awesome icon tag for Facebook (e.g. <i class="fab fa-facebook-f"></i>)'
    )

    twitter_url = models.URLField(
        blank=True,
        help_text="Enter the full Twitter/X profile URL."
    )
    twitter_icon = models.CharField(
        max_length=100,
        blank=True,
        help_text='Font Awesome icon tag for Twitter (e.g. <i class="fab fa-x-twitter"></i>)'
    )

    youtube_url = models.URLField(
        blank=True,
        help_text="Enter the full YouTube channel or video URL."
    )
    youtube_icon = models.CharField(
        max_length=100,
        blank=True,
        help_text='Font Awesome icon tag for YouTube (e.g. <i class="fab fa-youtube"></i>)'
    )

    linkedin_url = models.URLField(
        blank=True,
        help_text="Enter the full LinkedIn profile or company page URL."
    )
    linkedin_icon = models.CharField(
        max_length=100,
        blank=True,
        help_text='Font Awesome icon tag for LinkedIn (e.g. <i class="fab fa-linkedin-in"></i>)'
    )

    instagram_url = models.URLField(
        blank=True,
        help_text="Enter the full Instagram profile URL."
    )
    instagram_icon = models.CharField(
        max_length=100,
        blank=True,
        help_text='Font Awesome icon tag for Instagram (e.g. <i class="fab fa-instagram"></i>)'
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook_url"),
            FieldPanel("facebook_icon"),
        ], heading="Facebook"),
        MultiFieldPanel([
            FieldPanel("twitter_url"),
            FieldPanel("twitter_icon"),
        ], heading="Twitter"),
        MultiFieldPanel([
            FieldPanel("youtube_url"),
            FieldPanel("youtube_icon"),
        ], heading="YouTube"),
        MultiFieldPanel([
            FieldPanel("linkedin_url"),
            FieldPanel("linkedin_icon"),
        ], heading="LinkedIn"),
        MultiFieldPanel([
            FieldPanel("instagram_url"),
            FieldPanel("instagram_icon"),
        ], heading="Instagram"),
    ]

    class Meta:
        verbose_name = _("Social Links")
        verbose_name_plural = _("Social Links")