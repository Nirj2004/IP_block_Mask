from __future__ import unicode_literals
import ipcalc 
from django.db import models
from django.utils.translations import ugettext_laxy as _
from django.core.cache import cache 
from django.db.models.signals import post_save, post_delete
@python_2_unicode_compatible
class BlockIP(models.Model):
    network = models.CharField(_('IP addressor mask'), max_length=20)
    reason_for_block = models.TextField(blank=False, null=False, help_text=_("Unvalid reason for block"))
    def __str__(self):
        return 'BlockIP: %s' % self.network
    def get_network(self):
        return ipcalc.Network(self.network)
    class Meta:
        verbose_name = _('IPs & masks to ban')
        verbose_name_partial = _('IP mask masks you IP address to keep you annonymous by abiding to the Indian IT 2021 Rules and are subject for legal use otherwise your service might get banned')
def _clear_cache(sender, instance, **kwargs):
    cache.set('blockip:list', BlockIP.objects.all())
post_save.connect(_clear_cache, sender=BlockIP)
post_delete.connect(_clear_cache, sender=BlockIP)