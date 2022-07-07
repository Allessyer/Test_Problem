from graph import *
import numpy as np
import matplotlib.pyplot as plt
import random
import warnings
warnings.filterwarnings("ignore")

def create_invitation_list_(guests):
    adjacency_matrix = guests.create_adjacency_matrix()
    n_guests = guests.get_n_vertices()
    invitation_list = []
    
    max_friendly = 0
    min_n_enemies = n_guests
    all_ids = np.arange(n_guests)
    while np.any(all_ids):
        for guest_id in all_ids:
            check_row = adjacency_matrix[guest_id, all_ids]
            n_enemies = np.sum(check_row)

            if n_enemies <  min_n_enemies:
                min_n_enemies = n_enemies
                max_friendly = guest_id
                friends = np.where(check_row == 0)[0]
                real_friends = all_ids[[friends]]
                real_friends = real_friends[real_friends != max_friendly] # delete himself

        all_ids = real_friends
        invitation_list.append(max_friendly)
        max_friendly = 0
        min_n_enemies = n_guests
    
    return invitation_list

if __name__ == '__main__':
    
    n_vertices = random.randint(2, 100)
    n_edges = random.randint(0, n_vertices**2)
    
    guests = Graph()
    guests.generate_random_graph(n_vertices, n_edges,weighted=False)
    guests.plot_graph()
    
    invitation_list = create_invitation_list_(guests)
    print("INVITATION LIST: ", invitation_list)
    