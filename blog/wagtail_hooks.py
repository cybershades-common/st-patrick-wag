from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import Category, Blog

class BlogCategoryViewSet(SnippetViewSet):
    model = Category
    menu_label = "Categories"
    list_display  = ("title",'weight',)

    search_fields = ("title",)

class BlogViewSet(SnippetViewSet):
    model = Blog
    menu_label = "Blog"
    list_display  = ("title",'status',)
    search_fields = ("title",)


class BlogGroup(SnippetViewSetGroup):
    menu_label = "Blog"
    menu_icon = "bars"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        BlogCategoryViewSet,
        BlogViewSet,

    )

register_snippet(BlogGroup)
