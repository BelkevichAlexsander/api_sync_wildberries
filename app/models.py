from django.core.validators import FileExtensionValidator
from django.db import models


class File(models.Model):
    """Модель для файла"""
    file = models.FileField(
        help_text='Формат файла должен быть <.xlsx>',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['xlsx']
            )
        ]
    )


class Article(models.Model):
    """Модель для артикула"""
    article = models.IntegerField()
