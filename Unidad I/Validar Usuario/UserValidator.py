import re

class UserValidator:

    def is_valid(self, user):
        """Validar que un usuario es válido. Un usuario debe de 
        tener entre 8 y 12 caracteres y solo puede contener letras, números
         guiones bajos o guiones altos"""
        pattern = r"^([\w\-]){8,12}$"
        return True if re.match(pattern, user) else False