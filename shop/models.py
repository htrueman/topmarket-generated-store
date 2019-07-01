from django.db import models
from django.utils.translation import ugettext as _

# Single tone


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


# Models with single tone

class Domain(SingletonModel):
    is_domain = models.BooleanField(
        default=True,
        verbose_name=_('True - домен, False - поддомен')
    )
    name =  models.CharField(
        max_length=32,
        verbose_name=_('Имя домена/поддомена'),
    )

    def __str__(self):
        return ''.format(self.name)


class SliderMainPage(models.Model):
    image_url = models.URLField(
        verbose_name=_('Ссылка на картинку')
    )

    class Meta:
        verbose_name = _('Ссылка на картинку')
        verbose_name_plural = _('Ссылки на картинку')


class LogoWithPhones(SingletonModel):
    logo = models.URLField(null=True, blank=True)
    shop_name = models.CharField(max_length=40, null=True, blank=True, verbose_name=_('Название магазина'))
    first_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Контакт'))
    second_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Контакт'))


class SocialNetwork(SingletonModel):

    facebook = models.URLField(max_length=100, null=True, blank=True)
    instagram = models.URLField(max_length=100, null=True, blank=True)
    twitter = models.URLField(max_length=100, null=True, blank=True)
    google = models.URLField(max_length=100, null=True, blank=True)


class DeliveryAndPayment(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Заголовок'))
    text = models.TextField(null=True, blank=True, verbose_name=_('Текст'))


class ExchangeAndReturn(SingletonModel):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Заголовок'))
    text = models.TextField(null=True, blank=True, verbose_name=_('Текст'))


class HowToUse(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Заголовок'))
    text = models.TextField(null=True, blank=True, verbose_name=_('Текст'))


class Support(SingletonModel):
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Имя'))
    email = models.EmailField(max_length=40, null=True, blank=True, verbose_name=_('Емейл'))
    message = models.TextField(null=True, blank=True, verbose_name=_('Сообщение'))


class Contacts(SingletonModel):
    text = models.TextField(null=True, blank=True, verbose_name=_('Текст'))


class AboutUs(SingletonModel):
    title = models.CharField(max_length=40, null=True, blank=True, verbose_name=_('Заголовок'))
    image = models.URLField(null=True, blank=True)
    text = models.TextField(null=True, blank=True, verbose_name=_('Текст'))
