class Plan:
    """
    Clase base (Herencia)
    Hecho por Jorge
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name} - ${self.price}"


class VPSPlan(Plan):
    """
    Plan VPS
    """

    def __init__(self, name, price, ram):
        super().__init__(name, price)
        self.ram = ram
        # Guardamos el SO como texto para mostrarlo en la factura.
        # Inicialmente no está seleccionado para que el usuario deba elegirlo.
        self.os = "Sin seleccionar"

    def set_os(self, os_name):
        self.os = os_name

    def get_info(self):
        return f"{self.name} ({self.ram}GB) - ${self.price} | SO: {self.os}"