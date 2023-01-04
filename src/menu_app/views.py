from django.views.generic import ListView
from menu_app.models import Menu


class MenuView(ListView):  # type:ignore
    """View for display list of menus"""

    context_object_name = "menus"
    template_name: str = "menu_app/index.html"
    queryset = Menu.objects.all()  # pylint: disable=no-member
