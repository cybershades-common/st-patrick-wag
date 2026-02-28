from django.shortcuts import render, get_object_or_404
from pages.models import GeneralPage
from django.http import HttpResponse
from pages.models import ContentHolder
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def download_contentholder(request, pk):
    holder = get_object_or_404(ContentHolder, pk=pk)
    timestamp = timezone.now().strftime("%d%m%Y_%H%M%S")
    response = HttpResponse(holder.content or "", content_type="text/html")
    response['Content-Disposition'] = f'attachment; filename="{holder.slug}_{timestamp}.html"'
    return response

def news_detail(request, slug):
    news_page = get_object_or_404(GeneralPage, slug='news-details')
    return render(request, 'pages/news_detail.html', {"news_slug": slug, 'page': news_page})

def blog_detail(request, slug):
    blog_page = get_object_or_404(GeneralPage, slug='blog-details')
    return render(request, 'pages/blog_detail.html', {"blog_slug": slug, 'page': blog_page})