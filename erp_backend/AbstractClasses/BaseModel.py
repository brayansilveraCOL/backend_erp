from django.db import models


class BaseModel(models.Model):
    state = models.BooleanField('State', default=True)
    create_date = models.DateField('Create Date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Modified Date', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Model'
