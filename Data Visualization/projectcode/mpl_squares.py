import matplotlib.pyplot as plt

# in the terminal
# import matplotlib.pyplot as plt
# plt.style.available to look up the list of available styles in matplotlib

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.plot(squares)
ax.plot(squares, linewidth=3)

# set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labes.
ax.tick_params(axis="both", labelsize=14)

plt.show()
