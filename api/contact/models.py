from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import CreatedMixin


class ContactMessage(CreatedMixin):

    body = models.TextField(
        _("body"))
    email = models.EmailField(
        _("email"))
    name = models.CharField(
        _("name"),
        max_length=128)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "#{} from {} on {}".format(self.id, self.email, self.created)
