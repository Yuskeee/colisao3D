from Vector import *

class Physics:
	physical_objects = []

	def __init__(physics, limits):
		physics.limit = limits

	def add_ball(physics, ball):
		physics.physical_objects.append(ball)

	def update(physics):
		physics._check_wall_collision()
		for i in range(len(physics.physical_objects)):
			for j in range(i+1, len(physics.physical_objects)):
				physics._check_ball_collision(physics.physical_objects[i], physics.physical_objects[j])

	def _check_ball_collision(physics, a, b):
		direcX = a.position[0] - b.position[0]
		direcY = a.position[1] - b.position[1]
		direcZ = a.position[2] - b.position[2]

		distance_squared = direcX ** 2 + direcY ** 2 + direcZ ** 2

		if distance_squared <= (a.radius ** 2) * 4:
			#verifica se houve contato
			#print("CONTATO ENTRE BOLAS!!!\n");

			collision_parallel_vector = Vector(direcX, direcY, direcZ)

			dVx = a.velocity[0] - b.velocity[0]
			dVy = a.velocity[1] - b.velocity[1]
			dVz = a.velocity[2] - b.velocity[2]

			#retorna velocidade se bolas não estiverem se aproximando para evitar que grudem e buguem
			if dVx * direcX + dVy * direcY + dVz * direcZ >= 0:
			    return

			#no eixo de colisao
			inner_product_velocity = float(a.velocity.inner(collision_parallel_vector))
			orthogonal_projection_velocity_a = collision_parallel_vector * float(inner_product_velocity / collision_parallel_vector.norm_squared())

			inner_product_velocity = float(b.velocity.inner(collision_parallel_vector))
			orthogonal_projection_velocity_b = collision_parallel_vector * float(inner_product_velocity / collision_parallel_vector.norm_squared())

			#perpendicular ao eixo de colisao (permanece inalterado)
			perpendicular_velocity_a = a.velocity + orthogonal_projection_velocity_a * -1
			perpendicular_velocity_b = b.velocity + orthogonal_projection_velocity_b * -1

			#atualiza velocidades
			a.velocity = perpendicular_velocity_a + orthogonal_projection_velocity_b
			b.velocity = perpendicular_velocity_b + orthogonal_projection_velocity_a
            
	def _check_wall_collision(physics):
		for i in physics.physical_objects:
			#eixo x
			if i.position[0] < -(physics.limit - i.radius) and i.velocity[0] < 0 or i.position[0] > (physics.limit - i.radius) and i.velocity[0] > 0:
				i.velocity = Vector(i.velocity[0] * -1, i.velocity[1], i.velocity[2])
			#eixo y
			elif i.position[1] < -(physics.limit - i.radius) and i.velocity[1] < 0 or i.position[1] > (physics.limit - i.radius) and i.velocity[1] > 0:
				i.velocity = Vector(i.velocity[0], i.velocity[1] * -1, i.velocity[2])
			#eixo z
			elif i.position[2] < -(physics.limit - i.radius) and i.velocity[2] < 0 or i.position[2] > (physics.limit - i.radius) and i.velocity[2] > 0:
				i.velocity = Vector(i.velocity[0], i.velocity[1], i.velocity[2] * -1)