import matplotlib.pyplot as plt

input_values1 = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# Make a plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values1, cubes, markeredgecolor='none', markersize=40)

# Set chart title and label axes.
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cubes of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Show plot.
plt.show()
