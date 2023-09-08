import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import squarify
from matplotlib.sankey import Sankey

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Function to perform integration
def integrate(expression, var):
    try:
        result = sp.integrate(expression, var)
        return result
    except Exception as e:
        return str(e)

# Function to perform differentiation
def differentiate(expression, var):
    try:
        result = sp.diff(expression, var)
        return result
    except Exception as e:
        return str(e)

# Function to plot a pie chart
def plot_pie_chart(data, labels):
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart')
    plt.show()

# Function to plot a bar chart
def plot_bar_chart(x_labels, data):
    x = np.arange(len(x_labels))
    plt.bar(x, data)
    plt.xticks(x, x_labels)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart')
    plt.show()

# Function to plot a histogram
def plot_histogram(data, num_bins):
    plt.hist(data, bins=num_bins, alpha=0.5, color='b', edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

# Function to plot a line chart
def plot_line_chart(x, y):
    plt.plot(x, y, marker='o', linestyle='-')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Line Chart')
    plt.grid(True)
    plt.show()

# Function to plot a scatter plot
def plot_scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Scatter Plot')
    plt.grid(True)
    plt.show()

# Function to plot a box plot
def plot_box_plot(data):
    plt.boxplot(data)
    plt.xlabel('Data')
    plt.ylabel('Value')
    plt.title('Box Plot')
    plt.grid(True)
    plt.show()

# Function to plot a violin plot
def plot_violin_plot(data):
    plt.violinplot(data, showmedians=True)
    plt.xlabel('Data')
    plt.ylabel('Value')
    plt.title('Violin Plot')
    plt.grid(True)
    plt.show()

# Function to plot a heatmap
def plot_heatmap(data):
    plt.imshow(data, cmap='viridis', aspect='auto')
    plt.colorbar()
    plt.title('Heatmap')
    plt.show()

# Function to plot a 3D scatter plot
def plot_3d_scatter(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_zlabel('Z-Axis')
    ax.set_title('3D Scatter Plot')
    plt.show()

# Function to plot a radar chart
def plot_radar_chart(categories, values):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    num_categories = len(categories)
    values += values[:1]  # Close the circle
    angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
    angles += angles[:1]

    ax.fill(angles, values, 'b', alpha=0.1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title('Radar Chart')
    plt.show()

# Function to plot a network graph
def plot_network_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, font_color='black', font_weight='bold', node_color='skyblue')
    plt.title('Network Graph')
    plt.show()

# Function to plot a polar plot
def plot_polar_plot(theta, r):
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r)
    ax.set_rmax(max(r))
    ax.set_title('Polar Plot')
    plt.show()

# Function to plot error bars
def plot_error_bars(x, y, error):
    plt.errorbar(x, y, yerr=error, fmt='o', capsize=5)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Error Bars Plot')
    plt.grid(True)
    plt.show()

# Function to plot a contour plot
def plot_contour_plot(x, y, z):
    plt.contour(x, y, z, cmap='viridis')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Contour Plot')
    plt.colorbar()
    plt.grid(True)
    plt.show()

# Function to plot a quiver plot
def plot_quiver_plot(x, y, u, v):
    plt.quiver(x, y, u, v)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Quiver Plot')
    plt.grid(True)
    plt.show()

# Function to plot a streamplot
def plot_streamplot(x, y, u, v):
    plt.streamplot(x, y, u, v)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Streamplot')
    plt.grid(True)
    plt.show()

# Function to plot a hexbin plot
def plot_hexbin_plot(x, y, gridsize=30):
    plt.hexbin(x, y, gridsize=gridsize, cmap='viridis')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Hexbin Plot')
    plt.colorbar()
    plt.grid(True)
    plt.show()

# Function to plot a Sankey diagram
def plot_sankey_diagram(labels, source, target, value):
    fig, ax = plt.subplots()
    sankey = Sankey(ax=ax, scale=1.0)
    sankey.add(flows=value,
               labels=labels,
               orientations=[0, 1, -1, -1],
               pathlengths=[0, 0, 0.5, 1.0])
    sankey.finish()
    plt.title('Sankey Diagram')
    plt.show()

# Function to plot a Treemap
def plot_treemap(labels, sizes):
    plt.figure(figsize=(8, 6))
    squarify.plot(sizes=sizes, label=labels, alpha=0.6)
    plt.axis('off')
    plt.title('Treemap')
    plt.show()

# Main function to run the calculator
def main():
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'integrate' for integration")
        print("Enter 'differentiate' for differentiation")
        print("Enter 'plot_pie' for pie chart")
        print("Enter 'plot_bar' for bar chart")
        print("Enter 'plot_hist' for histogram")
        print("Enter 'plot_line' for line chart")
        print("Enter 'plot_scatter' for scatter plot")
        print("Enter 'plot_box' for box plot")
        print("Enter 'plot_violin' for violin plot")
        print("Enter 'plot_heatmap' for heatmap")
        print("Enter 'plot_3d_scatter' for 3D scatter plot")
        print("Enter 'plot_radar' for radar chart")
        print("Enter 'plot_network' for network graph")
        print("Enter 'plot_polar' for polar plot")
        print("Enter 'plot_error_bars' for error bars plot")
        print("Enter 'plot_contour' for contour plot")
        print("Enter 'plot_quiver' for quiver plot")
        print("Enter 'plot_streamplot' for streamplot")
        print("Enter 'plot_hexbin' for hexbin plot")
        print("Enter 'plot_sankey' for Sankey diagram")
        print("Enter 'plot_treemap' for Treemap")
        print("Enter 'quit' to end the program")

        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ["add", "subtract", "multiply", "divide"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                print("Result: ", add(num1, num2))
            elif user_input == "subtract":
                print("Result: ", subtract(num1, num2))
            elif user_input == "multiply":
                print("Result: ", multiply(num1, num2))
            elif user_input == "divide":
                print("Result: ", divide(num1, num2))
        elif user_input in ["integrate", "differentiate"]:
            expression_str = input("Enter an expression in terms of 'x': ")
            var = sp.symbols('x')
            expression = sp.sympify(expression_str)
            
            if user_input == "integrate":
                result = integrate(expression, var)
                print("Result: ", result)
            elif user_input == "differentiate":
                result = differentiate(expression, var)
                print("Result: ", result)
        elif user_input in ["plot_pie", "plot_bar", "plot_hist", "plot_line", "plot_scatter", "plot_box", "plot_violin", "plot_heatmap"]:
            data_str = input("Enter data (comma-separated values): ")
            data = [float(x) for x in data_str.split(',')]
            if user_input == "plot_pie":
                labels_str = input("Enter labels (comma-separated values): ")
                labels = labels_str.split(',')
                plot_pie_chart(data, labels)
            elif user_input == "plot_bar":
                x_labels_str = input("Enter labels for the categories (comma-separated values): ")
                x_labels = x_labels_str.split(',')
                plot_bar_chart(x_labels, data)
            elif user_input == "plot_hist":
                num_bins = int(input("Enter the number of bins: "))
                plot_histogram(data, num_bins)
            elif user_input == "plot_line":
                x_str = input("Enter x-values (space-separated values): ")
                y_str = input("Enter y-values (space-separated values): ")
                x = [float(val) for val in x_str.split()]
                y = [float(val) for val in y_str.split()]
                plot_line_chart(x, y)
            elif user_input == "plot_scatter":
                y_str = input("Enter y-values (space-separated values): ")
                y = [float(val) for val in y_str.split()]
                plot_scatter_plot(data, y)
            elif user_input == "plot_box":
                plot_box_plot(data)
            elif user_input == "plot_violin":
                plot_violin_plot(data)
            elif user_input == "plot_heatmap":
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                data_matrix = [data[i:i+cols] for i in range(0, len(data), cols)]
                plot_heatmap(data_matrix)
        elif user_input == "plot_3d_scatter":
            x_str = input("Enter x-values (space-separated values): ")
            y_str = input("Enter y-values (space-separated values): ")
            z_str = input("Enter z-values (space-separated values): ")
            x = [float(val) for val in x_str.split()]
            y = [float(val) for val in y_str.split()]
            z = [float(val) for val in z_str.split()]
            plot_3d_scatter(x, y, z)
        elif user_input == "plot_radar":
            categories_str = input("Enter categories (comma-separated values): ")
            values_str = input("Enter values (comma-separated values): ")
            categories = categories_str.split(',')
            values = [float(val) for val in values_str.split(',')]
            plot_radar_chart(categories, values)
        elif user_input == "plot_network":
            nodes_str = input("Enter nodes (comma-separated values): ")
            edges_str = input("Enter edges (pairs of nodes separated by spaces): ")
            nodes = nodes_str.split(',')
            edges = [tuple(pair.split()) for pair in edges_str.split()]
            plot_network_graph(nodes, edges)
        elif user_input == "plot_polar":
            theta_str = input("Enter theta values (space-separated values): ")
            r_str = input("Enter r values (space-separated values): ")
            theta = [float(val) for val in theta_str.split()]
            r = [float(val) for val in r_str.split()]
            plot_polar_plot(theta, r)
        elif user_input == "plot_error_bars":
            x_str = input("Enter x-values (space-separated values): ")
            y_str = input("Enter y-values (space-separated values): ")
            error_str = input("Enter error values (space-separated values): ")
            x = [float(val) for val in x_str.split()]
            y = [float(val) for val in y_str.split()]
            error = [float(val) for val in error_str.split()]
            plot_error_bars(x, y, error)
        elif user_input == "plot_contour":
            x_str = input("Enter x-values (space-separated values): ")
            y_str = input("Enter y-values (space-separated values): ")
            z_str = input("Enter z-values (space-separated values): ")
            x = [float(val) for val in x_str.split()]
            y = [float(val) for val in y_str.split()]
            z = [float(val) for val in z_str.split()]
            plot_contour_plot(x, y, z)
        elif user_input == "plot_quiver":
            x_str = input("Enter x-values (space-separated values): ")
            y_str = input("Enter y-values (space-separated values): ")
            u_str = input("Enter u-values (space-separated values): ")
            v_str = input("Enter v-values (space-separated values): ")
            x = [float(val) for val in x_str.split()]
            y = [float(val) for val in y_str.split()]
            u = [float(val) for val in u_str.split()]
            v = [float(val) for val in v_str.split()]
            plot_quiver_plot(x, y, u, v)
        elif user_input == "plot_streamplot":
            x_str = input("Enter x-values (space-separated values): ")
            y_str = input("Enter y-values (space-separated values): ")
            u_str = input("Enter u-values (space-separated values): ")
            v_str = input("Enter v-values (space-separated values): ")
            x = [float(val) for val in x_str.split()]
            y = [float(val) for val in y_str.split()]
            u = [float(val) for val in u_str.split()]
            v = [float(val) for val in v_str.split()]
            plot_streamplot(x, y, u, v)
        elif user_input == "plot_hexbin":
            x_str = input("Enter x-values (space-separated values): ")
            y_str = input("Enter y-values (space-separated values): ")
            gridsize = int(input("Enter gridsize: "))
            x = [float(val) for val in x_str.split()]
            y = [float(val) for val in y_str.split()]
            plot_hexbin_plot(x, y, gridsize)
        elif user_input == "plot_sankey":
            labels_str = input("Enter labels (comma-separated values): ")
            source_str = input("Enter source nodes (comma-separated values): ")
            target_str = input("Enter target nodes (comma-separated values): ")
            value_str = input("Enter flow values (comma-separated values): ")
            labels = labels_str.split(',')
            source = source_str.split(',')
            target = target_str.split(',')
            value = [float(val) for val in value_str.split(',')]
            plot_sankey_diagram(labels, source, target, value)
        elif user_input == "plot_treemap":
            labels_str = input("Enter labels (comma-separated values): ")
            sizes_str = input("Enter sizes (comma-separated values): ")
            labels = labels_str.split(',')
            sizes = [float(val) for val in sizes_str.split(',')]
            plot_treemap(labels, sizes)
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
