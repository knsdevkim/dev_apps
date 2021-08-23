from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def text_capitalize(value):
    text = value.split(' ')
    text_exploded = []
    for string in text:
        text_exploded.append(string[:1].upper() + string[1:])
    return ' '.join(text_exploded)