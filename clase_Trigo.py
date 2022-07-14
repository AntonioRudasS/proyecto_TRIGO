class Trigo:

    #inicializar atributos
    def __init__(self, cant_almacenada, cant_plantada, T_cosecha, dinero):
        self.cant_almacenada = cant_almacenada
        self.cant_plantada = cant_plantada
        self.T_cosecha = T_cosecha
        self.dinero = dinero
    
    #metodo para cosechar el objeto "Trigo"
    def cosechar(self):
        if self.T_cosecha < 3 and self.cant_plantada != 0:
            print("Tiene que esperar para poder cosechar.")
            self.T_cosecha += 1
        elif self.T_cosecha == 3 and self.cant_plantada != 0:
            self.cant_almacenada += self.cant_plantada * 2
            self.cant_plantada = 0
            self.T_cosecha = 0
            print("Cosecha realizada exitosamente!")
    
    #metodo para plantar n unidades del objeto "Trigo"
    def plantar(self, cant_plan):
        if self.cant_almacenada >= cant_plan:
            self.cant_almacenada -= cant_plan
            self.cant_plantada = cant_plan
            print("Se han plantado", cant_plan, "exitosamente.")
        else:
            print("La cantidad de trigo almacenada, no alcanza para lo que quiere plantar.")
    
    #metodo para vender n cantidades del objeto "Trigo"
    def vender(self, cant_vender):
        precio = 2
        self.cant_almacenada -= cant_vender
        self.dinero += cant_vender * precio

    #metodo para comprar n cantidades del objeto "Trigo"
    def comprar(self, cant_comprar):
        precio = 2
        self.cant_almacenada += cant_comprar
        self.dinero -= cant_comprar

    #metodo para mostrar los datos 
    def mostrar(self):
        print("Semillas almacenadas: ", self.cant_almacenada)
        print("Semillar plantadas: ", self.cant_plantada)
        print("Dinero: ", self.dinero)
