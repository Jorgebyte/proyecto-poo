from models.user import User
from models.cart import Cart, CartItem
from models.invoice import Invoice
from services.plan_factory import PlanFactory
from ui.menu import Menu
from ui.input_handler import InputHandler


class Main:
    """
    Hecho por Emir, Jorge y Axel
    """

    def run(self):
        print("=== HOSTING ===")

        # Pedimos datos del usuario y validamos con funciones separadas.
        name, last_name, phone, email = InputHandler.get_user_data()
        user = User(name, last_name, phone, email)

        cart = Cart()

        # Bucle principal del menú. Se mantiene simple: comprar, ver, quitar, pagar.
        # Usamos Menu para separar la presentación del flujo.
        while True:
            option = Menu.main_menu()

            if option == "1":
                plans = PlanFactory.get_vps_plans()

                for i, plan in enumerate(plans):
                    print(f"{i + 1}. {plan.get_info()}")

                # Elegir plan con validación numérica para evitar errores por entrada.
                choice = InputHandler.get_valid_option(
                    "Selecciona plan: ", 1, len(plans)
                ) - 1
                selected = plans[choice]

                # Repetimos hasta que el usuario seleccione un SO valido.
                # Hacemos esto para que no se elija un valor por defecto invisible.
                while True:
                    os_option = Menu.os_menu()
                    os_name = Menu.get_os_name(os_option)
                    if os_name is not None:
                        selected.set_os(os_name)
                        break
                    print("Seleccione un sistema operativo valido: 1, 2 o 3.")

                cart.add_item(CartItem(selected))
                print("Agregado al carrito.")

            elif option == "2":
                # Mostrar el contenido del carrito (solo presentacion)
                cart.show_cart()

            elif option == "3":
                # Permitir eliminar un producto si hay items
                cart.show_cart()
                if cart.is_empty():
                    continue

                index = InputHandler.get_valid_option(
                    "Eliminar #: ", 1, len(cart.items)
                ) - 1
                if cart.remove_item(index):
                    print("Producto eliminado.")

            elif option == "4":
                # Finalizar compra: si hay productos, generamos la factura.
                if cart.is_empty():
                    print("El carrito está vacío.")
                    continue

                invoice = Invoice(user, cart)
                invoice.generate()
                break

            else:
                print("Opcion invalida.")


if __name__ == "__main__":
    Main().run()