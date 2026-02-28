from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from home.models import HeroAbstract
from modelcluster.fields import ParentalKey
from pages.fields import generalpage_stream_fields
from django.shortcuts import render
from django.template.loader import get_template
from wagtail.images.models import Image

# Create your models here.
class ContactSubmission(models.Model):
    name = models.CharField("Name", max_length=100)
    email = models.EmailField("Email")
    phone = models.CharField(null=True,blank=True,max_length=50)
    enquiry = models.CharField("Enquiry", max_length=255)
    message = models.TextField("Message")
    created = models.DateTimeField("Created", auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'
        ordering = ['-created',]

    def __str__(self):
        return self.email

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('enquiry'),
        FieldPanel('message'),
    ]

    def send_email(self,page):
        context = {"contact": self}
        html_template = get_template('contact/email/contact.html')
        text_template = get_template('contact/email/contact.txt')
        email_html = html_template.render(context)
        email_text = text_template.render(context)
        #send_to_email_addresses = [settings.CONTACT_EMAIL]
        if page.notification_to_address:
            to_addresses = [x.strip() for x in page.notification_to_address.split(',')]
        else:
            to_addresses = [page.notification_to_address]
        if to_addresses:
            from_email_address = page.notification_from_address
            email = EmailMultiAlternatives(subject=page.notification_subject,
                                        body=email_text,
                                        from_email=from_email_address,
                                        to=to_addresses,
                                        reply_to=[from_email_address],
                                        )
            email.attach_alternative(email_html, "text/html")
            email.send()

        #autoresponse to user
        user_email_html = page.autoresponder_content
        if user_email_html:
            user_email_text = strip_tags(user_email_html)
            automail_subject = page.autoresponder_subject
            automail_from  = page.autoresponder_from_email
            automail_to = [self.email]
            useremail = EmailMultiAlternatives(automail_subject,
                                            body=user_email_text,
                                        from_email = automail_from,
                                        to =automail_to,
                                        reply_to=[automail_from],
                                        )
            useremail.attach_alternative(user_email_html, "text/html")
            useremail.send()



class ContactpageHero(HeroAbstract):
    page = ParentalKey('ContactPage', related_name='contactpage_hero', on_delete=models.CASCADE)

class ContactPage(Page):
    short_description = models.TextField(null=True,blank=True)
    # intro = RichTextField(blank=True)
    thankyou_message = RichTextField()

    image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Form Image",
    )
    #auto
    autoresponder_from_email = models.CharField(max_length=100, null=True, blank=True)
    autoresponder_subject = models.CharField(max_length=200, null=True, blank=True)
    autoresponder_content = RichTextField(blank=True)
    #notification
    notification_from_address = models.CharField(max_length=100, null=True, blank=True)
    notification_to_address = models.CharField(max_length=200, null=True, blank=True)
    notification_subject = models.CharField(max_length=500,null=True,blank=True)
    body = StreamField(generalpage_stream_fields,null=True,blank=True)
    bottom_body = StreamField(generalpage_stream_fields,null=True,blank=True)


    content_panels = Page.content_panels + [
        InlinePanel('contactpage_hero', label='Hero Images', panels=[
            FieldPanel('image'),
            FieldPanel('pre_title'),
            FieldPanel('title'),
            FieldPanel('text'),
        ],max_num=1),
        FieldPanel('image'),
        FieldPanel('thankyou_message'),
        MultiFieldPanel([
        FieldPanel('autoresponder_from_email'),
        FieldPanel('autoresponder_subject'),
        FieldPanel('autoresponder_content'),
        ],'Autoresponder mail notification'),
        MultiFieldPanel([
        FieldPanel('notification_from_address'),
        FieldPanel('notification_to_address'),
        FieldPanel('notification_subject'),
        ],'Mail notification'),
        FieldPanel('body'),
        FieldPanel('bottom_body'),
    ]

    """promote_panels = Page.promote_panels + [
        FieldPanel('short_description'),
        FieldPanel('seo_image'),
        FieldPanel('noindex'),
    ]"""
    class Meta:
        verbose_name = "Contact Page"

    def get_hero(self):
        if self.contactpage_hero.all():
            return self.contactpage_hero.all()
        else:
            return False

    def serve(self, request):
        from contact.forms import ContactForm

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save()
                contact.send_email(self)
                return render(request, 'contact/thankyou.html', {
                    'page': self,
                    'contact': contact,
                })
        else:
            form = ContactForm()

        return render(request, 'contact/contact_form.html', {
            'page': self,
            'form': form,
        })
