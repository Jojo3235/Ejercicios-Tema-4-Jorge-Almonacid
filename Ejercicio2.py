import random

def pedir_entero(mensaje):
    while True:
        try:
            entero = int(input(mensaje))
            break
        except ValueError:
            print('Debe ingresar un número entero')
    return int(entero)

class Mission:
    def __init__(self, mission_type, planet, general, priority):
        self.mission_type = mission_type
        self.planet = planet
        self.general = general
        self.priority = priority
        
    def assign_resources(self):
        resources = {}
        if self.priority == 'alta':
            resources['Stormtroopers'] = pedir_entero('Ingrese la cantidad de Stormtroopers: ')
            resources['Scout Troopers'] = pedir_entero('Ingrese la cantidad de Scout Troopers: ')
            resources['speeder bike'] = pedir_entero('Ingrese la cantidad de speeder bike: ')
            vehicles = ['AT-AT', 'AT-RT', 'AT-TE', 'AT-DP', 'AT-ST', 'AT-M6', 'AT-MP', 'AT-DT']
            for vehicle in vehicles:
                resources[vehicle] = pedir_entero(f'Ingrese la cantidad de {vehicle}: ')
        elif self.priority == 'baja':
            if self.mission_type == 'exploración':
                resources['Scout Troopers'] = 15
                resources['speeder bike'] = 2
            elif self.mission_type == 'contención':
                resources['Stormtroopers'] = 30
                vehicles = ['AT-AT', 'AT-RT', 'AT-TE', 'AT-DP', 'AT-ST']
                for i in range(3):
                    vehicle = random.choice(vehicles)
                    if vehicle in resources:
                        resources[vehicle] += 1
                    else:
                        resources[vehicle] = 1
            elif self.mission_type == 'ataque':
                resources['Stormtroopers'] = 50
                vehicles = ['AT-AT', 'AT-RT', 'AT-TE', 'AT-DP', 'AT-ST', 'AT-M6', 'AT-MP', 'AT-DT']
                for i in range(7):
                    vehicle = random.choice(vehicles)
                    if vehicle in resources:
                        resources[vehicle] += 1
                    else:
                        resources[vehicle] = 1
            else:
                print('Tipo de misión inválida')
        return resources
    
    def show_resources(self):
        resources = self.assign_resources()
        for resource in resources:
            print(f'{resource}: {resources[resource]}')

    def __str__(self):
        return f'Mission: {self.mission_type}, Planet: {self.planet}, General: {self.general}, Priority: {self.priority}'
    
class MissionQueue:
    def __init__(self):
        self.missions = []
        
    def ask_mission(self):
        while True:
            mision = input('Ingrese el tipo de misión: ')
            if mision.lower() == 'exploración':
                mission_type = 'exploración'
                break
            elif mision.lower() == 'contención':
                mission_type = 'contención'
                break
            elif mision.lower() == 'ataque':
                mission_type = 'ataque'
                break
            else:
                print('Tipo de misión inválida')
        planet = input('Ingrese el planeta: ')
        general = input('Ingrese el general: ')
        if general == 'Palpatine' or general == 'Darth Vader':
            priority = 'alta'
        else:
            priority = 'baja'
        self.add_mission(Mission(mission_type, planet, general, priority))

    def add_mission(self, mission):
        self.missions.append(mission)
        
    def assign_missions(self):
        for mission in self.missions:
            print(mission)
            mission.show_resources()
            print()
            
    def total_resources(self):
        resources = {}
        for mission in self.missions:
            mission_resources = mission.assign_resources()
            for resource in mission_resources:
                if resource in resources:
                    resources[resource] += mission_resources[resource]
                else:
                    resources[resource] = mission_resources[resource]
        for resource in resources:
            print(f'{resource}: {resources[resource]}')

VALIDACIONES = ['s', 'S', 'SI', 'si', 'Si', 'y', 'Y', 'YES', 'yes', 'Yes']

def main():
    mission_queue = MissionQueue()
    mission_queue.add_mission(Mission('exploración', 'Tatooine', 'Palpatine', 'alta'))
    mission_queue.add_mission(Mission('contención', 'Naboo', 'Darth Vader', 'alta'))
    mission_queue.add_mission(Mission('ataque', 'Alderaan', 'Moff Tarkin', 'baja'))
    mission_queue.add_mission(Mission('exploración', 'Coruscant', 'Moff Tarkin', 'baja'))
    mission_queue.add_mission(Mission('contención', 'Kashyyyk', 'Palpatine', 'baja'))
    while input('¿Desea agregar una misión? (s/n): ') in VALIDACIONES:
        mission_queue.ask_mission()
    #por alguna razón esto genera una misión de más
    mission_queue.assign_missions()
    mission_queue.total_resources()


if __name__ == "__main__":
    main()