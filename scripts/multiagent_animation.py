import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import argparse

class Node():
    def __init__(self):
        self.id = 0
        self.pos = 0
        self.vel = 0
        self.cluster_head = 0

class Cluster():
    def __init__(self):
        self.id = 0;
        self.level = 0;

class MultiagentSimulation(object):
    def __init__(self, N_agents = 50, interval = 32,
                 xmax = 1, ymax = 1):

        # Parameters
        self.N_agents = N_agents  # Number of agents
        self.interval = interval  # 
        self.xmax     = xmax
        self.ymax     = ymax

        # State
        self.pos_agents = (self.xmax, self.ymax) * np.random.rand(N_agents,2) # agent positions
        self.vel_agents = 0.1 * np.random.randn(N_agents,2)                   # agent velocities

        # Animation
        self.fig, self. ax = plt.subplots()
        self.animation = animation.FuncAnimation(self.fig, self.update_plot,
                                                 interval = self.interval, init_func =
                                                 self.setup_plot, blit=True, frames = 100)

    def setup_plot(self):
        self.ax.set_xlim((0,self.xmax))
        self.ax.set_ylim((0,self.ymax))
        self.scatter = self.ax.scatter(self.pos_agents[:,0],self.pos_agents[:,1])
        return [self.scatter]

    def update_plot(self, i):
        self.pos_agents += self.vel_agents * 0.001 * self.interval
        self.pos_agents = np.remainder(self.pos_agents,(self.xmax,self.ymax))
        self.scatter.set_offsets(self.pos_agents)
        return [self.scatter]

    

parser = argparse.ArgumentParser()

parser.add_argument("-N", "--n-agents", action = "store", type=int,
                    dest="N_agents", default = 50,
                    help = "number of agents to simulate")



if __name__ == '__main__':
    args = parser.parse_args()
    ms = MultiagentSimulation(N_agents = args.N_agents)
    ms.animation.save("out.gif",dpi = 70, writer="imagemagick")
    plt.show()


