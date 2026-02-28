from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import ContentHolder, DynamicContentSnippet, PhotoGallery, BlockCatalog

class BlockCatalogViewSet(SnippetViewSet):
    model = BlockCatalog
    menu_label = "Blocks Catalog"
    ordering = ("title",'image',)
    list_display = ["title", "image_preview"]
    search_fields = ("title",)
    add_to_settings_menu  = True
    #index_template_name = "pages/wagtailsnippets/blockcatalog/index.html"

register_snippet(BlockCatalogViewSet)    


class PhotoGalleryViewSet(SnippetViewSet):
    model = PhotoGallery
    menu_label = "Photo Galleries"
    ordering = ("title",)
    search_fields = ("title",)
    add_to_admin_menu = True

register_snippet(PhotoGalleryViewSet)    

class CHSnippetViewSet(SnippetViewSet):
    model = ContentHolder
    menu_label = "Content Holders"
    ordering = ("title",)
    search_fields = ("title",)
    list_display = ["title", "download_button"] 

class DynamicCHSnippetViewSet(SnippetViewSet):
    model = DynamicContentSnippet
    menu_label = "Dynamic Content Snippet"
    ordering = ("title",)
    search_fields = ("title",)


class CHSnippetGroup(SnippetViewSetGroup):
    menu_label = "Content Holders"
    menu_icon = "bars"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        CHSnippetViewSet,
        DynamicCHSnippetViewSet,
        
    )

register_snippet(CHSnippetGroup)
