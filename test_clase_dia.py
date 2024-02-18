from clase_dia import Dia

def test_fecha_valida():
  fecha = Dia(1970, 1, 1)
  assert fecha.anyo == 1970
  assert fecha.mes == 1
  assert fecha.dia == 1
  assert fecha.fecha_valida()

def test_fecha_invalida():
  try:
    Dia(2024, 2, 31)
    assert False
  except ValueError:
    assert True

def test_anyo_bisiesto():
  fecha_bisiesta = Dia(2020, 2, 29)
  assert fecha_bisiesta.es_bisiesto() == True

  fecha_no_bisiesta = Dia(2021, 2, 28)
  assert fecha_no_bisiesta.es_bisiesto() == False

def test_calcular_dia_semana():
  assert Dia(2024, 2, 8).calcular_dia_semana() == 'Jueves'  
  assert Dia(2023, 11, 22).calcular_dia_semana() == 'Miércoles' 
  assert Dia(2020, 1, 1).calcular_dia_semana() == 'Miércoles' 
  assert Dia(2005, 1, 2).calcular_dia_semana() == 'Domingo'  
  assert Dia(2021, 5, 10).calcular_dia_semana() == 'Lunes' 