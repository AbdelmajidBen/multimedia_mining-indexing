from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import comb
import numpy as np

# Define control points
control_points = np.array([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.5],
    [2.0, 0.0, 0.0],
    [0.0, 1.0, 0.5],
    [1.0, 1.0, 1.0],
    [2.0, 1.0, 0.5],
    [0.0, 2.0, 0.0],
    [1.0, 2.0, 0.5],
    [2.0, 2.0, 0.0]
])

selected_point = 0
camera_pos = np.array([3.0, 3.0, 5.0])
camera_angle = np.array([0.0, 0.0])  # yaw, pitch

# Bézier surface function
def bezier_surface(u, v, control_points):
    p = np.zeros(3)

    coeff = lambda n, i, t: comb(n, i) * (t**i) * ((1 - t)**(n - i))

    for i in range(3):
        for j in range(3):
            b = coeff(2, i, u) * coeff(2, j, v)
            p += b * control_points[i * 3 + j]
    return p

# Draw Bézier surface
def draw_bezier_surface():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera setup
    gluLookAt(
        camera_pos[0], camera_pos[1], camera_pos[2],
        1.0, 1.0, 0.0,
        0.0, 1.0, 0.0
    )

    # Draw control points
    glPointSize(10)
    glBegin(GL_POINTS)
    for i, point in enumerate(control_points):
        if i == selected_point:
            glColor3f(0.0, 1.0, 0.0)  # Selected point
        else:
            glColor3f(1.0, 0.0, 0.0)  # Regular points
        glVertex3fv(point)
    glEnd()

    # Draw Bézier surface
    glColor3f(0.2, 0.6, 1.0)
    glBegin(GL_QUADS)
    resolution = 20
    for u in np.linspace(0, 1, resolution):
        for v in np.linspace(0, 1, resolution):
            p1 = bezier_surface(u, v, control_points)
            p2 = bezier_surface(u + 1/resolution, v, control_points)
            p3 = bezier_surface(u + 1/resolution, v + 1/resolution, control_points)
            p4 = bezier_surface(u, v + 1/resolution, control_points)
            glVertex3fv(p1)
            glVertex3fv(p2)
            glVertex3fv(p3)
            glVertex3fv(p4)
    glEnd()

    # Draw grid
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_LINES)
    for i in range(-5, 6):
        glVertex3f(i, -5, 0)
        glVertex3f(i, 5, 0)
        glVertex3f(-5, i, 0)
        glVertex3f(5, i, 0)
    glEnd()

    glutSwapBuffers()

# Keyboard controls
def keyboard(key, x, y):
    global selected_point, control_points

    if key == b'\t':  # Switch selected point
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

# Mouse controls for camera rotation
def mouse_motion(x, y):
    global camera_angle
    camera_angle[0] = (x - 400) / 400 * 180  # yaw
    camera_angle[1] = (300 - y) / 300 * 90   # pitch

    # Recalculate camera position
    r = 5.0  # distance from the origin
    yaw, pitch = np.radians(camera_angle)
    camera_pos[0] = r * np.cos(pitch) * np.sin(yaw)
    camera_pos[1] = r * np.sin(pitch)
    camera_pos[2] = r * np.cos(pitch) * np.cos(yaw)

    glutPostRedisplay()

# Window resizing
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(w)/float(h), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Improved Bézier Surface")

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glutDisplayFunc(draw_bezier_surface)
    glutKeyboardFunc(keyboard)
    glutMotionFunc(mouse_motion)
    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == "__main__":
    main()
