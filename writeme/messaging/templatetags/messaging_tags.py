from django import template

register = template.Library()

@register.filter
def limit_char_50(string):
    if len(string) > 50:
        return string[:50] + "..."
    return string