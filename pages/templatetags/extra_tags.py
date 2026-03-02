from django import template
from django.template import Template, Context
from pages.models import ContentHolder
from django.utils.safestring import mark_safe
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify
register = template.Library()
import re
import random
from news.models import Category as newscategory,News
from blog.models import Category as blogcategory,Blog
from wagtailmenus.models import FlatMenu
from wagtail.models import Site

@register.filter
def highlight(string, term):
    max_length = 200
    parts = re.split(term, string, flags=re.IGNORECASE)
    lft = parts[0][len(parts[0]) - max_length:len(parts[0])]
    rht = '' if len(parts) < 2 else parts[1][:max_length]
    return mark_safe('...%s<b>%s</b>%s...' % (lft, term, rht))

@register.filter
def split_words(value):
    if not value:
        return []
    return [word for word in re.split(r'\s+', str(value).strip()) if word]

@register.filter
def split_lines(value):
    if not value:
        return []
    text = str(value)
    text = text.replace('<br />', '\n').replace('<br>', '\n')
    return [line.strip() for line in text.splitlines() if line.strip()]


@register.inclusion_tag('pages/menus/flat_menu_dropdown.html', takes_context=True)
def flat_menu_any(context, handle):
    request = context.get('request')
    site = None
    if request is not None:
        site = getattr(request, 'site', None) or Site.find_for_request(request)
    if site is None:
        site = Site.objects.filter(is_default_site=True).first()

    menu_qs = FlatMenu.objects.filter(handle=handle)
    if site is not None:
        menu_qs = menu_qs.filter(site=site)

    menu = menu_qs.first()
    items = []

    if menu:
        for item in menu.custom_flat_menu_items.all().order_by('sort_order'):
            href = '#'
            if item.link_page:
                if getattr(item.link_page, 'live', True) is False:
                    continue
                href = item.link_page.url or '#'
            elif item.link_url:
                href = item.link_url

            if item.url_append:
                href = f"{href}{item.url_append}"

            items.append({
                'href': href,
                'text': item.link_text or '',
            })

    return {'menu_items': items}


@register.inclusion_tag('pages/content-holders/content_holder.html',takes_context=True)
def load_content_holder(context, Slug):
    html_header = ""
    try:
        header = ContentHolder.objects.get(slug=Slug)
        if header.content:
            # Remove compress tags from content holder HTML to avoid lessc requirement
            content = header.content
            if '{% compress' in content or 'compress %}' in content:
                # Strip out compress tags if present
                import re
                content = re.sub(r'{%\s*compress[^%]*%}.*?{%\s*endcompress\s*%}', '', content, flags=re.DOTALL)
            try:
                header_template = Template(content)
                html_header = header_template.render(context)
            except Exception as e:
                # If rendering fails, return empty string instead of error
                html_header = ""
    except ObjectDoesNotExist:
        # Content holder doesn't exist, return empty string
        html_header = ""
    except Exception:
        # Any other error, return empty string
        html_header = ""

    return {
        'html_header': html_header
    }

@register.simple_tag()
def get_news_category():
    items = newscategory.objects.filter(newscategories__isnull=False).distinct()
    #print("---------------",items)
    return {'items':items}

@register.simple_tag()
def get_news_detail(slug):
    try:
        detail = News.objects.get(slug=slug)
    except Exception:
        detail = False
    return {
        'item': detail
    }

@register.simple_tag()
def get_news_items(category="all",limit="-1"):
    items = News.objects.filter(status=True).order_by('release_date')

    # Filter by category slug if provided
    if category and category != 'all':
        items = items.filter(news_category__category__slug=category)

    if limit != "-1":
        try:
            limit = int(limit)
            items = items[:limit]
        except ValueError:
            pass  # If not a valid integer, return all

    return {'items':items}


@register.simple_tag()
def get_blog_category():
    items = blogcategory.objects.filter(blogcategories__isnull=False).distinct()
    return {'items':items}

@register.simple_tag()
def get_blog_detail(slug):
    try:
        detail = Blog.objects.get(slug=slug)
    except Exception:
        detail = False
    return {
        'item': detail
    }

@register.simple_tag()
def get_blog_items(category="all",limit="-1"):
    items = Blog.objects.filter(status=True).order_by('-release_date')  # latest first

    if limit != "-1":
        try:
            limit = int(limit)
            items = items[:limit]
        except ValueError:
            pass  # If not a valid integer, return all

    return {'items': items}



