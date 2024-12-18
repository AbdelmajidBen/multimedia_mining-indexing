from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

W, H = 800, 600  # Initialize global width and height

def main():
    global W, H
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(W, H)
    glutCreateWindow('Labs Note 8')
    # Background color
    glClearColor(0., 0., 0., 1)
    glutDisplayFunc(aff)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(redim)
    glutMainLoop()

def redim(w, h):
    global W, H
    W = w
    H = h

def keyboard(key, x, y):
    intKey = ord(key)  # Convert the key to its ASCII value
    if intKey == 27:  # ESC key
        exit(1)

def axes():
    glLineStipple(1, 0x0CFF)
    glEnable(GL_LINE_STIPPLE)
    glLineWidth(1)
    # Draw axes
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  # Red axis
    glVertex3f(-10.0, 0.0, 0.0)
    glVertex3f(10.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Green axis
    glVertex3f(0.0, -10.0, 0.0)
    glVertex3f(0.0, 10.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)  # Blue axis
    glVertex3f(0.0, 0.0, -10.0)
    glVertex3f(0.0, 0.0, 10.0)
    glEnd()
    glDisable(GL_LINE_STIPPLE)

def dessiner():
    # Draw axes
    axes()
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)  # Red teapot
    glTranslatef(-1, 0., 0.)
    glutSolidTeapot(0.3)
    glPopMatrix()
    glColor3f(0.0, 1.0, 0.0)  # Green teapot
    glTranslatef(1, 0., 0.)
    glutSolidTeapot(0.3)

def aff():
    global W, H
    # Clear the buffer
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0, 0, int(W), int(H/2))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(1., 1., 1., 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    dessiner()

    glViewport(0, int(H/2), int(W/3), int(H/2))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(1., 0., 0., 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    dessiner()

    glViewport(int(W/3), int(H/2), int(W/3), int(H/2))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0., 1., 0., 0.0, 0.0, 0.0, 1.0, 0.0, 1.0)
    dessiner()

    glViewport(int(2*W/3), int(H/2), int(W/4), int(H/2))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0., 0., 1., 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    dessiner()

    glutSwapBuffers()

if __name__ == '__main__':
    main()
