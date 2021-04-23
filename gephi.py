import igraph as ig
from pyvis.network import Network
import IPython


def main():
    #load graph
    G=ig.Graph.Read_GraphML('gameOfThrones2.graphml', False)

    net = Network(height='600px', width='600px', bgcolor='rgba(0,0,0,0)',font_color='white')
    #adding the nodes
    for v in G.vs:
        net.add_node(v['id'], size=v['size'] * 0.75, label=v['label'],
                     color="rgb(" + str(v['r']) + "," + str(v['g']) + "," + str(v['b']) + ")",
                     x=v['x'], y=v['y'], borderWidth=0)
    #adding the edges
    id = G.vs['id']
    for e in G.es:
        net.add_edge(id[e.source], id[e.target], width=e['weight'] * 0.1 + 0.1)

    # Draw the graph to an HTML file
    net.show('nx.html')

    IPython.display.HTML(filename='nx.html')





if __name__ == "__main__":
        main()