# REGISTRO DE FRUTAS

frutas = set()


def agregar_fruta():
    fruta = input("Nombre de la fruta: ").strip().title()

    if fruta == "":
        print("Debes escribir un nombre de fruta.")
        return

    if fruta in frutas:
        print(f"'{fruta}' ya está registrada, no se repite.")
    else:
        frutas.add(fruta)
        print(f"'{fruta}' agregada correctamente.")


def mostrar_frutas():
    if len(frutas) == 0:
        print("Todavía no hay frutas registradas.")
        return

    print("\n--- FRUTAS REGISTRADAS ---")
    numero = 1
    for fruta in frutas:
        print(f"{numero}. {fruta}")
        numero += 1
    print(f"Total de frutas distintas: {len(frutas)}")


def buscar_fruta():
    fruta = input("Fruta a buscar: ").strip().title()

    if fruta in frutas:
        print(f"Sí, '{fruta}' está en la lista.")
    else:
        print(f"'{fruta}' no está registrada.")


def eliminar_fruta():
    fruta = input("Fruta a eliminar: ").strip().title()

    if fruta in frutas:
        frutas.remove(fruta)
        print(f"'{fruta}' eliminada.")
    else:
        print(f"'{fruta}' no está en la lista.")


def menu():
    opcion = ""
    while opcion != "5":
        print("\n===== REGISTRO DE FRUTAS =====")
        print("1. Agregar fruta")
        print("2. Mostrar frutas")
        print("3. Buscar fruta")
        print("4. Eliminar fruta")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_fruta()
        elif opcion == "2":
            mostrar_frutas()
        elif opcion == "3":
            buscar_fruta()
        elif opcion == "4":
            eliminar_fruta()
        elif opcion == "5":
            print("¡Hasta pronto!")
        else:
            print("Opción no válida, intenta de nuevo.")


menu()