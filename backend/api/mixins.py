from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


# Thismmixin will make authenticated users to only see their own post and not others
class UserQuerySetMixin:
    user_field = "user"

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and user.is_staff:
            return qs
        return qs.filter(**lookup_data)
