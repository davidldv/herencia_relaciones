from modelo.antibiotico import Antibiotico

def test_dosis_invalida():
    try:
        Antibiotico("Test", 300, "Bovinos", 50000)
        assert False, "Debería lanzar ValueError"
    except ValueError:
        assert True

def test_tipo_animal_invalido():
    try:
        Antibiotico("Test", 500, "Felinos", 50000)
        assert False, "Debería lanzar ValueError"
    except ValueError:
        assert True

if __name__ == "__main__":
    test_dosis_invalida()
    test_tipo_animal_invalido()
    print("Todos los tests pasaron.")
