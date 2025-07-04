from django.http import JsonResponse


def get_all_users(request):
    return JsonResponse({
        "hello": "world"
    }, safe=False)
