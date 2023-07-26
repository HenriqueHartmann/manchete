from rest_framework.exceptions import PermissionDenied


def is_user_authenticated(request):
    if not request.user.is_authenticated: 
        raise PermissionDenied("Você não tem permissão.")
def is_user_super(request):
    if not request.user.is_superuser:
        raise PermissionDenied("Você não tem permissão.")

def is_user_a_writer_or_super(request):
    if request.user.groups.filter(name='writer').exists() == False:
        if not request.user.is_superuser:
            raise PermissionDenied("Você não tem permissão.")
        
def is_user_an_editor_or_super(request):
    if request.user.groups.filter(name='editor').exists() == False:
        if not request.user.is_superuser:
            raise PermissionDenied("Você não tem permissão.")
