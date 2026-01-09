from django.template import Library


register = Library()


@register.filter
def get_the_name():
    pass
