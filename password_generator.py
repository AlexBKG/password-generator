import random
import string

def generar_contrasena(longitud=12, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_letters  # Letras
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    return ''.join(random.choice(caracteres) for _ in range(longitud))

if __name__ == "__main__":
    print("🔒 Generador de Contraseñas Seguras 🔒")
    longitud = int(input("🔹 Longitud de la contraseña: "))
    incluir_numeros = input("🔹 ¿Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("🔹 ¿Incluir símbolos? (s/n): ").lower() == 's'

    contrasena = generar_contrasena(longitud, incluir_numeros, incluir_simbolos)
    print(f"🔐 Contraseña generada: {contrasena}")

