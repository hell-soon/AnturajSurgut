from rest_framework.throttling import AnonRateThrottle


class UserReviewsThrottle(AnonRateThrottle):
    scope = "user_reviews"


class SearchThrottle(AnonRateThrottle):
    scope = "search"


class FeedbackThrottle(AnonRateThrottle):
    scope = "feedback"
