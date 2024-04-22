from rest_framework.throttling import UserRateThrottle


class ChangePasswordThrottle(UserRateThrottle):
    scope = "change_password"


class ChangeInfoThrottle(UserRateThrottle):
    scope = "change_info"


class UserReviewsThrottle(UserRateThrottle):
    scope = "user_reviews"
