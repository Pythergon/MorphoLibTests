# # Import Library
# import morpholib as morpho
# morpho.importAll()
#
# # Define Function
# def f(x):
#     return x*x
#
# # Get the points
# points = []
#
# ## What is linespace?
# ## Line space takes 3 parameters
# ## Start val, end val, and step amount
# ## So in this case it will take 100 different equally spaced intervals between -5 & 5
# for x in morpho.space.linspace(-5, 5, 100):
#     y = f(x)
#     points.append(morpho.Point(x, y))
#
# # Create the curve of the function as an object
# plot = morpho.Path(points)
# plot.color = morpho.blue
#
# # Time for displaying!
# ## Make animation object
# anim = morpho.Animation()
# ## Create layer to display the curve
# layer = morpho.Layer(actors=[plot])
# ## Add the layer "layer" to animation object
# anim.addLayer(layer)
# ## Start the display!
# morpho.play()

import morpholib as morpho


# Define the function to be graphed.
# We are plotting f(x) = x**2
def f(x):
    return x ** 2


def main():
    # Create a new figure with a default size.
    fig = morpho.Figure()

    # Add a new plotting axis to the figure.
    ax = fig.new_axis()

    # Create a graph object for the function.
    # We specify the function, the range of x-values, and the color of the graph.
    graph = morpho.Graph(f, xlim=(-3, 3), color=morpho.blue)

    # Add the graph to the axis.
    ax.add_graph(graph)

    # Set the title and labels for the axes.
    ax.title = "Graph of $f(x) = x^2$"
    ax.xlabel = "x"
    ax.ylabel = "y"

    # Add a grid to the background for better visualization.
    ax.grid = True

    # Display the figure.
    # The figure window will remain open until closed by the user.
    morpho.show_figure(fig)


if __name__ == "__main__":
    main()
