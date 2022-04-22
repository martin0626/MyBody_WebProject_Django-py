from MyBody.navigation.models import Navigation


def nav_processor(request):
    navigation = Navigation.objects.filter(is_active=True)
    print(navigation)
    return {
        'navigation': navigation,
    }
