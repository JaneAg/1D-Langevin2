#Langevin simulator of a 1D particle using Object Oriented Programming, OOP.
from random import gauss
import numpy as np
import matplotlib.pyplot as plt

#Parameters given in reduced unit:
mass = 1
Temp = 1 
K_B = 1

wall_size = 5
dt = 0.1
total_time = 1000
gamma = 0.1

#Finding the standard deviation
std_dev = lambda Temp, gamma, K_B: (2 * Temp * gamma * K_B)**0.5
sigma = std_dev(Temp, gamma, K_B)

#Finding the total number of time steps
num_steps = lambda total_time, dt: total_time/dt
n = int(num_steps(total_time, dt))

#vel is for velocity and pos is for position
vel = np.zeros([n])
pos = np.zeros([n])
time = np.arange(0, n, dt)

#The positions and velocities will be added to the lists x and v respectively
x = []
v = []

times_it_hits_wall_size = []
wall_at_zero = []



#Using Euler algorithm to find the positions and velocities of the 1D particle

# f = open('output.txt','w')
class Dynamics():
    
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def move(self):    
        for j in range(1, 101):
                      
            #Initial position and velocity            
            self.vel[0] = 0
            self.pos[0] = 0                 

            for i in range(n):
                
                mu = 0
                epsilon = gauss(mu, sigma) #epsilon is a random force

                #The expressions below are Euler integrators for velocity and position
                self.vel[i] = self.vel[i-1] + ((-gamma * self.vel[i-1] + epsilon) * dt)
                self.pos[i] = self.pos[i-1] + dt * self.vel[i-1] + ((-gamma * self.vel[i-1] + epsilon) * dt**2)
                
                #It is expected that if the particle hits either of the walls (wall size is from 0 to 5), it should stop
                if self.pos[i] <= 0:
                    wall_at_zero.append(i*dt)
                    break
                    
                elif self.pos[i] >= 5:
                    times_it_hits_wall_size.append(i*dt)
                    print('Particle stopped at i = {}'.format(i))
                    break
                                        
                else:
                    x.append(self.pos[i])
                    v.append(self.vel[i])
                    # f.write("%4s\n%5s\n%10s\n%10s\n" % (i, time, x[i], v[i])) 
                                                     
            # return i, x, v
            
        return times_it_hits_wall_size

my_dynamics = Dynamics(pos, vel)
print(my_dynamics.move())

# f.close()

#Plot of the trajectory of the particle
plt.plot(time[0:len(x)], x, 'r')
plt.xlabel('Time')
plt.ylabel('Position') 
plt.show()

#Making a histogram of the number of times the particle hits the wall size (5)
# plt.hist(times_it_hits_wall_size, bins=(10), rwidth=0.85, color='y')
# plt.xlabel('Times the particle hits the wall size')
# plt.show()