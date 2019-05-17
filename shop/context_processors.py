from .models import LogoWithPhones, SocialNetwork


def take_logo_with_phones(request):
    logo_with_phones = LogoWithPhones.objects.first()
    social_networks = SocialNetwork.objects.first()
    return {
        'logo_with_phones': logo_with_phones,
        'social_networks': social_networks,
    }
