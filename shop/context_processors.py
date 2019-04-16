from .models import LogoWithPhones


def take_logo_with_phones(request):
    logo_with_phones = LogoWithPhones.objects.first()
    return {'logo_with_phones': logo_with_phones}
