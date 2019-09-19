from functools import wraps
from .models import pageHit
from django.db.models import F
from django.db import transaction


def counted(f):
    @wraps(f)
    def decorator(request, *args, **kwargs):
        with transaction.atomic():
            counter, created = pageHit.objects.get_or_create(title=request.path)
            counter.count = F('count') + 1
            counter.save()
        return f(request, *args, **kwargs)
    return decorator
