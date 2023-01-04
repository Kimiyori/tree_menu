import re
from django import template
from django.db.models import QuerySet

from menu_app.models import Item, Menu

register = template.Library()


@register.filter
def get_domain(url: str) -> str:
    re_domain = re.search(r"^(?:https?:\/\/)?(www\.)?(?P<domain>[^\/]+)", url)
    return re_domain["domain"] if re_domain else url


@register.inclusion_tag("menu_app/menu.html")
def draw_menu(menu: Menu) -> dict[str, QuerySet[Item] | str]:
    menu_items: QuerySet[Item] = Item.objects.filter(menu=menu)
    return {"menu_name": menu.name, "items": menu_items}
