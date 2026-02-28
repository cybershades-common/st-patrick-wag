from django.core.management.base import BaseCommand
from pages.models import ContentHolder
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates or updates content holders from HTML files'

    def handle(self, *args, **options):
        # Define content holders to create
        content_holders = [
            {
                'title': 'Header Design',
                'slug': 'header-design',
                'file': 'content_holders/header_design.html'
            },
            {
                'title': 'Footer Design',
                'slug': 'footer-design',
                'file': 'content_holders/footer_design.html'
            },
            {
                'title': 'Header Script',
                'slug': 'header-script',
                'file': 'content_holders/header_script.html'
            },
            {
                'title': 'Footer Script',
                'slug': 'footer-script',
                'file': 'content_holders/footer_script.html'
            },
        ]

        base_dir = settings.BASE_DIR

        for holder_data in content_holders:
            file_path = os.path.join(base_dir, holder_data['file'])
            
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                holder, created = ContentHolder.objects.get_or_create(
                    slug=holder_data['slug'],
                    defaults={
                        'title': holder_data['title'],
                        'content': content
                    }
                )
                
                if not created:
                    holder.title = holder_data['title']
                    holder.content = content
                    holder.save()
                    self.stdout.write(
                        self.style.SUCCESS(f'Updated content holder: {holder_data["title"]}')
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f'Created content holder: {holder_data["title"]}')
                    )
            else:
                self.stdout.write(
                    self.style.WARNING(f'File not found: {file_path}')
                )
