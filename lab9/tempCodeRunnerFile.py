from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

control_points = np.array([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [2.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [1.0, 1.0, 0.0],
    [2.0, 1.0, 0.0],
    [0.0, 2.0, 0.0],
    [1.0, 2.0, 0.0],
    [2.0, 2.0, 0.0],
    [0.0, 3.0, 0.0],
])

selected_point = 0
view_mode = 0
camera_pos = np.array([3.0, 3.0, 3.0])

def bezier_surface(u, v, control_points):
    p = np.zeros(3)
    for i in range(3):
        for j in range(3):
            p += (1 - u)**(2 - i) * u**i * (1 - v)**(2 - j) * v**j * control_points[i * 3 + j]
    return p

def draw_bezier_surface():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    if view_mode == 0:
        gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2], 1.0, 1.0, 0.0, 0.0, 1.0, 0.0)
    elif view_mode == 1:
        gluLookAt(5.0, 0.0, 3.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0)
    elif view_mode == 2:
        gluLookAt(1.0, 5.0, 3.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0)

    glPointSize(10)
    glBegin(GL_POINTS)
    for i, point in enumerate(control_points):
        if i == selected_point:
            glColor3f(0.0, 0.0, 1.0)
        else:
            glColor3f(1.0, 0.0, 0.0)
        glVertex3fv(point)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINE_STRIP)
    for u in np.linspace(0, 1, 20):
        for v in np.linspace(0, 1, 20):
            p = bezier_surface(u, v, control_points)
            glVertex3fv(p)
    glEnd()

    glutSwapBuffers()

def keyboard(key, x, y):
    global view_mode, selected_point

    if key == b'a':
        view_mode = 0
    elif key == b'b':
        view_mode = 1
    elif key == b'c':
        view_mode = 2
    elif key == b'\t':
        selected_point = (selected_point + 1) % len(control_points)
    elif key == b'x':
        control_points[selected_point][0] += 0.1
    elif key == b'y':
        control_points[selected_point][1] += 0.1
    elif key == b'z':
        control_points[selected_point][2] += 0.1
    elif key == b'X':
        control_points[selected_point][0] -= 0.1
    elif key == b'Y':
        control_points[selected_point][1] -= 0.1
    elif key == b'Z':
        control_points[selected_point][2] -= 0.1

    glutPostRedisplay()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(w)/float(h), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Surface de Bézier 3D avec points de contrôle")

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glutDisplayFunc(draw_bezier_surface)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == "__main__":
    main()
