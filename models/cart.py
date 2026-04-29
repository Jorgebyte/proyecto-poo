class CartItem:
    """
    Representa un producto dentro del carrito
    Hecho por Axel
    """

    def __init__(self, plan):
        self.plan = plan

    def get_info(self):
        return self.plan.get_info()

    def get_price(self):
        return self.plan.price


class Cart:
    """
    Carrito (Agregacion)
    Hecho por Axel
    """

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)
            return True
        # Mensaje claro cuando el índice está fuera del rango
        print("Índice inválido.")
        return False

    def is_empty(self):
        return len(self.items) == 0

    def show_cart(self):
        if self.is_empty():
            # Mensaje claro cuando no hay productos
            print("Carrito vacío.")
            return

        for i, item in enumerate(self.items):
            print(f"{i + 1}. {item.get_info()}")

    def get_total(self):
        return sum(item.get_price() for item in self.items)