from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _
from catalog import constants


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Дата обновления'))

    class Meta:
        abstract = True


class Category(MPTTModel):
    id = models.PositiveIntegerField(
        primary_key=True,
        verbose_name='id - primary key',
    )
    name = models.CharField(
        max_length=256,
        verbose_name=_('Название категории'),
    )
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.SET_NULL,
        db_index=True,
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    @property
    def get_category_level(self):
        return self.get_level()

    def __str__(self):
        return '{}'.format(self.name)


class Product(TimeStampedModel):
    """
    Если поле contractor=NULL - товар добавлен поставщиком.
    В противном случае это товар, добавленный партнером от поставщика
    """

    id = models.PositiveIntegerField(
        primary_key=True,
        verbose_name='id - primary key',
    )

    category = TreeForeignKey(
        Category,
        null=True, blank=True,
        verbose_name=_('Категория товара'),
        on_delete=models.SET_NULL,
    )

    availability = models.CharField(
        max_length=13,
        verbose_name=_('Доступность товара'),
        choices=constants.PRODUCT_AVAILABILITY,
        default='IN_STOCK'
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('Имя продукта')
    )
    vendor_code = models.CharField(
        max_length=63,
        verbose_name=_('Артикул'),
    )
    product_type = models.CharField(
        max_length=256,
        verbose_name=_('Вид товара')
    )
    brand = models.CharField(
        max_length=255,
        verbose_name=_('Бренд'),
    )
    count = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Наличие'),
    )
    description = models.TextField(
        max_length=4095,
        null=True, blank=True,
        verbose_name=_('Описание'),
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True, blank=True,
        verbose_name=_('Цена товара'),
    )

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')


class ProductImageURL(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    url = models.URLField(
        verbose_name=_('Ссылка на картинку'),
    )


class ProductCharacteristic(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='characteristics')
    characteristic_type = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name=_('Тип характеристики'),
    )
    name = models.CharField(
        max_length=255,
        null=True, blank=True,
        verbose_name = _('Имя характеристики'),
    )
    value = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.characteristic_type} -- {self.name} -- {self.value}'

    class Meta:
        ordering = ['product']
        verbose_name = _('Характеристика')
        verbose_name_plural = _('Характеристики продукта')
        unique_together = ['product', 'characteristic_type', 'name', 'value']


class FeedBack(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_feedback'
    )
    name = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name=_('Имя пользователя'),
    )
    content = models.TextField(verbose_name=_('Отзыв'), max_length=1024)
    pub_date = models.DateTimeField(
        verbose_name=_('Дата создания отзыва'),
        auto_now_add=True
    )
    reply = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return self.content[0:200]
