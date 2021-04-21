from OpenGL.GL import *
from OpenGL.GLU import *

from Vector import *

class Sphere:
	position = Vector(0.0, 0.0, 0.0)
	velocity = Vector(0.0, 0.0, 0.0)

	def __init__(sphere, radius, position, velocity):
		sphere._id = gluNewQuadric()
		sphere.radius = radius
		sphere.position = position
		sphere.velocity = velocity

	def update(sphere, dt):
		sphere.position += (sphere.velocity * dt)

	def rend(sphere):
		glPushMatrix()

		glTranslatef(sphere.position[0], sphere.position[1], sphere.position[2]);
		gluSphere(sphere._id, sphere.radius, 30, 30)

		glPopMatrix()