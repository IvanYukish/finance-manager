import os
from datetime import datetime
from uuid import uuid4

from django.conf import settings


def path_and_rename(instance, filename):
    path = settings.UPLOAD_TO_PATHS[instance.__class__.__name__]
    extension = filename.split(".")[-1]
    random_string = uuid4().hex
    filename = "{}.{}".format(random_string, extension)
    return os.path.join(datetime.strftime(datetime.today(), path), filename)
