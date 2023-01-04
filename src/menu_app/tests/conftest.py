import pytest

from menu_app.models import Item, Menu


@pytest.fixture
def create_menu():
    pytest.menu1 = Menu.objects.create(name="test_menu1")
    pytest.menu2 = Menu.objects.create(name="test_menu2")


@pytest.fixture
def create_items(create_menu):
    items_dict = {
        "menu1_item1": {
            "url": "https://www.youtube.com",
            "menu": pytest.menu1,
            "parent": None,
        },
        "menu1_item2": {
            "url": "https://twitter.com",
            "menu": pytest.menu1,
            "parent": "menu1_item1",
        },
        "menu1_item3": {
            "url": "https://dtf.ru",
            "menu": pytest.menu1,
            "parent": "menu1_item2",
        },
    }
    for item_name, item in items_dict.items():
        setattr(
            pytest,
            item_name,
            Item.objects.create(
                url=item["url"],
                menu=item["menu"],
                parent=getattr(pytest, item["parent"]) if item["parent"] else None,
            ),
        )
