from rest_framework.throttling import ScopedRateThrottle


class CustomScopedThrottle(ScopedRateThrottle):

    def allow_request(self, request, view):
        scope = view.throttle_scope

        if request.user.is_authenticated:
            view.throttle_scope = f"{scope}_user"
        else:
            view.throttle_scope = f"{scope}_anon"

        return super().allow_request(request, view)