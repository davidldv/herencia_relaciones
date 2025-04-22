class Antibiotico:
    def __init__(self, nombre, dosis, tipo_animal, precio):
        if dosis < 400 or dosis > 600:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg")
        if tipo_animal not in ['Bovinos', 'Caprinos', 'Porcinos']:
            raise ValueError("Tipo de animal inválido")
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio
