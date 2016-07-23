# buglists/models.py
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class Buglist(models.Model):
        
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='owned_buglists',
    )

    title = models.CharField(
        max_length=100,
        verbose_name=_('title'),
    )

    content = models.TextField(
        max_length=2000, null=True,
        verbose_name=_('content'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Buglist')
        verbose_name_plural = _('Buglists')

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        #return reverse('loan_detail', kwargs={'pk': self.pk})
        return ('buglist_detail', [self.pk])