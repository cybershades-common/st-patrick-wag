from django import template
from django.template import Template, Context
from pages.models import ContentHolder
from django.utils.safestring import mark_safe
from django.core.exceptions import ObjectDoesNotExist
register = template.Library()
import re
import random
from news.models import Category as newscategory,News
from blog.models import Category as blogcategory,Blog

@register.filter
def highlight(string, term):
    max_length = 200
    parts = re.split(term, string, flags=re.IGNORECASE)
    lft = parts[0][len(parts[0]) - max_length:len(parts[0])]
    rht = '' if len(parts) < 2 else parts[1][:max_length]
    return mark_safe('...%s<b>%s</b>%s...' % (lft, term, rht))

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

