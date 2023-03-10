import matplotlib.pyplot as plt

# Plot the first 5 cubic numbers
input_values1 = [1, 2, 3, 4, 5]
cubes1 = [1, 8, 27, 64, 125]

# Plot the first 5000 cubic numbers
input_values2 = list(range(1, 5001))
cubes2 = [x**3 for x in input_values2]

# Make a plot
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Plot the first 5 cubic numbers
ax.plot(input_values1, cubes1, label='First 5 Cubic Numbers')

# Plot the first 5000 cubic numbers
ax.plot(input_values2, cubes2, alpha=0.5, label='First 5000 Cubic Numbers')

# Set chart title and label axes.
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cubes of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Add legend
ax.legend()

# Show plot.
plt.show()
