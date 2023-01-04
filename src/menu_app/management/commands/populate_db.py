from typing import Any
from menu_app.models import Item, Menu
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        menu = ["test_menu1", "test_menu2"]
        for index, name in enumerate(menu):
            menu[index] = Menu.objects.create(name=name)
        items_dict = {
            "menu1_item1": {
                "url": "https://www.youtube.com",
                "parent": None,
            },
            "menu1_item2": {
                "url": "https://twitter.com",
                "parent": "menu1_item1",
            },
            "menu1_item3": {
                "url": "https://dtf.ru",
                "parent": "menu1_item2",
            },
            "menu1_item4": {
                "url": "https://www.wanikani.com",
                "parent": "menu1_item3",
            },
        }
        items_dict2 = items_dict.copy()
        for item_name, item in items_dict.items():
            items_dict[item_name] = Item.objects.create(
                url=item["url"],
                menu=menu[0],
                parent=items_dict[item["parent"]] if item["parent"] else None,
            )
        for item_name, item in items_dict2.items():
            items_dict[item_name] = Item.objects.create(
                url=item["url"],
                menu=menu[1],
                parent=items_dict[item["parent"]] if item["parent"] else None,
            )
