import gym #cargamos la libreria gym

envi = gym.make("MountainCar-v0") #lanzamos una instancia de videojuego de la montaña rusa
envi.reset() #limpiar y reparar el entorno para toamr deciciones
for _ in range(2000): #se realizaran 2000 iteraciones (2000 veces el proceso)
    envi.render() #se renderizara las acciones en pantalla 
    envi.step(envi.action_space.sample()) #toma de decicion aleatoria del conjunto de las opciones disponibles