from utils.validator import Validator


class InputHandler:
    """
    Maneja entradas del usuario
    Hecho por Emir
    """

    @staticmethod
    def get_valid_input(message, validation_func, error_message="Dato inválido."):
        # Pide un valor y lo valida con una función pasada por parámetro.
        # De esta forma la validación queda centralizada y es fácil de cambiar.
        while True:
            value = input(message).strip()
            if validation_func(value):
                return value
            # Mensaje claro: indicamos qué faltó o qué no es correcto.
            print(error_message)

    @staticmethod
    def get_valid_option(message, minimum, maximum):
        # Valida que la entrada sea un número y esté dentro del rango.
        while True:
            value = input(message).strip()
            if value.isdigit():
                number = int(value)
                if minimum <= number <= maximum:
                    return number
            # Mensaje específico para guiar al usuario
            print(f"Dato inválido. Debe elegir un número entre {minimum} y {maximum}.")

    @staticmethod
    def get_user_data():
        # Solicitamos nombre y apellido usando validaciones sencillas.
        # Si el profesor pide permitir caracteres especiales, cambiar Validator.
        name = InputHandler.get_valid_input(
            "Nombre: ",
            Validator.validate_name,
            "Falta el nombre o no es válido."
        )
        last_name = InputHandler.get_valid_input(
            "Apellido: ",
            Validator.validate_name,
            "Falta el apellido o no es válido."
        )

        # Teléfono: aceptamos solo dígitos y un largo razonable.
        phone = InputHandler.get_valid_input(
            "Teléfono: ",
            Validator.validate_phone,
            "Falta el número de teléfono o no es válido."
        )

        # Email: validación básica para evitar entradas sin arroba o espacios.
        email = InputHandler.get_valid_input(
            "Correo: ",
            Validator.validate_email,
            "Falta el correo o no es válido. Ej: usuario@dominio.com"
        )

        return name, last_name, phone, email