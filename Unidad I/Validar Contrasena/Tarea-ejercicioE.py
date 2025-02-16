import re

def validar_contrasena(contrasena):
    exp = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.fullmatch(exp, contrasena))

def main():
    while True:
        contrasena = input("Ingrese la contraseña: ")
        if validar_contrasena(contrasena):
            print("La contraseña es segura")
            break
        else:
            print("La contraseña es insegura.")
            print("Intente de nuevo.")

if __name__ == "__main__":
    main()
