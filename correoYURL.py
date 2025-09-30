import re

def validar_correo(texto):
    """
    Valida si el texto tiene formato de correo electrónico válido
    Dominios aceptados: gmail, hotmail, outlook, yahoo, live, tectijuana.edu.mx
    Formatos: usuario@dominio.com | usuario@dominio.mx | usuario@tectijuana.edu.mx
    """
    patron = r'^[a-zA-Z0-9._%+-]+@(gmail|hotmail|outlook|yahoo|live|tectijuana\.edu)\.(com|mx|edu\.mx)$'
    return re.match(patron, texto) is not None

def validar_url(texto):
    """
    Valida si el texto tiene formato de URL web
    Formatos aceptados: 
    - www.ejemplo.com
    - http://www.ejemplo.com
    - https://ejemplo.com/pagina
    - ejemplo.mx
    """
    patron = r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/\S*)?$'
    return re.match(patron, texto) is not None

def main():
    """
    Función principal que ejecuta el sistema de validación
    Flujo:
    1. Captura texto del usuario
    2. Valida si es correo o URL
    3. Muestra resultado
    4. Pregunta si desea continuar
    """
    while True:
        texto = input("\nIngrese el texto a validar: ").strip()
        
        if validar_correo(texto):
            print("✅ El texto es un CORREO electrónico válido")
        elif validar_url(texto):
            print("✅ El texto es una URL válida")
        else:
            print("❌ El texto no es correo ni URL válido")
        
        continuar = input("\n¿Desea validar otro texto? (s/n): ").strip().lower()
        if continuar != 's':
            print("Programa terminado.")
            break

if __name__ == "__main__":
    main()
    