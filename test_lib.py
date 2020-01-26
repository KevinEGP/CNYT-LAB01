import lib as c

def test_suma():
        assert c.suma((3,2),(7,5)) == (10, 7), 'Debe ser 10 + 7i'

def test_resta():
        assert c.resta((3,2),(7,5)) == (-4, -3), 'Debe ser -4 - 3i'

def test_producto():
        assert c.producto((3,2),(7,5)) == (11, 29), 'Debe ser 11 + 29i'

def test_cociente():
        assert c.cociente((3,2),(7,5)) == (0.4189189189189189, -0.013513513513513514), 'Debe ser 0.4189189189189189 - 0.013513513513513514i'

def test_modulo():
        assert c.modulo((3,2)) == 3.605551275463989, 'Debe ser 3.605551275463989'

def test_conjugado():
        assert c.conjugado((3, 2)) == (3, -2), 'Debe ser 3 - 2i'

def test_potencia():
        assert c.potencia((3, 2),3) == (-9, 46), 'Debe ser -9 + 46i'

def test_pol():
        assert c.pol((3, 2)) == (3.605551275463989, 0.5880026035475675), 'Debe ser (3.605551275463989, 0.5880026035475675)'

def test_rec():
        assert c.rec((3.605551275463989, 0.5880026035475675)) == (3.0, 1.9999999999999996), 'Debe ser (3.0, 1.9999999999999996)'

def test_printP():
        assert c.str(printP((3,2))) == "3e^(i2)", 'Debe ser 3e^(i2)'

def test_printR():
        assert c.str(printR((3,2))) == "3 + 2i", 'Debe ser 3 + 2i'


if __name__=='__main__':
    test_suma()
    test_resta()
    test_producto()
    test_cociente()
    test_modulo()
    test_conjugado()
    test_pol()
    test_rec()
    test_printP
    test_printR
    print('Prueba exitosa')
