import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # For a linegraph    
    plt.plot(rw.x_values, rw.y_values, linewidth=5)

    # Emphasize the first and last points.
    plt.scatter(0,0, c='green', edgecolors='none', s=500)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=500)

    # Remove the axes
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    # plt.show()
    plt.savefig('random_walk_positive.png', bbox_inches='tight')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break