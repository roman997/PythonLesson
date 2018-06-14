from Machine import Machine
from Factory import Factory

m1 = Machine('Audi A8', '47 000', 'not ready')
m2 = Machine('BMW X6', '83 000', ' not ready')
m3 = Machine('BMW X5', '71 000', 'ready')

factory = Factory()
factory.add(m1)
factory.add(m2)
factory.add(m3)
factory.getStatus()
factory.allMachines()
factory.delete(m2)
print("\nПісля видалення:")
factory.allMachines()