@register.simple_tag
def get_related_blogs(slug, count=2):

    # Find other blogs sharing any of those categories
    related_blogs = Blog.objects.exclude(slug=slug).distinct()[:count]

    return {'items':related_blogs}

@register.simple_tag()
def get_next_pre_pages(page):
    if not page:
        return False

    # Get the current page's parent
    parent_page = page.specific.get_parent()

    # Get the previous page (sibling), published and in menu
    previous_page = (
        page.specific.get_prev_sibling()
        if page.specific.get_prev_sibling() and page.specific.get_prev_sibling().live and page.specific.get_prev_sibling().show_in_menus
        else None
    )

    # If no previous sibling, get the last child of the parent's previous sibling
    if not previous_page and parent_page.get_prev_sibling():
        previous_sibling = parent_page.get_prev_sibling()
        previous_page = (
            previous_sibling.get_children()
            .live()
            .in_menu()
            .last()
        )

    # Get the next page (sibling), published and in menu
    next_page = page.specific.get_next_sibling()
    if next_page and (not next_page.live or not next_page.show_in_menus):
        next_page = None

    # Try to get the second next page
    second_next_page = None
    if next_page:
        temp = next_page.get_next_sibling()
        if temp and temp.live and temp.show_in_menus:
            second_next_page = temp

    # If no next_page, get the first child of parent's next sibling
    if not next_page:
        next_sibling = parent_page.get_next_sibling()
        if next_sibling:
            next_page = (
                next_sibling.get_children()
                .live()
                .in_menu()
                .first()
            )
            # Attempt to get second next page after this
            if next_page:
                temp = next_page.get_next_sibling()
                if temp and temp.live and temp.show_in_menus:
                    second_next_page = temp

    # If second_next_page is still not found, try again from parent's next sibling
    if not second_next_page and parent_page.get_next_sibling():
        second_next_page = (
            parent_page.get_next_sibling()
            .get_children()
            .live()
            .in_menu()
            .first()
        )

    return {
        'previous_page': previous_page,
        'next_page': next_page,
        'second_next_page': second_next_page,
    }


@register.simple_tag()
def get_random_number_tagged(min_value=1, max_value=10000):
    number = random.randint(min_value, max_value)
    return number


@register.simple_tag(takes_context=True)
def get_main_menu_items(context):
    """
    Returns a list of main menu items directly from the DB for the current site.
    Each item has: text, href, slug, image_url, children (list of {text, href}).
    Replaces double {% main_menu %} calls to avoid wagtailmenus double-render issues.
    """
    from wagtailmenus.models import MainMenu
    from wagtail.models import Site

    request = context.get('request')
    if not request:
        return []

    try:
        current_site = Site.find_for_request(request)
        menu = MainMenu.objects.filter(site=current_site).first()
        if not menu:
            return []

        result = []
        for menu_item in menu.custom_main_menu_items.all().select_related('link_page', 'image').order_by('sort_order'):
            try:
                # Determine display text
                text = (menu_item.link_text or
                        (menu_item.link_page.title if menu_item.link_page else '') or
                        menu_item.link_url or '')
                if not text:
                    continue

                # Determine href and child pages
                if menu_item.link_page and menu_item.link_page.live:
                    href = menu_item.link_page.get_url(request) or menu_item.link_page.url or '#'
                    children = []
                    for child in menu_item.link_page.get_children().live().in_menu():
                        child_href = child.get_url(request) or child.url or '#'
                        children.append({'text': child.title, 'href': child_href})
                elif menu_item.link_url:
                    href = menu_item.link_url
                    children = []
                else:
                    continue

                # Get image rendition URL
                image_url = ''
                if menu_item.image:
                    try:
                        rendition = menu_item.image.get_rendition('original')
                        image_url = rendition.url
                    except Exception:
                        pass

                # Determine active state based on request path
                is_active = False
                if menu_item.link_page:
                    page_url = menu_item.link_page.url or ''
                    if page_url and page_url != '/' and (
                        request.path == page_url or
                        request.path.startswith(page_url.rstrip('/') + '/')
                    ):
                        is_active = True

                result.append({
                    'text': text,
                    'href': href,
                    'slug': slugify(text),
                    'image_url': image_url,
                    'children': children,
                    'is_active': is_active,
                })
            except Exception:
                continue  # skip bad items, keep processing the rest

        return result
    except Exception:
        return []
