from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from rest_framework.throttling import UserRateThrottle

from django.db.models import Q
from django_filters import rest_framework as filters

from backend.paginator import StandardResultsSetPagination

from users.models import CustomUser
from order.models import Order
from reviews.models import Review

from .serializers.Users.UserSerializer import (
    UserSerializer,
    UserUpdateSerializer,
)
from .serializers.Users.UserOrderSerializer import (
    ProfilListeOrderSerializer,
    ProfileDetailOrderSerializer,
)

from .serializers.Users.UserReviewSerializer import ProfileReviewSerializer


from reviews.filters.reviewfilter import ReviewsFilter
from order.filters.OrderFilter import OrderFilter


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]

    def get_queryset(self):
        if self.action.startswith("review"):
            self.filterset_class = ReviewsFilter
            queryset = Review.objects.filter(user=self.request.user).order_by(
                "-created_at"
            )
            queryset = self.filter_queryset(queryset)
            return queryset
        if self.action.startswith("order"):
            self.filterset_class = OrderFilter
            queryset = Order.objects.filter(
                Q(user_phone=self.request.user.phone)
                | Q(user_email=self.request.user.email)
            ).order_by("-created_at")
            queryset = self.filter_queryset(queryset)
            return queryset
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == "current":
            return UserSerializer
        elif self.action == "update":
            return UserUpdateSerializer
        elif self.action in [
            "review",
            "review_create",
            "review_detail",
            "update_review",
        ]:
            return ProfileReviewSerializer
        if self.action == "orders":
            return ProfilListeOrderSerializer
        elif self.action == "order_info":
            return ProfileDetailOrderSerializer

        return self.serializer_class

    @action(detail=False, methods=["get"])
    def current(self, request):
        user = request.user
        serializer = self.get_serializer_class()
        data = serializer(user).data
        return Response(data)

    @action(detail=False, methods=["get"])
    def review(self, request):
        reviews = self.get_queryset()
        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(reviews, request)
        serializer = self.get_serializer_class()(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @action(detail=False, methods=["post"])
    def review_create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Отзыв успешно опубликован"},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    @action(detail=True, methods=["patch"])
    def update_review(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        if instance.user != request.user:
            return Response(
                {"detail": "У вас нет разрешения на изменение этого отзыва"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}
        return Response(
            {"message": "Отзыв успешно обновлен"}, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["get"])
    def review_detail(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=["delete"])
    def review_delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response(
                {"detail": "У вас нет разрешения на удаление этого отзыва"},
                status=status.HTTP_403_FORBIDDEN,
            )
        self.perform_destroy(instance)
        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}
        return Response(
            {"message": "Отзыв успешно удален"}, status=status.HTTP_204_NO_CONTENT
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(
            {"message": "Данные успешно обновлены"}, status=status.HTTP_200_OK
        )

    @action(detail=False, methods=["get"])
    def orders(self, request):
        orders = self.get_queryset()
        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(orders, request)
        serializer = self.get_serializer_class()(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @action(detail=True, methods=["get"])
    def order_info(self, request, pk=None):
        order = self.get_object()
        serializer = self.get_serializer_class()(order)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def change_order(self, request):
        pass
