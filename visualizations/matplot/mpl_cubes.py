import matplotlib.pyplot as plt 

input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]
plt.plot(input_values, cubes, linewidth=5)

# Set chart title and label axes.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()
