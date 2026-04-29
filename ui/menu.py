class Menu:
    """
    Menús del sistema
    Hecho por Jorge
    """

    @staticmethod
    def main_menu():
        # Menú principal: claro y numerado para facilitar la validación.
        print("\n1. Comprar VPS")
        print("2. Ver carrito")
        print("3. Eliminar producto")
        print("4. Finalizar compra")
        return input("Opción: ")

    @staticmethod
    def os_menu():
        # Menú de selección del sistema operativo. Devolvemos la entrada
        # tal cual; la validación se hace en Main para poder repetir si es necesario.
        print("\nSistema Operativo:")
        print("1. Ubuntu")
        print("2. Debian")
        print("3. CentOS")
        return input("Elige: ")

    @staticmethod
    def get_os_name(option):
        # Mapea la opción numérica a un nombre de SO. Si no es válido, devolvemos None
        if option == "1":
            return "Ubuntu"
        if option == "2":
            return "Debian"
        if option == "3":
            return "CentOS"
        return None