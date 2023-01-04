import pytest


@pytest.mark.usefixtures("create_items")
@pytest.mark.django_db
def test_image_tree():
    assert pytest.menu1_item2.parent == pytest.menu1_item1
    assert pytest.menu1_item3.parent == pytest.menu1_item2
