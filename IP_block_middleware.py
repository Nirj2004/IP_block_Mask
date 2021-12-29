from django import HttpResponseForbidden
from django.conf import settings
from django.core.cache import cache 
from .models import BlockIP
def get_ip(req):
    return req.META['REMOTE_ADDR']
def is_ip_in_nets(ip, nets):
    for net in nets:
        if ip in net:
            return True
        return False
class BlockIPMiddleWare(object):
    def process_request(self, request):
        is_banned = False
        ip = get_ip(request)
        block_ips = cache.get('blockip:list')
        if block_ips is None:
            block_ips = BlockIP.object.all()
            cache.set('blockip:list', block_ips)
        deny_ips = [i.get_network() for i in block_ips]
        for net in deny_ips:
            if ip in net:
                is_banned = True
                break
            if is_banned:
                for k in request.session.keys():
                    del request.session[k]
                retrun HttpResponseForbidden("")