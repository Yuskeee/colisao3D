#Colisao de Esferas em 3D

#Rodrigo Yuske Yamauchi

import glfw

def create_window(width, length, title):
    window = glfw.create_window(width, length, title, None, None)
    glfw.make_context_current(window)

    if(not window):
        print("ERROR: NAO FOI POSSIVEL INICIAR A JANELA!\n")
        exit()

    return window

def init(display):
    if(glfw.init()):
        window = create_window(display[0], display[1], "Colisao Bolas 3D")

        gluPerspective(70, (display[0]/display[1]), 0.0, 50.0)

        glTranslatef(0.0, 0.0, -30)
        glRotatef(30, 0, 1, 0)

        print("SUCESSO!\n")

        return window

    else:
        print("ERROR: NAO FOI POSSIVEL INICIAR GLFW!\n")
        glfw.terminate()
        exit()

def end(window):
	glfw.destroy_window(window);
	glfw.terminate()


from random import sample
from numpy import arange

from Cube import *
from Sphere import *
from Vector import *
from Physics import *

def create_spheres(physics, n_spheres, radius, max_vel, cube_length):#cria esferas com posições e velocidades aleatórias, sem que coincidam
    list_spheres = []

    for i in range(n_spheres):
        #gera as coordenadas e velocidades aleatórias
        pos = sample(list(arange(-(cube_length - radius), (cube_length - radius), 0.1)), 3)
        vel = sample(list(arange(-5, 5, 0.1)), 3)
        list_spheres.append(Sphere(radius, Vector(pos[0], pos[1], pos[2]), Vector(vel[0], vel[1], vel[2])))

    #evita bolas surgirem num mesmo lugar
    for i in range(n_spheres):
        for j in range(i + 1, n_spheres):
            direcX = list_spheres[i].position[0] - list_spheres[j].position[0]
            direcY = list_spheres[i].position[1] - list_spheres[j].position[1]
            direcZ = list_spheres[i].position[2] - list_spheres[j].position[2]

            distance_squared = direcX ** 2 + direcY ** 2 + direcZ ** 2

            if distance_squared <= (radius ** 2) * 4:
                #gera as coordenadas aleatórias novamente
                pos = sample(list(arange(-(cube_length - radius), (cube_length - radius), 0.1)), 3)
                list_spheres[i].position = Vector(pos[0], pos[1], pos[2])

                #reinicia a verificação
                i = 0
                j = 1

    for i in range(n_spheres):
        physics.add_ball(list_spheres[i])

    return list_spheres

#MAIN---------------------------------------------------------------------------------------------

from OpenGL.GL import *

def main():
    display = (800, 600) 
    window = init(display)

    cube_length = 10

    #inicia instancias de Física e esferas
    physics = Physics(cube_length)
    list_spheres = create_spheres(physics, 25, 1, 20, 10)

    timeA = glfw.get_time()

    print_timer = 0.0

    while not glfw.window_should_close(window):
        timeB = glfw.get_time()
        dt = timeB - timeA
        timeA = timeB

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        Cube(cube_length)

        physics.update()
        for sphere in list_spheres:
            sphere.update(dt)
        for sphere in list_spheres:
            sphere.rend()

        #imprime informações sobre conservação
        print_timer += dt
        if print_timer > 1.0:
            kinetic_energy = 0.0
            for sphere in list_spheres:
                kinetic_energy += float(sphere.velocity.norm() ** 2)#assumimos a massa como sendo uma unidade e nao dividimos por 2 para economizar processamento
            print("Total kinetic energy: {}\n".format(kinetic_energy), end = '\r')
            print_timer = 0.0

        glfw.swap_buffers(window)
        glfw.poll_events()
        glfw.swap_interval(1);

    end(window)
    quit()

if __name__ == '__main__':
	main()