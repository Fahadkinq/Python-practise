import matplotlib.pyplot as plt

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x_values, y_values, color='blue', marker='o')

# Set labels for x and y axis
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set title for the plot
plt.title('Simple Scatter Plot')

# Display the plot
plt.grid(True)
plt.show()
