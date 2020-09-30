from django import template
register = template.Library()


def my_filter(value):
    B = ''
    for i in reversed(value):

        B = B + i
    return B


register.filter('my_filter',my_filter)
