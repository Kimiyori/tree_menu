from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Menu(models.Model):  # type:ignore
    """Menu model"""

    name = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return str(self.name)


class Item(MPTTModel):
    """Model for menu items"""

    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    url = models.URLField()
    menu = models.ForeignKey(
        to=Menu, on_delete=models.CASCADE, null=True, blank=True, related_name="items"
    )

    def __str__(self) -> str:
        return f"{self.pk} - {self.menu}"
