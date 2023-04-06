from django.contrib import admin
from .models import Usuario

# Decorador
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    """Essa classe foi criada para que no modo admin do Django, o usuário
        admin só terá autorização para ver os campos, e não alterá-los."""
    readonly_fields = ('nome', 'email', 'senha')


# admin.site.register(Usuario)
