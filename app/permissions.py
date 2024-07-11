from rest_framework import permissions


class GlobalDefaultPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        
        permission_string = self.__get_permission_string(
            method=request.method,
            view=view
        )

        if not permission_string: # caso ocorra algum erro ao obter a string de permissão, nega o acesso
            return False

        return request.user.has_perm(permission_string)
    
    def __get_permission_string(self, method, view):
        try:
            app_name = view.queryset.model._meta.app_label
            action_name = self.__get_action_string(method)
            model_name = view.queryset.model._meta.model_name

            return f'{app_name}.{action_name}_{model_name}'
        except AttributeError:
            return None

    
    def __get_action_string(self, method):
        actions = {
            'GET': 'view',
            'HEAD': 'view',
            'OPTIONS': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
        }

        return actions[method]