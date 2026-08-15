import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

# Crear la bandera
fig, ax = plt.subplots(figsize=(12, 7))

# Dimensiones
flag_length = 3
flag_height = 2
half = flag_length / 2

# Colores
YELLOW = "#FCD116"
BLUE = "#003893"
RED = "#CE1126"
WHITE = "#FFFFFF"

# ==========================================
# COLOMBIA - MITAD IZQUIERDA
# ==========================================

ax.add_patch(Rectangle(
    (0, 1), half, 1,
    facecolor=YELLOW
))

ax.add_patch(Rectangle(
    (0, 0.5), half, 0.5,
    facecolor=BLUE
))

ax.add_patch(Rectangle(
    (0, 0), half, 0.5,
    facecolor=RED
))

# ==========================================
# VENEZUELA - MITAD DERECHA
# ==========================================

ax.add_patch(Rectangle(
    (half, 4/3), half, 2/3,
    facecolor=YELLOW
))

ax.add_patch(Rectangle(
    (half, 2/3), half, 2/3,
    facecolor=BLUE
))

ax.add_patch(Rectangle(
    (half, 0), half, 2/3,
    facecolor=RED
))

# ==========================================
# ESTRELLAS DE VENEZUELA
# ==========================================
# ==========================================
# ESTRELLAS DE VENEZUELA
# ==========================================

import math

center_x = half + half / 2
center_y = 0.82

star_radius = 0.07
star_distance = 0.30

# Arco de 8 estrellas
# El arco queda hacia arriba, dentro de la franja azul
for i in range(8):

    angle = 0.15 + i * (math.pi - 0.30) / 7

    x = center_x + star_distance * math.cos(angle)
    y = center_y + star_distance * math.sin(angle)

    points = []

    # Crear estrella de 5 puntas
    for j in range(10):

        if j % 2 == 0:
            radius = star_radius
        else:
            radius = star_radius * 0.4

        # Punta de la estrella hacia arriba
        a = math.pi / 2 + j * math.pi / 5

        points.append([
            x + radius * math.cos(a),
            y + radius * math.sin(a)
        ])

    ax.add_patch(
        Polygon(
            points,
            closed=True,
            facecolor=WHITE,
            edgecolor=WHITE
        )
    )

# ==========================================
# LÍNEA CENTRAL
# ==========================================

ax.plot(
    [half, half],
    [0, flag_height],
    color="black",
    linewidth=2
)

# Configuración
ax.set_xlim(0, flag_length)
ax.set_ylim(0, flag_height)
ax.set_aspect("equal")
ax.axis("off")

plt.tight_layout()

# Guardar como imagen
plt.savefig(
    "hanssybandera.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

print("¡Bandera creada correctamente!")
print("Archivo: hanssybandera.png")