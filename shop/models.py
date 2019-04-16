from django.db import models
from django.utils.translation import ugettext as _


class SliderMainPage(models.Model):
    image_url = models.URLField(
        verbose_name=_('Ссылка на картинку')
    )

    class Meta:
        verbose_name = _('Ссылка на картинку')
        verbose_name_plural = _('Ссылки на картинку')


class LogoWithPhones(models.Model):
    logo = models.URLField(null=True, blank=True)
    shop_name = models.CharField(max_length=40, null=True, blank=True, verbose_name=_('Название магазина'))
    first_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Контакт'))
    second_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Контакт'))

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class SocialNetwork(models.Model):

    facebook = models.URLField(max_length=100, null=True, blank=True)
    instagram = models.URLField(max_length=100, null=True, blank=True)
    twitter = models.URLField(max_length=100, null=True, blank=True)
    google = models.URLField(max_length=100, null=True, blank=True)


class DeliveryAndPayment(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Заголовок'))
    text = models.TextField(null=True, blank=True, verbose_name=_('Текст'))


class ExchangeAndReturn(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Заголовок'))
    text = models.TextField(null=True, blank=True, verbose_name=_('Текст'))


class HowToUse(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Заголовок'))
    text = models.TextField(null=True, blank=True, verbose_name=_('Текст'))


class Support(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Имя'))
    email = models.EmailField(max_length=40, null=True, blank=True, verbose_name=_('Емейл'))
    message = models.TextField(null=True, blank=True, verbose_name=_('Сообщение'))


class Contacts(models.Model):
    text = models.TextField(null=True, blank=True, verbose_name=_('Текст'))


class AboutUs(models.Model):
    title = models.CharField(max_length=40, null=True, blank=True, verbose_name=_('Заголовок'))
    image = models.ImageField(upload_to='shop/about_us', null=True, blank=True)
    text = models.TextField(null=True, blank=True, verbose_name=_('Текст'))
