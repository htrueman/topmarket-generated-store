from django.db import models
from catalog.models import TimeStampedModel, Product
from django.utils.translation import ugettext as _


class Order(TimeStampedModel):
    user_phone = models.CharField(
        max_length=13,
        verbose_name=_('Телефон покупателя')
    )
    city = models.CharField(
        max_length=256,
        null=True, blank=True,
        verbose_name=_('Город покупателя')
    )
    first_name = models.CharField(
        max_length=256,
        verbose_name=_('Имя покупателя')
    )
    last_name = models.CharField(
        max_length=256,
        verbose_name=_('Фамилия покупателя'),
        null=True, blank=True
    )
    patronymic = models.CharField(
        max_length=256,
        verbose_name=_('Отчество'),
        null=True, blank=True,
    )
    email = models.EmailField(
        null=True, blank=True,
        verbose_name=_('Електронный адрес покупателя')
    )
    phone = models.CharField(
        max_length=13,
        verbose_name=_('Телефон покупателя')
    )
    nova_poshta = models.CharField(
        max_length=256,
        null=True, blank=True,
        verbose_name=_('Отделение новой почты')
    )

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    @property
    def full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.patronymic)

    def __str__(self):
        return self.full_name


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name=_('Количество товара'),
        default=1
    )

