class Dia:

  def __init__(self, anyo=1970, mes=1, dia=1):
    self.dia = dia
    self.mes = mes
    self.anyo = anyo
    self.dia_semana = self.calcular_dia_semana()
  
    if not self.fecha_valida():
      raise ValueError('Fecha Inválida')
    
  def info(self):
    print(f'La fecha es día {self.calcular_dia_semana()} {self.dia}, del {self.mes} de {self.anyo}.')
    
  def fecha_valida(self):
    if not 1 <= self.mes <= 12:
      return False
    
    dias_mes = [31, 28 + self.es_bisiesto(), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not 1 <= self.dia <= dias_mes[self.mes - 1]:
        return False
        
    return True   

  def es_bisiesto(self):
    return (self.anyo % 4 == 0 and self.anyo % 100 != 0) or (self.anyo % 400 == 0)

  def calcular_dia_semana(self):
    if self.mes < 3:
       mes = self.mes + 12
       anyo = self.anyo - 1
    else:
       mes = self.mes
       anyo = self.anyo
    
    A = anyo % 100
    B = anyo // 100
    C = 2 - B + (B // 4)
    D = A // 4
    E = (13 * (mes + 1)) // 5
    F = A + C + D + E + self.dia - 1

    dia_semana_indice = F % 7

    dia_semana = {
      0: 'Sábado',
      1: 'Domingo',
      2: 'Lunes',
      3: 'Martes',
      4: 'Miércoles',
      5: 'Jueves',
      6: 'Vienes'
    }
    return dia_semana[dia_semana_indice]
