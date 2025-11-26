import numpy as np
def create_array(shape, value):
    """Create a NumPy array of given shape filled with the specified value.

    Args:
        shape (tuple): The shape of the array to create.
        value (float): The value to fill the array with.

    Returns:
        np.ndarray: A NumPy array of the specified shape filled with the given value.
    """
    return np.full(shape, value)
# Example usage:
array = create_array((3, 4), 7.5)
print(array)