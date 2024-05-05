import VectorLib as vec
import Physics as phs

Sim = phs.Simulation(False)


body0 = phs.CelestialBody(4.94407e14, vec.Vector3(-200, 0, 0), vec.Vector3(0, 12.5664, 0), 1)
body1 = phs.CelestialBody(4.94407e14, vec.Vector3(0, 200, 0), vec.Vector3(12.5664, 0, 0), 1)
body2 = phs.CelestialBody(4.94407e14, vec.Vector3(200, 0, 0), vec.Vector3(0, -12.5664, 0), 1)
body3 = phs.CelestialBody(4.94407e14, vec.Vector3(0, -200, 0), vec.Vector3(-12.5664, 0, 0), 1)

Sim.bodies.append(body0)
Sim.bodies.append(body1)
Sim.bodies.append(body2)
Sim.bodies.append(body3)

for i in range(0, 2001):
    Sim.Simulate(0.5)
    
    if(Sim.Time%10.0 == 0): 
        print(body0.Position.GetInfo(), "       ", body1.Position.GetInfo(), "       ", body2.Position.GetInfo(), "       ", body3.Position.GetInfo(), "       ", Sim.Time)
#print(body0.Position.GetInfo(), "       ", body1.Position.GetInfo(), "       ", body2.Position.GetInfo(), "       ", Sim.Time)

