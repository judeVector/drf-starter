from rest_framework import permissions


# class IsStaffEditorPermission(permissions.DjangoModelPermissions):
#     def has_permission(self, request, view):
#         user = request.user
#         print(user.get_all_permissions())
#         if user.is_staff:
#             if user.has_perm("products.view_product"):  # "app_name.verb_model_name"
#                 return True
#         return False


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }
