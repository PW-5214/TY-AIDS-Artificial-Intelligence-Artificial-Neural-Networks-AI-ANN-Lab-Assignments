def create_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    
    for _ in range(n):
        node = input("Enter node name: ")
        graph[node] = []

    print("Enter edges like 'A B'. Type 'done' when finished:")
    while True:
        edge = input("Enter edge: ")
        if edge.lower() == "done":
            break
        u, v = edge.split()
        if u in graph and v in graph:
            graph[u].append(v)
            graph[v].append(u)
        else:
            print("Invalid edge.")
    
    return graph

def is_safe(node, graph, color_map, color):
    for neighbor in graph[node]:
        if color_map.get(neighbor) == color:
            return False
    return True

def color_graph(graph, colors, node_list, color_map):
    if not node_list:
        return True

    node = node_list[0]
    for color in colors:
        if is_safe(node, graph, color_map, color):
            color_map[node] = color
            if color_graph(graph, colors, node_list[1:], color_map):
                return True
            del color_map[node]  # Backtrack
    return False

# Main
graph = create_graph()
colors = ["Red", "Green", "Blue", "Yellow"]
nodes = sorted(graph, key=lambda n: len(graph[n]), reverse=True)
color_map = {}

if color_graph(graph, colors, nodes, color_map):
    print("Coloring result:")
    for node in color_map:
        print(f"{node}: {color_map[node]}")
else:
    print("No valid coloring found.")
