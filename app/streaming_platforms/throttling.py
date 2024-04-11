from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


# For Authenticated user
class UserPlatformViewThrottle(UserRateThrottle):
    scope = 'user-platforms'


# For Anonymous user
class AnonPlatformViewThrottle(AnonRateThrottle):
    scope = 'anon-platforms'
