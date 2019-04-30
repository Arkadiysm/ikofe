from django.db import models
from django.utils import timezone
from uuid import uuid4
from django.core.files.storage import FileSystemStorage
from os.path import splitext


class UUIDFileStorage(FileSystemStorage):
    def generate_filename(self, filename):
        _, ext = splitext(filename)
        return uuid4().hex + ext


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=10000)
    image = models.ImageField(storage=UUIDFileStorage())

    def __str__(self):
        return self.title

    @staticmethod
    def get_events_quantity():
        return len(Event.objects.all())

    @staticmethod
    def get_event_by_id(event_id):
        try:
            return Event.objects.all().filter(id=event_id)[0]
        except IndexError:
            return None

    @staticmethod
    def get_last_events(quantity, start_from=1):
        all_events = Event.objects.all()

        if len(all_events) >= (start_from + quantity - 1):
            return all_events.order_by('pub_date')[start_from - 1: quantity]
        elif len(all_events) > start_from:
            return all_events.order_by('pub_date')[start_from - 1: len(all_events)]
        else:
            return None


class Project(models.Model):
    categories = (
        ('video_ad', 'Видеореклама'),
        ('elevator', 'Реклама в лифтах')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=50, choices=categories, default='video_ad')
    description = models.CharField(max_length=10000)
    image = models.ImageField(storage=UUIDFileStorage(), blank=True)
    youtube_link = models.CharField(max_length=150, blank=True)


    @staticmethod
    def get_all():
        return Project.objects.all()

    @staticmethod
    def get_all_by_category(category):
        if category in [c[0] for c in Project.categories]:
            return Project.get_all().filter(category=category)
        else:
            return None

    @staticmethod
    def get_project_by_id(project_id):
        try:
            return Project.objects.all().filter(id=project_id)[0]
        except IndexError:
            return None

    @staticmethod
    def get_last_projects(quantity, start_from=1):
        all_projects = Project.get_all()

        if len(all_projects) >= (start_from + quantity - 1):
            return all_projects.order_by('pub_date')[start_from - 1: quantity]
        elif len(all_projects) > start_from:
            return all_projects.order_by('pub_date')[start_from - 1: len(all_projects)]
        else:
            return None

    def __str__(self):
        return self.title
