from django import template

register = template.Library()

@register.filter
def count_pair_with(first_programmer, second_programmer):
    return first_programmer.get_count_paired_with(second_programmer)


@register.filter
def url_pair_with(first_programmer, second_programmer):
    return '/add_pair/' + str(first_programmer.id) + '/' + str(second_programmer.id)