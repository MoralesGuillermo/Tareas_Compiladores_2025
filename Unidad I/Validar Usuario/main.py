from UserValidator import UserValidator
import sys

# Ejecutar código si se llama directamente al archivo 
if __name__ == "__main__":
    # Se leen los argumentos recibidos desde la consola 
    users = sys.argv[1:]
    valid_users = []
    user_validator = UserValidator()
    for user in users:
        if (user_validator.is_valid(user)):
            valid_users.append(user)
    print(f"Usuarios validos encontrados: {valid_users}")