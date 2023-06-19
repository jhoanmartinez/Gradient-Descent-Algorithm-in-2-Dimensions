# Gradient-Descent-Algorithm-in-2-Dimensions

The Gradient Descent algorithm is an iterative optimization algorithm used to find the minimum of a function. In this implementation, we focus on finding the local minimum of a function in a 2-dimensional space.

# Introduction

The Gradient Descent algorithm is an iterative optimization algorithm used to find the minimum of a function. It is widely used in various machine learning and optimization tasks. This implementation focuses on finding the local minimum of a function in a 2-dimensional space.

The algorithm starts with an initial point in the 2-dimensional space and iteratively updates the current point by taking steps proportional to the negative gradient of the function. By moving in the direction of the steepest descent, the algorithm converges to a local minimum.

This README provides an overview of the implementation, its usage, and an example to help you get started with the Gradient Descent algorithm in 2 dimensions.

# Usage

To use the Gradient Descent algorithm in 2 dimensions, follow these steps:

1. Define the function you want to minimize. This function should take two variables as inputs, representing the coordinates in the 2-dimensional space.

2. Set the initial point where the algorithm will start the optimization process.

3. Choose the learning rate, which determines the step size taken at each iteration of the algorithm.

4. Set the maximum number of iterations to perform, or define a stopping criterion based on the convergence of the algorithm.

5. Call the Gradient Descent function with the function to minimize, the initial point, learning rate, and maximum number of iterations as inputs.

6. The algorithm will iteratively update the current point by moving in the direction of the steepest descent until convergence or the maximum number of iterations is reached.

7. The algorithm will return the final point where the local minimum was found.

# Example

  ```
  # Set initial point randomly
  localmin = np.random.rand(2) * 4 - 2
  startpnt = localmin[:] 
  
  # Set initial point static
  startpnt = [-0.5743824,  -1.84219917]

  # Set learning rate
  learning_rate = 0.01

  # Set maximum number of iterations
  max_iterations = 1000
  
  #run
  python gradient_descent_2d.py
  ```
 


# Notes

It is important to choose an appropriate learning rate to ensure convergence of the algorithm. If the learning rate is too large, the algorithm may overshoot the minimum and fail to converge. If the learning rate is too small, the algorithm may take a long time to converge.

- **The Gradient Descent algorithm can be extended to higher dimensions by modifying the function and the initial point accordingly.

- **This implementation assumes that the function to minimize is continuous and differentiable.

- **Feel free to experiment with different functions, initial points, learning rates, and maximum iterations to see how the algorithm performs.

# License

This repository is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute the code for personal or commercial purposes.
