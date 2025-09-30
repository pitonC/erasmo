
import re

def capturar_telefono():
    """
    Captura y valida número telefónico en formato XXX-XXX-XXXX
    
    Retorna: Número validado como string
    """
    print("=== CAPTURA DE TELÉFONO ===")
    print("Formato: XXX-XXX-XXXX")
    
    while True:
        telefono = input("Ingrese número telefónico: ").strip()
        
        # Valida formato: 3 dígitos + guión + 3 dígitos + guión + 4 dígitos
        if re.match(r'^\d{3}-\d{3}-\d{4}$', telefono):
            return telefono
        else:
            print("Error: Formato debe ser como xxx-xxx-xxxx")

def main():
    """
    Función principal - Ejecuta el flujo completo del programa
    """
    telefono_validado = capturar_telefono()
    print(f"\nTeléfono registrado: {telefono_validado}")

if __name__ == "__main__":
    main()
