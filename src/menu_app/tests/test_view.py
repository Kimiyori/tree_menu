from django.urls import reverse
import pytest


@pytest.mark.usefixtures("create_items")
@pytest.mark.django_db
def test_menu_view(client):
    response = client.get(reverse("menu_list"))
    assert response.status_code == 200
