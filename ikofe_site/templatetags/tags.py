from django import template

register = template.Library()


@register.simple_tag
def abs_url(req):
    return '{0}://{1}/'.format(req.scheme, req.get_host())