from django.utils.translation import ugettext as _
from django.db import models
from django.conf import settings


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"))
    feedback_text = models.CharField(max_length=10000, verbose_name=_("Feedback"))


    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")
