import math
import VectorLib as vec

G = 6.67428e-11

class Simulation:

    def __init__(self, collisions):
        self.bodies = list()
        self.Time = 0
        self.collisions = collisions


    def CollisionDetection(self):
        for b0 in range(0, len(self.bodies) - 1):
            for b1 in range(b0 + 1, len(self.bodies)):
                if(vec.Distance(b0.Position, b1.Position) < b0.Radius + b1.Radius):
                    return True
                
        return False

    def Simulate(self, dt): #dt = delta time
        self.Time += dt

        # Gravitional Attraction
        for b0 in range(0, len(self.bodies) - 1):
            for b1 in range(b0 + 1, len(self.bodies)):
                self.bodies[b0].Attract(self.bodies[b1], dt)

        # Movement of Bodies
        for body in self.bodies:
            body.Simulate(dt)
        
        if(self.collisions):
            self.CollisionDetection()


class CelestialBody:

    def __init__(self, Mass, Position, Velocity, Radius):
        self.Mass = Mass
        self.Position = Position
        self.Velocity = Velocity
        self.Radius = Radius

    def Simulate(self, dt):
        self.Position += self.Velocity * dt

    def ApplyForce(self, force, dt):
        self.Velocity += force / self.Mass * dt

    def Attract(self, other, dt):
        vector = self.Position - other.Position
        direction = vector.Normalize()
        force = direction * G * self.Mass * other.Mass / (vector.Magnitude()**2)
        self.ApplyForce(-force, dt)
        other.ApplyForce(force, dt)


    def GetInfo(self):
        return "Mass: " + str(self.Mass) + "   Position: " + self.Position.GetInfo() + "   Velocity: " + self.Velocity.GetInfo() + "   Radius: " + str(self.Radius)