class Factory:
    def __init__(self):
        self.machines = []


    def add(self, machine):
        self.machines.append(machine)


    def delete(self, machine):
        self.machines.remove(machine)


    def getStatus(self):
        count = 0
        assembled = 0
        for machine in self.machines:
            count += 1
            if machine.ready:
                assembled += 1
        print("Всього машин " + str(count))
        print("Готових машин " + str(assembled))
    
    
    def allMachines(self):
        status = ""
        for machine in self.machines:   
            if machine.ready:
                status = "Готова"
            else:
                status = "Не готова"
            print("Назва машини " + str(machine.machineName) + " Ціна машини " + str(machine.price) + " Готовність машини " + status)
        