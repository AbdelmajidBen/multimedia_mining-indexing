from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

# Définir les points de contrôle (exemple d'une grille 3x3)
control_points = np.array([
    [0.0, 0.0, 0.0],  # Point de contrôle 0
    [1.0, 0.0, 0.0],  # Point de contrôle 1
    [2.0, 0.0, 0.0],  # Point de contrôle 2
    [0.0, 1.0, 0.0],  # Point de contrôle 3
    [1.0, 1.0, 0.0],  # Point de contrôle 4
    [2.0, 1.0, 0.0],  # Point de contrôle 5
    [0.0, 2.0, 0.0],  # Point de contrôle 6
    [1.0, 2.0, 0.0],  # Point de contrôle 7
    [2.0, 2.0, 0.0],  # Point de contrôle 8
    [0.0, 3.0, 0.0],  # Point de contrôle 9
    [1.0, 3.0, 0.0],  # Point de contrôle 10
])

# Variables pour gérer les positions de la caméra et les angles
camera_pos = np.array([3.0, 3.0, 3.0])  # Position initiale de la caméra
view_mode = 0  # Mode de vue actuel : 0 = vue standard, 1 = vue de côté, 2 = vue du dessus

# Fonction pour calculer la surface de Bézier
def bezier_surface(u, v, control_points):
    p = np.zeros(3)  # Point final de la surface
    for i in range(3):
        for j in range(3):
            p += (1 - u)**(2 - i) * u**i * (1 - v)**(2 - j) * v**j * control_points[i * 3 + j]
    return p

# Fonction pour dessiner la surface de Bézier
def draw_bezier_surface():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Changer la vue selon le mode de visualisation
    if view_mode == 0:  # Vue standard
        gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2], 1.0, 1.0, 0.0, 0.0, 1.0, 0.0)
    elif view_mode == 1:  # Vue de côté
        gluLookAt(5.0, 0.0, 3.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0)
    elif view_mode == 2:  # Vue du dessus
        gluLookAt(1.0, 5.0, 3.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0)

    # Dessiner les points de contrôle
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)  # Couleur rouge pour les points de contrôle
    for point in control_points:
        glVertex3fv(point)
    glEnd()

    # Dessiner la surface de Bézier
    glColor3f(0.0, 1.0, 0.0)  # Couleur verte pour la surface
    glBegin(GL_LINE_STRIP)
    for u in np.linspace(0, 1, 100):
        for v in np.linspace(0, 1, 100):
            p = bezier_surface(u, v, control_points)
            glVertex3fv(p)
    glEnd()

    # Afficher les résultats
    glutSwapBuffers()

# Fonction pour gérer les entrées clavier
def keyboard(key, x, y):
    global view_mode

    if key == b'a':  # Vue standard (Perspective)
        view_mode = 0
    elif key == b'b':  # Vue de côté (caméra à droite)
        view_mode = 1
    elif key == b'c':  # Vue du dessus (caméra au-dessus)
        view_mode = 2

    # Redessiner la scène après modification
    glutPostRedisplay()

# Fonction pour gérer la mise à jour de la fenêtre
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(w)/float(h), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# Fonction principale
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Surface de Bézier 3D avec points de contrôle")

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fond noir

    # Définir les fonctions de gestion des événements
    glutDisplayFunc(draw_bezier_surface)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)

    # Lancer la boucle GLUT
    glutMainLoop()

if __name__ == "__main__":
    main()
