import numpy as np
import matplotlib.pyplot as plt
import random
import warnings
warnings.filterwarnings("ignore")

class Vertex:
    
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbors = {}
    
    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight
    
    def get_connections(self):
        return self.neighbors.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]
    
class Graph:
    
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        
    def add_vertex(self, vertex_id):
        self.num_vertices += 1
        new_vertex = Vertex(vertex_id)
        self.vert_dict[vertex_id] = new_vertex
    
    def get_vertex(self, vertex_id):
        return self.vert_dict.get(vertex_id)
    
    def get_n_vertices(self):
        return self.num_vertices

    def add_edge(self, from_vertex_id, to_vertex_id, weight = 0):
        '''
        
        a -------- b 
           weight
           
        '''
        a = from_vertex_id
        b = to_vertex_id
        
        if a in self.vert_dict and b in self.vert_dict:
            self.vert_dict[a].add_neighbor(b, weight)
            self.vert_dict[b].add_neighbor(a, weight)
        else:
            if a not in self.vert_dict:
                raise ValueError("Vertex from which you want to add edge doesn't exist. \
                                  Please, initialize it first.")
            elif b not in self.vert_dict:
                raise ValueError("Vertex to which you want to add edge doesn't exist. \
                                  Please, initialize it first.")
    
    def get_vertices(self):
        return self.vert_dict.keys()
    
    def create_coordinates(self):
        vertex_ids = self.get_vertices()
        n_vertices = len(vertex_ids)
        if n_vertices % 2 == 0:
            n = n_vertices // 2 

            x1 = np.linspace(-n,n,n)
            x2 = np.linspace(-(n-1),n-1,n)
            R = n
            y1 = [np.sqrt(R**2 - x_i**2) for x_i in x1]
            y2 = [-np.sqrt(R**2 - x_i**2) for x_i in x2]
        else:
            n = n_vertices // 2 

            x1 = np.linspace(-n,n,n)
            x2 = np.linspace(-(n-1),n-1,n+1)
            R = n
            y1 = [np.sqrt(R**2 - x_i**2) for x_i in x1]
            y2 = [-np.sqrt(R**2 - x_i**2) for x_i in x2]

        x = np.concatenate((x1, x2[::-1]), axis=None)
        y = np.concatenate((y1, y2[::-1]), axis=None)
        
        return x, y, R
        
    def plot_graph(self):
        
        x, y, R = self.create_coordinates()
        
        fig, ax = plt.subplots(figsize = (R,R))
        ax.scatter(x,y,s=22**2)
        for i in range(len(x)):
            ax.text(x[i], y[i], f"{i}", transform=ax.transData,ha='center', va='center',color='white')
            
        for vertex_id in self.vert_dict.keys():
            vertex = self.get_vertex(vertex_id)
            
            for neighbor_id in vertex.get_connections():
                weight = vertex.get_weight(neighbor_id)
                self.plot_edge(vertex_id, neighbor_id, weight)
                
        plt.savefig(f'graph_{self.num_vertices}.png')
    
    def plot_edge(self, frm, to, weight):
        x, y, _ = self.create_coordinates()
        plt.plot([x[frm], x[to]],[y[frm], y[to]],color='C0')
        mediana_x = (x[frm] + x[to])/2
        mediana_y = (y[frm] + y[to])/2
        if weight != 0:
            plt.text(mediana_x,mediana_y, f"{weight}",ha='left', va='bottom',color='black')
        
    def generate_random_graph(self, n_vertices=10, n_edges=10, weighted=False):
        vertex_ids = np.arange(n_vertices)
        for i in vertex_ids:
            self.add_vertex(i)
        
        for _ in range(n_edges):
            if weighted:
                weight = random.randint(0, n_edges)
            else:
                weight = 0
            from_vertex_id, to_vertex_id = np.random.choice(n_vertices,(2,1),replace=False) 
            self.add_edge(from_vertex_id[0], to_vertex_id[0], weight) 
            
    def create_adjacency_matrix(self):
        adjacency_matrix = np.zeros((self.num_vertices,self.num_vertices))
        for vertex_id in range(self.num_vertices):
            vertex = self.get_vertex(vertex_id)
            neighbors = list(vertex.get_connections())
            adjacency_matrix[vertex_id,neighbors] += 1
        return adjacency_matrix