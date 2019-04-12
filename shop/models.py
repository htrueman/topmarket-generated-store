from django.db import models
from django.utils.translation import ugettext as _


class SliderMainPage(models.Model):
    image_url = models.URLField(
        verbose_name=_('Ссылка на картинку')
    )

    class Meta:
        verbose_name = _('Ссылка на картинку')
        verbose_name_plural = _('Ссылки на картинку')


