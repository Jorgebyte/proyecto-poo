class InvoiceFormatter:
    """
    Hecho por Axel
    """

    @staticmethod
    def format(invoice):
        # Construye la factura como una lista de líneas para facilitar cambios
        lines = []
        lines.append("===== FACTURA =====")
        lines.append(f"Cliente: {invoice.user.get_full_name()}")
        lines.append(f"Teléfono: {invoice.user.phone}")
        lines.append(f"Correo: {invoice.user.email}")
        lines.append("")
        lines.append("Productos:")

        for i, item in enumerate(invoice.cart.items, start=1):
            # Cada item muestra su descripción y SO (si se seleccionó)
            lines.append(f"{i}. {item.get_info()}")

        lines.append("")
        lines.append(f"TOTAL: ${invoice.cart.get_total()}")
        lines.append("===================")

        return "\n".join(lines)


class Invoice:
    """
    Factura (Composición).
    Hecho por Axel
    """

    def __init__(self, user, cart):
        self.user = user
        self.cart = cart

    def generate(self):
        print(InvoiceFormatter.format(self))