from django import template
from lists import models as lists_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, room):
    user = context.request.user
    if user.is_authenticated:
        the_list = lists_models.List.objects.get_or_none(
            user=user, name="My Favourite Houses"
        )
        if the_list is not None:
            return room in the_list.places.all()
        else:
            return False
    else:
        return False
