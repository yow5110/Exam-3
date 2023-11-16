import numpy as np
import matplotlib.pyplot as plt

def rw2d(x0,y0,Nstep):
    #Paste your single-particle random walk code here 
    # that generates x_traj and y_traj starting from the origin
    
    #Generate the trajectories starting from x0 and y0
    x_traj_shifted = 
    y_traj_shifted = 
    
    #We will return a 2D array of dimensions Nstep x 2.
    # .T stands for taking the transpose
    return np.array([x_traj_shifted, y_traj_shifted]).T

def check_intersec(traj, cluster):
    """
    traj: a 2D array with dimensions Nsteps x 2. Needs to be all integers.
    cluster: a 2D array with dimensions Cluster Size x 2. Needs to be all integers.
    
    Description: This function searches for the first time traj intersects with cluster.
    
    Returns: the index of traj immediately before the intersection,
    i.e. the element in traj to be appended to the growing cluster.
    If there is no intersection, it returns -1.
    """
    traj    = np.around(traj).astype(int)
    cluster = np.around(cluster).astype(int)
    traj = traj[:,0]+traj[:,1]*1j
    cluster= cluster[:,0] + cluster[:,1]*1j
    
    intersec = np.where(np.isin(traj,  cluster ))[0]
    idx = -1 #default return value
    if len(intersec) > 0:
        idx = intersec[0] - 1
        #to prevent accidentally returning negative values
        if idx < 0 : 
            idx = -1
    return idx
            
def dla():
    rng = np.random.default_rng()
    
    #This is our starting cluster, two particles at [0,0] and [0,1]
    cluster = np.array([[0,0],[0,1]])
    
    #Number of steps. If wait times are long, start with fewer steps.
    Nparticle = 10000 
    for i in range(Nparticle):
        #A progress monitor
        if i%100==0: print(int(i/Nparticle*100),'%')
        
        #Setup a starting radius spawn_radius from which particles will spawn 
        # and perform random walk.
        #It needs to be far enough from the growing cluster.
        #Among all the particles in the current cluster,
        #find the one with the furthest distance cluster_max_radius from the origin.
        #A good estimate for the radius of spawning particles is 2*cluster_max_radius.
        cluster_max_radius = 
        spawn_radius = 2*cluster_max_radius
        
        #Generate a random spawn coordinate x0,y0 somewhere on spawn_radius
        #and convert them into integers,
        #since check_intersec() only works for integers.
        x0 =
        y0 = 
        
        #Generate random walk trajector starting from x0,y0
        #We'll try 10000 steps.
        traj = rw2d(x0,y0,1e4)
        
        #This is a provided function that finds the correct coordinate 
        # where the particle sticks to the growing cluster.
        # Takes 2D arrays of dimensions Nstep x 2 and ClusterSize x 2 as input.
        #No need to worry about how it works.
        idx = check_intersec(traj, cluster)
        if idx >0:
            cluster = np.append(cluster, [traj[idx]],axis=0)
    
    r=100
    plt.figure()
    plt.xlim(-r,r)
    plt.ylim(-r,r)
    
    plt.plot(..., ...,  marker='.', linestyle='')
    plt.show()
    
dla()    
