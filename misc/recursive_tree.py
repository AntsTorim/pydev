import turtle

def recursive_tree(length, min_length=2):
    """
    Draws a recursive tree that is length points high,
    stops recursion if branches are below min_length
    """
    # Remember initial state
    rootx, rooty = turtle.pos()
    rootheading = turtle.heading()
    if length > min_length:
    # Recursive case
        # Draw the trunk
        turtle.forward(0.4*length)
        # Draw the left branch
        turtle.left(30)
        recursive_tree(0.5*length, min_length)
        # Draw the right branch
        turtle.right(80)
        recursive_tree(0.6*length, min_length)
    else:
    # End of recursion, limit
        turtle.forward(length)
    # Restore initial state
    turtle.setpos(rootx, rooty)
    turtle.setheading(rootheading)


if __name__ == "__main__":
    turtle.left(90)
    turtle.speed(3)
    recursive_tree(300, 10)
