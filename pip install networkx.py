pip install networkx
import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo direcionado
G = nx.DiGraph()

# Adicionar arestas (fases) ao grafo com os respectivos pesos (distâncias)
G.add_edge('Torre', '1', weight=2)
G.add_edge('Torre', '2', weight=5)
G.add_edge('Torre', '3', weight=4)
G.add_edge('1', '4', weight=1)
G.add_edge('1', '5', weight=2)
G.add_edge('2', '5', weight=3)
G.add_edge('3', '6', weight=2)
G.add_edge('4', '7', weight=4)
G.add_edge('5', '7', weight=1)
G.add_edge('5', '8', weight=3)
G.add_edge('6', '8', weight=4)
G.add_edge('7', '9', weight=2)
G.add_edge('8', '9', weight=3)
G.add_edge('8', '10', weight=2)
G.add_edge('9', '11', weight=1)
G.add_edge('10', '11', weight=3)

# Calcular o menor caminho usando o algoritmo de Dijkstra
start_node = 'Torre'
shortest_paths = nx.single_source_dijkstra_path_length(G, start_node)

# Mostrar os resultados
print("Menor caminho a partir da Torre:")
for node, distance in shortest_paths.items():
    print(f"{node}: {distance}")

# Desenhar o grafo para visualização
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
