#Hana Farahdiana 20051397073 2020MIA
# Algoritma Bresenham

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# bresenham line drawing algorithm
def bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0
    for x in range(dx+1):
        glVertex2i(x0 + x*xx + y*yx, y0 + x*xy + y*yy)
        if D > 0:
            y += 1
            D -= 2*dx
        D += 2*dy

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POINTS)
    bresenham(10,20,30,40)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bresenham's line algorithm")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-50, 50, -50, 50)
    glutDisplayFunc(display)
    glutMainLoop()

main()