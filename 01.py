from network import *

pc1 = Work_station("Alice")
pc2 = Work_station("Bob")
sw = Switch().connect(pc1).connect(pc2)
print(sw.connected)
pc1.ping(pc2)
print()
pc2.ping(pc1)


