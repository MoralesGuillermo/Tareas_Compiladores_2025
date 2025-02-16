#b. Reemplazar palabras identificando otra palabra para cambiarla en una oracion/parrafo. Por ejemplo cambiar “el” por “en”.

import re

texto = "Este es el texto de prueba para que el programa pueda remplazar el articulo 'el'"
patron = r'\b(el)\b'

ocurrencias = re.findall(patron, texto)

if ocurrencias:
    print("Ocurrencias encontradas:", ocurrencias)
else:
    print("No se encontraron ocurrencias.")

texto_modif = re.sub(patron, 'en', texto)
print("\nTexto original: ", texto)
print("\nTexto modificado: ", texto_modif)

with open("salida.txt", "w") as archivo_txt:
    archivo_txt.write(texto_modif)