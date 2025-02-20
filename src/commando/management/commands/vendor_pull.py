import helpers
from django.conf import settings
from django.core.management.base import BaseCommand

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js"
}
STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")
class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Downloading vendor files...')
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
               self.stdout.write(
                   self.style.ERROR(f"Failed to download {url}"))
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("Successfully downloaded all vendor files")) 