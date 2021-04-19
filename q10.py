class mycar:

    def __init__(self, distance, time):
        self.d = distance
        self.t = time

    def vel(self):
        v = self.d / self.t
        return v


distance = int(input("enter the distance "))
time = int(input("enter the time "))
p1 = mycar(distance, time)
print("the velocity = "+str(p1.vel()))
