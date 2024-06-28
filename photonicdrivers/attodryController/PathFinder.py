import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def find_route(xy_points, start_point_ix, dist_type = 'Euclidean', make_plot = True):
   
    points = xy_points
    num_points = len(points)
   
    distance_mat = np.zeros((num_points, num_points))
   
    for ix1 in range(num_points):
        for ix2 in range(ix1, num_points):
            point1 = points[ix1]
            point2 = points[ix2]
            if dist_type == 'Euclidean':
                dist = np.sqrt(np.sum((point1-point2)**2))
            elif dist_type == 'Manhattan':
                dist = np.sum(np.abs(point1-point2))
            distance_mat[ix1, ix2] = distance_mat[ix2, ix1] = dist

    explored_points = []
    points_left = list(range(num_points))

    current_point = start_point_ix
    explored_points.append(current_point)
    points_left.remove(current_point)

    total_dist = 0

    while points_left:
        distances_from_here = distance_mat[current_point][points_left]
        min_dist_ix = np.argmin(distances_from_here)
        this_dist = distances_from_here[min_dist_ix]

        #update to the ideantified neighbour
        current_point = points_left[min_dist_ix]
        explored_points.append(current_point)
        points_left.remove(current_point)  
        total_dist += this_dist
       
        xy_points_ordered = points[explored_points]


    if make_plot:
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect= (np.max(xy_points[:,0]) - np.min(xy_points[:,0]))/ (np.max(xy_points[:,1]) - np.min(xy_points[:,1])))

        ax.scatter(xy_points[:,0], xy_points[:,1])
        ax.scatter(xy_points[start_point_ix,0], xy_points[start_point_ix,1], c='red')

        # Create a continuous norm to map from data points to colors
        plot_points = np.array([xy_points_ordered[:,0], xy_points_ordered[:,1]]).T.reshape(-1, 1, 2)
        segments = np.concatenate([plot_points[:-1], plot_points[1:]], axis=1)

        norm = plt.Normalize(0, len(xy_points_ordered))
        lc = LineCollection(segments, cmap='turbo', norm=norm)
        # Set the values used for colormapping
        lc.set_array(range(len(xy_points_ordered)))
        line = ax.add_collection(lc)
        fig.colorbar(line, ax=ax, label='Step Number')
        ax.set_title('Total distance:' +str(total_dist))
        plt.show()  



    return xy_points_ordered, explored_points, total_dist




if  __name__ == "__main__":
    from itertools import product

                    

    # ############################

    # random
    num_points = 40
    points = np.random.rand(num_points, 2)

    # # on a grid
    # points = np.array([list(x) for x in product(range(10), repeat = 2)])

    # # on two grid2
    # # points0 = np.array([list(x) for x in product(range(20), repeat = 2)])
    # # points1 = points0 + np.array([40., 40.])
    # # points = np.concatenate([points0, points1])

    # ############################

    start_point_ix = 23

    dist_type = 'Euclidean'

    ############################


    xy_points_ordered, explored_points, total_dist = find_route(points, start_point_ix = start_point_ix, dist_type = 'Euclidean')




    
