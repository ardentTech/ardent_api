from django.db import models
from django.utils.translation import ugettext_lazy as _

from taxonomy.models import TaggedMixin
from utils.models import CreatedMixin, UpdatedMixin


class Post(CreatedMixin, TaggedMixin, UpdatedMixin):

    body = models.TextField(_("body"))
    is_public = models.BooleanField(_("is public"), default=False)
    title = models.CharField(_("title"), max_length=128)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return "Post: {}".format(self.title)
