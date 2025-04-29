

def min_stack_cost(initial_height, final_height, push_cost, pop_cost):
    """
    Calculates the minimum cost to manage a stack of bricks.

    Args:
        initial_height: The initial number of bricks in the stack.
        final_height: The desired final number of bricks in the stack.
        push_cost: The cost to add a brick to the stack.
        pop_cost: The cost to remove a brick from the stack.

    Returns:
        The minimum cost to reach the final height from the initial height.
    """
    if initial_height == final_height:
        return 0
    elif initial_height < final_height:
        return (final_height - initial_height) * push_cost
    else:
        return (initial_height - final_height) * pop_cost
# Example usage:
initial_height = 3
final_height = 1
push_cost = 6
pop_cost = 4

min_cost = min_stack_cost(initial_height, final_height, push_cost, pop_cost)
print(f"The minimum cost is: {min_cost}")

#------------------

def min_cost_adjust_bricks(x, y, cost_add, cost_remove):
    """
    Calculates the minimum cost to adjust brick stacks from initial heights x to target heights y.

    Args:
        x: A list of initial brick stack heights.
        y: A list of target brick stack heights.
        cost_add: The cost to add one brick to a stack.
        cost_remove: The cost to remove one brick from a stack.

    Returns:
        The minimum cost to adjust the brick stacks.
    """
    if len(x) != len(y):
        raise ValueError("Initial and target height lists must have the same length.")

    total_cost = 0
    for i in range(len(x)):
        diff = y[i] - x[i]
        if diff > 0:
            total_cost += diff * cost_add
        elif diff < 0:
            total_cost += abs(diff) * cost_remove

    return total_cost

# Example usage:
initial_heights = [3, 1, 1]
target_heights = [1, 2, 2]
add_cost = 6
remove_cost = 4

min_cost = min_cost_adjust_bricks(initial_heights, target_heights, add_cost, remove_cost)
print(f"The minimum cost to adjust the stacks is: {min_cost}") # Output: 13










