def encontrar_vocales(cadena):
    """
    Encuentra y devuelve las vocales presentes en una cadena de texto.

    Args:
        cadena (str): La cadena de texto en la que se buscarán las vocales.

    Returns:
        list: Una lista con las vocales encontradas en la cadena.
    """
    vocales = ['a', 'e', 'i', 'o', 'u']
    vocales_encontradas = []

    for caracter in cadena.lower():
        if caracter in vocales:
            vocales_encontradas.append(caracter)

    return vocales_encontradas


def main():
    """
    Función principal que solicita una cadena de texto al usuario y muestra las vocales encontradas.
    """
    cadena_usuario = input("Ingresa una palabra o una oración: ")
    vocales = encontrar_vocales(cadena_usuario)

    print(f"Las vocales encontradas en '{cadena_usuario}' son: {', '.join(vocales)}")


if __name__ == "__main__":
    main()