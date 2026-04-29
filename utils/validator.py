class Validator:
    """
    Validaciones basicas para email y telefono
    Hecho por Emir
    """

    @staticmethod
    def validate_name(name):
        # Acepta solo letras y espacios simples. Es suficiente para un formulario
        # de ejemplo en clase; si se requiere acentos u otros símbolos, ajustar.
        return bool(name) and all(part.isalpha() for part in name.split())

    @staticmethod
    def validate_email(email):
        # Validación básica: tiene '@' y un punto; evita espacios.
        # No es una validación completa RFC, pero evita errores comunes.
        return "@" in email and "." in email and " " not in email

    @staticmethod
    def validate_phone(phone):
        # Aceptamos solo dígitos y un largo entre 7 y 15 caracteres.
        # Esto cubre números locales y algunos internacionales simples.
        return phone.isdigit() and 7 <= len(phone) <= 15