from models.plan import VPSPlan


class PlanFactory:
    """
    Crea planes VPS
    Hecho por Jorge
    """

    @staticmethod
    def get_vps_plans():
        # Fabrica tres planes sencillos para que el menú muestre opciones.
        # Mantener esta lógica en una fábrica facilita cambiar precios luego.
        return [
            VPSPlan("VPS Básico", 10, 2),
            VPSPlan("VPS Medio", 20, 4),
            VPSPlan("VPS Pro", 40, 8)
        ]