import numpy as np

def f(x: float, y: float) -> float:
    """
    Calculates the value of the "f" function at given x and y coordinates.

    Parameters:
    - x (float): The x-coordinate.
    - y (float): The y-coordinate.

    Returns:
    - z (float): The value of the "f" function at (x, y).
    """
    z = np.sin(x) + np.cos(y)
    return z

x = np.linspace(-3, 3, 201)
y = np.linspace(-3, 3, 201)

def df_x(x, y):
    """
    Calculates the partial derivative of the "f" function with respect to x.

    Parameters:
    - x (float): The x-coordinate.
    - y (float): The y-coordinate.

    Returns:
    - df (float): The partial derivative of the "f" function with respect to x at (x, y).
    """
    return np.cos(x)

def df_y(x: float, y: float) -> float:
    """
    Calculates the partial derivative of the "f" function with respect to y.

    Parameters:
    - x (float): The x-coordinate.
    - y (float): The y-coordinate.

    Returns:
    - df (float): The partial derivative of the "f" function with respect to y at (x, y).
    """
    return -np.sin(y)

localmin = np.random.rand(2) * 4 - 2
startpnt = localmin[:]

learning_rate = 0.01
training_epochs = 1000

trajectory = np.zeros((training_epochs, 2))

for i in range(training_epochs):
    grad = np.array([
        df_x(localmin[0], localmin[1]), 
        df_y(localmin[0], localmin[1])])
    localmin = localmin - grad * learning_rate
    trajectory[i, :] = localmin

print("Local minimum:", localmin)
print("Starting point:", startpnt)
print("Trajectory:", trajectory)

# Plot the function and trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.plot(trajectory[:, 0], trajectory[:, 1], f(trajectory[:, 0], trajectory[:, 1]), 'r.-')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
