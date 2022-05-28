import factores_primos

class Test_Factores_primos_ObtenerPrimos:
    def test_obtenerPrimos_1(self):
        result = factores_primos.obtenerPrimos([12, 12345, "a1969970175", 12, "bc23a9d531064583ace8f67dad60f6bb", "a1969970175", 56784, 56784])

    def test_obtenerPrimos_2(self):
        result = factores_primos.obtenerPrimos([12345, 12, 56784, 12, 12, 12, "bc23a9d531064583ace8f67dad60f6bb", 987650])

    def test_obtenerPrimos_3(self):
        result = factores_primos.obtenerPrimos([12345, 987650, 987650, "a1969970175", 987650, 12345, 56784, 12345])

    def test_obtenerPrimos_4(self):
        result = factores_primos.obtenerPrimos([987650, 12, 12, "bc23a9d531064583ace8f67dad60f6bb", "bc23a9d531064583ace8f67dad60f6bb", 56784, 987650, 56784])

    def test_obtenerPrimos_5(self):
        result = factores_primos.obtenerPrimos([12345, 12345, 12345, 12345, 12, 12345, "bc23a9d531064583ace8f67dad60f6bb", "a1969970175"])

    def test_obtenerPrimos_6(self):
        result = factores_primos.obtenerPrimos([])

