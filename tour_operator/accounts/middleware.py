from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser


def is_admin(user):
    return user.is_admin


class AccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.route_permissions = {
            '/countries/': ['admin', 'regular'],
            '/hotels/': ['admin', 'regular'],
            '/tours/': ['admin', 'regular'],
            '/contracts/create/': ['admin', 'regular'],
            '/clients/create/': ['admin', 'regular'],
            '/employees/create/': ['admin'],
            '/employees/edit/': ['admin'],
        }

    def __call__(self, request):
        if isinstance(request.user, AnonymousUser):
            if request.path_info != reverse('accounts:login'):
                return redirect(reverse('accounts:login'))
            return self.get_response(request)

        current_path = request.path_info

        if any(route in current_path for route in ('/employees/', '/admin/')):
            if not is_admin(request.user):
                raise PermissionDenied("Недостаточно прав для доступа")

        for route, allowed_users in self.route_permissions.items():
            if route in current_path:
                if request.user.user_type not in allowed_users:
                    raise PermissionDenied("Недостаточно прав для доступа")

        return self.get_response(request)