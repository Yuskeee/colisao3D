from OpenGL.GL import *

class Cube:
	def __init__(cube, length):
		cube.size_length = length

		vertices= (
		    (length, -length, -length),
		    (length, length, -length),
		    (-length, length, -length),
		    (-length, -length, -length),
		    (length, -length, length),
		    (length, length, length),
		    (-length, -length, length),
		    (-length, length, length)
		    )

		edges = (
		    (0,1),
		    (0,3),
		    (0,4),
		    (2,1),
		    (2,3),
		    (2,7),
		    (6,3),
		    (6,4),
		    (6,7),
		    (5,1),
		    (5,4),
		    (5,7)
		    )

		glBegin(GL_LINES)

		for edge in edges:
			for vertex in edge:
				glVertex3fv(vertices[vertex])

		glEnd()