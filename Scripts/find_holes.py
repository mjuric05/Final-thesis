import numpy as np                                          # type: ignore
from stl import mesh                                        # type: ignore
import matplotlib.pyplot as plt                             # type: ignore
from mpl_toolkits.mplot3d.art3d import Poly3DCollection     # type: ignore

# Učitavanje STL datoteke
file_path = 'STL files/vijak2_2_8.stl'
vijak_mesh = mesh.Mesh.from_file(file_path)

# Prikupljanje svih trokuta iz STL datoteke
triangles = vijak_mesh.vectors

# Funkcija za detekciju šupljina
def find_holes(triangles):
    # Pronalazak svih rubova sa jednim "rubom"
    edges = {}
    for triangle in triangles:
        for i in range(3):
            edge = tuple(sorted((tuple(triangle[i]), tuple(triangle[(i + 1) % 3]))))
            if edge in edges:
                edges[edge] += 1
            else:
                edges[edge] = 1
    
    # Pronalaženje rubova koje se pojavljuju samo jednom, tj. šupljina
    bound_edges = [edge for edge, count in edges.items() if count == 1]
    
    return bound_edges

# Pronalazak šupljina kroz funkciju find_holes
holes = find_holes(triangles)

# Funkcija za crtanje STL modela i šupljina
def plot_screw_and_holes(triangles, holes):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Crtanje svih trokuta u plavoj boji tako da vijak bude plave boje
    ax.add_collection3d(Poly3DCollection(triangles, color='blue', alpha=0.3, linewidths=0.2, edgecolor='b'))
    
    # Crtanje šupljina tj. rubnih rubova sa crvenim rubovima kako bi vidjeli razliku
    for edge in holes:
        edge = np.array(edge)
        ax.plot(edge[:, 0], edge[:, 1], edge[:, 2], color='red', linewidth=2)
    
    # Podesavanje koordinatnih osiju
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Skaliranje
    scale = triangles.flatten(order='C')
    ax.auto_scale_xyz(scale, scale, scale)
    
    plt.show()

# Prikazivanje modela sa vijka sa šupljinama
plot_screw_and_holes(triangles, holes)      


