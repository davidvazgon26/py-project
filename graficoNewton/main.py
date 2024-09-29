import matplotlib
matplotlib.use('Agg')  # Cambia a un backend no interactivo
import matplotlib.pyplot as plt
import numpy as np

# Escala: 1 cm = 25 Newtons
scale = 1 / 25

# Angulos en grados
angles_deg = [60, 50, -30, -90, -160]

# Magnitudes en Newtons
forces = [250, 150, 125, 200, 100]

# Convertir magnitudes a cm
forces_cm = [f * scale for f in forces]

# Convertir angulos a radianes
angles_rad = [np.deg2rad(angle) for angle in angles_deg]

# Paso 1: Punto de Inicio
plt.figure(figsize=(8, 8))
plt.title("Paso 1: Punto de Inicio")
plt.xlabel("X (cm)")
plt.ylabel("Y (cm)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter(0, 0, color='red')  # Punto de inicio
plt.text(0, 0, "Inicio", fontsize=12, verticalalignment='bottom')
plt.savefig('paso1.png')  # Guardar la imagen como paso1.png

# Paso 2: Primera Fuerza - 250 Newtons a 60 grados hacia el norte del este
x1, y1 = forces_cm[0] * np.cos(angles_rad[0]), forces_cm[0] * np.sin(angles_rad[0])

plt.figure(figsize=(8, 8))
plt.title("Paso 2: Primera Fuerza")
plt.xlabel("X (cm)")
plt.ylabel("Y (cm)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter(0, 0, color='red')  # Punto de inicio
plt.quiver(0, 0, x1, y1, angles='xy', scale_units='xy', scale=1, color='blue', width=0.005)
plt.text(x1, y1, "250N", fontsize=12, verticalalignment='bottom')
plt.xlim(-2, 12)
plt.ylim(-2, 12)
plt.savefig('paso2.png')  # Guardar la imagen como paso2.png

# Paso 3: Segunda Fuerza - 150 Newtons a 50 grados hacia el norte del este desde el punto del paso 2
x2, y2 = x1 + forces_cm[1] * np.cos(angles_rad[1]), y1 + forces_cm[1] * np.sin(angles_rad[1])

plt.figure(figsize=(8, 8))
plt.title("Paso 3: Segunda Fuerza")
plt.xlabel("X (cm)")
plt.ylabel("Y (cm)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter([0, x1], [0, y1], color='red')  # Puntos de inicio y después de la primera fuerza
plt.quiver(0, 0, x1, y1, angles='xy', scale_units='xy', scale=1, color='blue', width=0.005)
plt.quiver(x1, y1, forces_cm[1] * np.cos(angles_rad[1]), forces_cm[1] * np.sin(angles_rad[1]), 
           angles='xy', scale_units='xy', scale=1, color='green', width=0.005)
plt.text(x1, y1, "250N", fontsize=12, verticalalignment='bottom')
plt.text(x2, y2, "150N", fontsize=12, verticalalignment='bottom')
plt.xlim(-2, 15)
plt.ylim(-2, 15)
plt.savefig('paso3.png')  # Guardar la imagen como paso3.png

# Paso 4: Tercera Fuerza - 125 Newtons a 30 grados hacia el sur del este
x3, y3 = x2 + forces_cm[2] * np.cos(angles_rad[2]), y2 + forces_cm[2] * np.sin(angles_rad[2])

plt.figure(figsize=(8, 8))
plt.title("Paso 4: Tercera Fuerza")
plt.xlabel("X (cm)")
plt.ylabel("Y (cm)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter([0, x2], [0, y2], color='red')  # Puntos de inicio y después de la segunda fuerza
plt.quiver(0, 0, x2, y2, angles='xy', scale_units='xy', scale=1, color='blue', width=0.005)
plt.quiver(x2, y2, forces_cm[2] * np.cos(angles_rad[2]), forces_cm[2] * np.sin(angles_rad[2]), 
           angles='xy', scale_units='xy', scale=1, color='orange', width=0.005)
plt.text(x2, y2, "150N", fontsize=12, verticalalignment='bottom')
plt.text(x3, y3, "125N", fontsize=12, verticalalignment='bottom')
plt.xlim(-2, 15)
plt.ylim(-15, 2)
plt.savefig('paso4.png')  # Guardar la imagen como paso4.png

# Paso 5: Cuarta Fuerza - 200 Newtons hacia el sur
x4, y4 = x3, y3 - forces_cm[3]

plt.figure(figsize=(8, 8))
plt.title("Paso 5: Cuarta Fuerza")
plt.xlabel("X (cm)")
plt.ylabel("Y (cm)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter([0, x3], [0, y3], color='red')  # Puntos de inicio y después de la tercera fuerza
plt.quiver(0, 0, x3, y3, angles='xy', scale_units='xy', scale=1, color='blue', width=0.005)
plt.quiver(x3, y3, 0, -forces_cm[3], angles='xy', scale_units='xy', scale=1, color='purple', width=0.005)
plt.text(x3, y3, "125N", fontsize=12, verticalalignment='bottom')
plt.text(x4, y4, "200N", fontsize=12, verticalalignment='bottom')
plt.xlim(-2, 15)
plt.ylim(-20, 2)
plt.savefig('paso5.png')  # Guardar la imagen como paso5.png

# Paso 6: Quinta Fuerza - 100 Newtons a 70 grados hacia el oeste del sur
x5, y5 = x4 - forces_cm[4] * np.cos(np.deg2rad(70)), y4 - forces_cm[4] * np.sin(np.deg2rad(70))

plt.figure(figsize=(8, 8))
plt.title("Paso 6: Quinta Fuerza")
plt.xlabel("X (cm)")
plt.ylabel("Y (cm)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter([0, x4], [0, y4], color='red')  # Puntos de inicio y después de la cuarta fuerza
plt.quiver(0, 0, x4, y4, angles='xy', scale_units='xy', scale=1, color='blue', width=0.005)
plt.quiver(x4, y4, -forces_cm[4] * np.cos(np.deg2rad(70)), -forces_cm[4] * np.sin(np.deg2rad(70)), 
           angles='xy', scale_units='xy', scale=1, color='brown', width=0.005)
plt.text(x4, y4, "200N", fontsize=12, verticalalignment='bottom')
plt.text(x5, y5, "100N", fontsize=12, verticalalignment='bottom')
plt.xlim(-20, 15)
plt.ylim(-25, 2)
plt.savefig('paso6.png')  # Guardar la imagen como paso6.png
