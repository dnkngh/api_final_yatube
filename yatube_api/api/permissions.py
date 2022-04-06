from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Ограничение доступа на внесение изменений только авторам контента."""
    message = (
        'Вы не можете вносить изенения, так как не являетесь автором '
        'этого контента.'
    )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
