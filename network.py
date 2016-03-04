import random
#network module

class Work_station:
    def __init__(self, title=""):
        self.title = title
        self.switched_to = False

    def connect_to(self, switch):
        switch.connect(self)

    def ping(self, pc):
        if not self.switched_to:
            print("no connection to the network")
            return None

        all_devices = self.switched_to.connected
        if pc not in all_devices:
            print("ping: unknown host ", pc.title)
            return None

        print("PING ", pc.title, " 56(84) bytes of data.")
        for i in range(6):
            print("64 bytes from", pc.title, ": icmp_seq=1 ttl=59 time=26.2 ms")
        print("5 packets transmitted, 5 received,",
              "0% packet loss, time", random.randrange(3900, 4050), "ms")


class Switch:
    def __init__(self):
        self.connected = []

    def connect(self, device):
        if device not in self.connected:
            self.connected.append(device)
            device.switched_to = self
        return self


assert Work_station() is not None
assert Switch() is not None

pc1 = Work_station("Alice")
pc2 = Work_station("Bob")
sw = Switch().connect(pc1).connect(pc2)
print(sw.connected)
pc1.ping(pc2)
print()
pc2.ping(pc1)
jim=Work_station("Jim")
print()
pc1.ping(jim)
print()
jim.ping(pc1)