from stl import mesh                # type: ignore
from mpl_toolkits import mplot3d    # type: ignore
from matplotlib import pyplot       # type: ignore

# Kreiranje novog plot-a
figure = pyplot.figure()
axes = figure.add_subplot(projection='3d')

# Učitavanje STL filea i dodavanje vektora u plot
vijak_mesh = mesh.Mesh.from_file('STL files/vijak2_2_8_zakrpano.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(vijak_mesh.vectors))

# Skalranje predmeta sa osima
scale = vijak_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Prikaz plota na ekran
pyplot.show()



