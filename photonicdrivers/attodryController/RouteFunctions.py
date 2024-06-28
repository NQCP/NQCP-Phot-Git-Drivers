import numpy as np






def spiral_path(centerX, centerY, dist, max_dist):
    
    num_coils = max_dist/ dist
     
    chord = dist     # distance between points
    radius = max_dist
    thetaMax = num_coils * 2 * np.pi   # value of theta corresponding to end of last coil
    awayStep = radius / thetaMax      # How far to step away from center for each side.

    theta = chord / awayStep
    
    xy_points = [[centerX, centerY]]
    
    while theta <= thetaMax:
        away = awayStep * theta   #  How far away from center
        around = theta   #  How far around from center

        x = centerX + np.cos (around) * away
        y = centerY + np.sin (around) * away

        xy_points.append([x,y])

        theta += chord / away
    
    return np.array(xy_points)





if  __name__ == "__main__":
    import matplotlib.pyplot as plt

    xy_points = spiral_path(0, 0, 0.5, 10)
    print(len(xy_points))

    dist = np.array([np.sqrt(xy[0]**2 + xy[1]**2) for xy in xy_points])

    plt.scatter(xy_points[:,0], xy_points[:,1], c = dist, cmap = 'seismic')
    plt.colorbar()
    plt.show()