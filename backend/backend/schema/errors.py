from drf_yasg import openapi


def generate_error_schema(serializer_class):
    fields = serializer_class().get_fields()
    error_schema = {}
    for field_name, field in fields.items():
        error_schema[field_name] = openapi.Schema(
            type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)
        )
    if hasattr(serializer_class, "validate") and serializer_class.validate != getattr(
        serializer_class.__base__, "validate", None
    ):
        error_schema["error"] = openapi.Schema(
            type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)
        )
    return error_schema
