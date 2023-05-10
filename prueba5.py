import random

class Mision:
    def __init__(self, tipo, planeta, general):
        self.tipo = tipo
        self.planeta = planeta
        self.general = general
        self.prioridad = "alta" if general in ["Palpatine", "Darth Vader"] else "baja"
        self.recursos_asignados = []

    def seleccionar_recursos(self):
        if self.prioridad == "alta":
            self.recursos_asignados = "Recursos sin asignar, por favor, seleccione los recursos manualmente."
            print("Número de stormtroopers: ")
            self.recursos_asignados["Stormtroopers"] = input()
            print("Número de Scout Troopers: ")
            self.recursos_asignados["Scout Troopers"] = input()
            print("Número de speeder bike: ")
            self.recursos_asignados["speeder bike"] = input()
            print("Número de AT-AT: ")
            self.recursos_asignados["AT-AT"] = input()
            print("Número de AT-RT: ")
            self.recursos_asignados["AT-RT"] = input()
            print("Número de AT-TE: ")
            self.recursos_asignados["AT-TE"] = input()
            print("Número de AT-DP: ")
            self.recursos_asignados["AT-DP"] = input()
            print("Número de AT-ST: ")
            self.recursos_asignados["AT-ST"] = input()       
            print("Número de AT-M6: ")
            self.recursos_asignados["AT-M6"] = input()
            print("Número de AT-MP: ")
            self.recursos_asignados["AT-MP"] = input()
            print("Número de AT-DT: ")
            self.recursos_asignados["AT-DT"] = input()

    def asignar_recursos(self):
        if self.prioridad == "alta":
            Mision.seleccionar_recursos(self)
        else:
            if self.tipo == "exploración":
                self.recursos_asignados = ["15 Scout Troopers", "2 speeder bike"]
            elif self.tipo == "contención":
                self.recursos_asignados = ["30 Stormtroopers", "AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"]
                self.recursos_asignados = random.sample(self.recursos_asignados, 4) # selecciona 3 vehículos aleatorios
            elif self.tipo == "ataque":
                self.recursos_asignados = ["50 Stormtroopers", "AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]
                self.recursos_asignados = random.sample(self.recursos_asignados, 8) # selecciona 7 vehículos aleatorios
            else:
                print("Tipo de misión no válido.")

    def mostrar_recursos_asignados(self):
        print("Recursos asignados: ")
        for recurso in self.recursos_asignados:
            print(recurso)

    def __str__(self):
        return "Tipo: " + self.tipo + "\nPlaneta: " + self.planeta + "\nGeneral: " + self.general + "\nPrioridad: " + self.prioridad + "\n"
    
#Crear misiones
mision1 = Mision("exploración", "Tatooine", "Palpatine")
mision2 = Mision("contención", "Naboo", "Darth Vader")
mision3 = Mision("ataque", "Kashyyyk", "Palpatine")
mision4 = Mision("exploración", "Hoth", "Darth Vader")
mision5 = Mision("contención", "Endor", "Palpatine")
mision6 = Mision("ataque", "Yavin", "Darth Vader")

#Asignar recursos
mision1.asignar_recursos()
mision2.asignar_recursos()
mision3.asignar_recursos()
mision4.asignar_recursos()
mision5.asignar_recursos()
mision6.asignar_recursos()

#Mostrar recursos asignados
print("Mision 1" + "\n" + str(mision1))
mision1.mostrar_recursos_asignados()
mision2.mostrar_recursos_asignados()
mision3.mostrar_recursos_asignados()
mision4.mostrar_recursos_asignados()
mision5.mostrar_recursos_asignados()
mision6.mostrar_recursos_asignados()

