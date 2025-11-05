def saludo(nombre: str) -> str:
    return f"Hola, {nombre}! Bienvenido a Git. Test1"

if __name__ == "__main__":
    nombre = input("¿Tu nombre?") 
    print(saludo(nombre))