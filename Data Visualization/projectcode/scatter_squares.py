import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


"""
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
"""

plt.style.use('seaborn')
fig, ax = plt.subplots()
# Using a Colormap
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# Defining Custom Colors
# ax.scatter(x_values, y_values, c='red', s=10)
# green:
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
# ---
# ax.scatter(x_values, y_values, s=10)
# ax.scatter(x_values, y_values, s=100)
# ax.scatter(2, 4, s=200)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()
# saves the figure.
# plt.savefig('savefig_plot2.png', bbox_inches='tight')
