import pytest

from menu_app.templatetags.menu_template_tag import draw_menu, get_domain


def test_get_domain_success():
    domain = get_domain("https://youtu.be/JBeEpW8l-Mg")
    assert domain == "youtu.be"


def test_get_domain_fail():
    domain = get_domain("something_wrong")
    assert domain == "something_wrong"


@pytest.mark.usefixtures("create_items")
@pytest.mark.django_db
def test_draw_menu():
    result = draw_menu(pytest.menu1)
    assert result["menu_name"] == pytest.menu1.name
    assert len(result["items"]) == 3
