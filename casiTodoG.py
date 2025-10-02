import re

def validar_entero(texto):
    """Valida números enteros con o sin signo"""
    patron = r'^[-+]?\d+$'
    # [-+]? : signo opcional + o -
    # \d+   : uno o más dígitos
    return re.match(patron, texto) is not None

def validar_decimal(texto):
    """Valida números decimales con o sin signo"""
    patron = r'^[-+]?\d*\.\d+$'
    # [-+]? : signo opcional
    # \d*   : cero o más dígitos antes del punto
    # \.    : punto decimal
    # \d+   : uno o más dígitos después del punto
    return re.match(patron, texto) is not None

def validar_variable(texto):
    """Valida nombres de variables (letras, números, guiones bajos)"""
    patron = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    # [a-zA-Z_]   : debe empezar con letra o _
    # [a-zA-Z0-9_]* : puede continuar con letras, números o _
    return re.match(patron, texto) is not None

def validar_correo(texto):
    """Valida correos electrónicos con dominios específicos"""
    patron = r'^[a-zA-Z0-9._%+-]+@(gmail|hotmail|outlook|yahoo|tectijuana\.edu)\.(com|mx|edu\.mx)$'
    # [a-zA-Z0-9._%+-]+ : usuario del correo
    # @                 : símbolo arroba
    # (gmail|hotmail|...) : dominios permitidos
    # \.(com|mx|edu\.mx) : extensiones permitidas
    return re.match(patron, texto) is not None

def validar_url(texto):
    """Valida URLs web"""
    patron = r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/\S*)?$'
    # (https?://)? : protocolo opcional
    # (www\.)?     : www opcional
    # [a-zA-Z0-9-]+ : nombre de dominio
    # \.[a-zA-Z]{2,} : extensión de dominio
    # (/\S*)?      : ruta opcional
    return re.match(patron, texto) is not None

def identificar_tipo(texto):
    """Identifica y muestra el tipo de dato del texto ingresado"""
    if validar_entero(texto):
        print(f"✅ '{texto}' es un NÚMERO ENTERO")
    elif validar_decimal(texto):
        print(f"✅ '{texto}' es un NÚMERO DECIMAL")
    elif validar_variable(texto):
        print(f"✅ '{texto}' es una VARIABLE válida")
    elif validar_correo(texto):
        print(f"✅ '{texto}' es un CORREO electrónico válido")
    elif validar_url(texto):
        print(f"✅ '{texto}' es una URL válida")
    else:
        print(f"❌ '{texto}' no coincide con ningún formato reconocido")

def main():
    while True:
        texto = input("\nIngrese el texto a validar: ").strip()
        identificar_tipo(texto)
        
        continuar = input("\n¿Validar otro texto? (s/n): ").lower()
        if continuar != 's':
            print("Programa terminado.")
            break

if __name__ == "__main__":
    main()