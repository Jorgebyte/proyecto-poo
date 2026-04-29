class User:
    """
    Representa un usuario
    Hecho por Emir
    """

    def __init__(self, name, last_name, phone, email):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def get_full_name(self):
        # Método simple para obtener nombre completo, usado en la factura
        return f"{self.name} {self.last_name}"