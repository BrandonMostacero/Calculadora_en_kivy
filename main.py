# Importamos los módulos necesarios para hacer la calculadora en Kivy.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Creamos nuestra clase que tendrá toda la lógica de las operaciones.
class MiWidget(BoxLayout):

    # Definimos la clase añadiendo el estado en el que se encuentra el modo de operacion y también añandimos un título.
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.modo_complejo = False
        self.ids.titulo.text = "CALCULADORA HECHA EN KIVY"

    # Esta función, al ser ejecutada, cambiará el estado de la operación de la calculadora.
    def cambiar_modo(self):
        self.modo_complejo = not self.modo_complejo

    # De acuerdo al modo de operación en el que se encuentra la calculadora, la función recibirá los números que se les de.
    # IMPORTANTE!!!!: Python utiliza el "j" para los números complejos, no "i".
    def recibir_valores(self):
        try:
            if self.modo_complejo:
                n1 = complex(self.ids.num1.text)
                n2 = complex(self.ids.num2.text)
            else:
                n1 = float(self.ids.num1.text)
                n2 = float(self.ids.num2.text)
            return n1,n2
        except ValueError:
            self.ids.resultado.text = "Syntaxis Error"
            return None,None

    # En esta función, el valor que se ingrese como parámetro será analizado si se trata de un número real o complejo.
    # Luego, se devolverá el resultado de la operación del que lo llamó. 
    def mostrar_resultado(self,valor):
        if isinstance(valor, complex):
            if valor.imag == 0:
                return str(valor.real)
            elif valor.real == 0:
                return f"{valor.imag}j"
            else:
                signo = '+' if valor.imag >= 0 else ''
                return f"{valor.real}{signo}{valor.imag}j"
        return str(valor)
    
    # Aquí se encuentras todas las operaciones básicas. 
    # Para números complejos, solo se definió las operaciones de Suma, Resta, Multiplicación y División.
    def sumar(self):
        n1, n2 = self.recibir_valores()
        if n1 is not None:
            self.ids.resultado.text = self.mostrar_resultado(n1+n2)

    def restar(self):
        n1, n2 = self.recibir_valores()
        if n1 is not None:
            self.ids.resultado.text = self.mostrar_resultado(n1-n2)
    
    def multiplicar(self):
        n1, n2 = self.recibir_valores()
        if n1 is not None:
            self.ids.resultado.text = self.mostrar_resultado(n1*n2)
    
    def dividir(self):
        n1, n2 = self.recibir_valores()
        if n1 is not None:
            try:
                self.ids.resultado.text = self.mostrar_resultado(n1/n2)
            except ZeroDivisionError:
                self.ids.resultado.text = "No se puede dividir entre '0'"
    
    def potencia(self):
        try:
            n1 = float(self.ids.num1.text)
            n2 = float(self.ids.num2.text)
            if n1 == 0 and n2 == 0:
                self.ids.resultado.text = "No es posible '0**0'"
            else:
                self.ids.resultado.text = str(n1**n2)
        except ValueError:
            self.ids.resultado.text = "Syntaxis Error"
    
    def raiz(self):
        try:
            n1 = float(self.ids.num1.text)
            n2 = float(self.ids.num2.text)
            if n2 == 0:
                self.ids.resultado.text = "No es posible su resultado"
            else:
                self.ids.resultado.text = str(n1**(1/n2))
        except ValueError:
            self.ids.resultado.text = "Syntaxis Error"

# Esta clase se encargará de ejecutar la clase inicial al ser ejecutada.
class MyApp(App):
    def build(self):
        return MiWidget()

# Finalmente, se ejecuta la clase MyApp.
if __name__ == "__main__":
    MyApp().run()