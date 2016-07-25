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

    TYPE_CHOICES = (
        ('SW Version', _('SW Version')),
        ('HartBeat', _('HeartBeat')),
        ('ErrorCode', _('ErrorCode')),
    )
    types = models.CharField(
        max_length=10, 
        choices=TYPE_CHOICES,
        verbose_name=_('Type')
    )

    STATION_CHOICES = (
        ('AAA', _('AAA')),
        ('ALS', _('ALS')),
        ('B3', _('B3')),
        ('DP1', _('DP1')),
        ('DP2', _('DP2')),
        ('HBT', _('HBT')),
        ('IT-CG', _('IT-CG')),
        ('IT-HSG1', _('IT-HSG1')),
        ('IT-HSG2', _('IT-HSG2')),
        ('MBA', _('MBA')),
        ('MBO', _('MBO')),
        ('MIC2', _('MIC2')),
        ('PFR', _('PFR')),
        ('RCAM', _('RCAM')),
        ('SA-IT-CG', _('SA-IT-CG')),
        ('SA-IT-HSG1', _('SA-IT-HSG1')),
        ('SA-IT-HSG2', _('SA-IT-HSG2')),
        ('SMS', _('SMS')),
        ('STOM', _('STOM')),
    )
    station = models.CharField(
        max_length=20,
        choices=STATION_CHOICES,
        verbose_name=_('station'),
    )

    title = models.CharField(
        max_length=100,
        verbose_name=_('title'),
    )

    content = models.TextField(
        max_length=2000, null=True,
        verbose_name=_('content'),
    )

    STATUS_CHOICES = (
        ('OPEN', _('OPEN')),
        ('CLOSE', _('CLOSE')),
    )
    status = models.CharField(
        max_length=5, 
        choices=STATUS_CHOICES,
        verbose_name=_('status')
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
        return "#"+str(self.id)+ ', ' + str(self.title)

    def get_absolute_url(self):
        return reverse('buglist_detail', kwargs={'pk': self.pk})


class Tracker(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='owned_tracker',
    )

    buglist = models.ForeignKey(
        'Buglist',
        related_name='menu_items_tracker', 
        verbose_name=_('buglist'),
    )

    message = models.TextField(
        max_length=300, null=True,
        verbose_name=_('message'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Tracker')
        verbose_name_plural = _('Trackers')

    def __str__(self):
        return self.message

    def get_absolute_url(self):
       return reverse('buglist_detail', kwargs={'pk': self.buglist.pk})


class Station(models.Model):

    buglist = models.ForeignKey(
        'Buglist',
        related_name='menu_items_station', 
        verbose_name=_('buglist'),
    )

    stationid = models.CharField(
        max_length=50,
        verbose_name=_('stationid'),
    )
    
    STATUS_CHOICES = (
        ('OPEN', _('OPEN')),
        ('CLOSE', _('CLOSE')),
    )
    status = models.CharField(
        max_length=5, 
        choices=STATUS_CHOICES,
        verbose_name=_('status')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Station')
        verbose_name_plural = _('Stations')

    def __str__(self):
        return self.stationid


