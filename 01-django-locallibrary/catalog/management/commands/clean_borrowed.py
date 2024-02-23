from django.core.management.base import BaseCommand
from ...models import BookInstance


class Command(BaseCommand):
    help = "Clan the borrowed"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        BookInstance.objects.all().update(borrower=None, due_back=None, status="a")

        self.stdout.write(self.style.SUCCESS("Successfully clean all books instances"))
