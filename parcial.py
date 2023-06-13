from cola import Cola
from lista import Lista
from pila import Pila

from mision import Mision
from superheroe import Superheroe

#1. Desarrollar una función recursiva que permita contar cuantas veces aparece una determinada palabra, en un vector de palabras. 

print("EJERCICIO 1")
vector = ["hola", "bailar", "saltar", "reirse", "star", "trek", "bailar", "rendir", "bailar", "francia"]

def contar(palabra, vector):
    if vector == []:
        return 0
    elif vector[0] == palabra:
        return 1 + contar(palabra, vector[1:])
    else:
        return 0 + contar(palabra, vector[1:])

print(contar("bailar", vector))

#2. Dada una lista con nombres de personajes de la saga de Avengers ordenados por nombre del superhéroes, de los cuales se conoce: nombre del superhéroe, nombre del personaje (puede ser vacio), 
# grupo al que (perteneces puede ser vacio), año de aparición, por ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976). Resolver las siguientes tareas: 
# a. Determinar si “Capitana Marvel” está en la lista y mostrar su nombre de personaje; 
# b. Almacenar los superhéroes que pertenezcan al grupo “Guardianes de la galaxia” en una cola e indicar cuantos son.  
# c. Mostrar de manera descendente los superhéroes que pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de la galaxia”. 
# d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960. 
# e. Hemos detectado que la superhéroe “Black Widow” está mal cargada por un error de tipeo, figura como “Vlanck Widow”, modifique dicho superhéroe para solucionar este problema.  
# f. Dada una lista auxiliar con los siguientes personajes (‘Black Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la información), agregarlos a la lista principal en el caso de no estar cargados.  
# g. Mostrar todos los personajes que comienzan con C, P o S. 
# h. Cargue al menos 20 superheroes a la lista. 

print("\nEJERCICIO 2:")
auxilar = Lista()
cola = Cola()
superheroes = Lista()

auxilar = [ Superheroe("Rocket Raccoon", "Rocket", 1976, "Guardianes de la Galaxia"),
            Superheroe("Hulk", "Bruce Banner", 1962, "Avengers"),
            Superheroe("Loki", "Loki", 1962, "Asgard"),
            Superheroe("Black Cat", "Felicia Hardy", 1979, "Defenders")
           ]

lista = [
    Superheroe("Star-Lord", "Peter Quill", 1980, "Guardianes de la Galaxia"),
    Superheroe("Capitana Marvel", "Carol Danvers", 1968, "Avengers"),
    Superheroe("Drax", "Drax", 1974, "Guardianes de la Galaxia"),
    Superheroe("Doctor Strange", "Stehpen Strange", 1963, "Avengers"),
    Superheroe("Thing", "Benjamin Grimm", 1961, "Fantastic Four"),
    Superheroe("Vlanck Widow", "Natasha Romanoff", 1964, "Avengers"),
    Superheroe("Mister Fantastic", "Reed Richards", 1961, "Fantastic Four"),
    Superheroe("Iron Man", "Tony Stark", 1963, "Avengers"),
    Superheroe("Captain America", "Steve Rogers", 1941, "Avengers"),
    Superheroe("Scarlet Witch", "Wanda Maximoff", 1964, "Avengers"),
    Superheroe("Ant-Man", "Scott Lang", 1979, "Avengers"),
    Superheroe("Spider-Man", "Peter Parker", 1962, "Avengers"),
    Superheroe("Squirrel Girl", "Doreen Green", 1992, "Avengers"),
    Superheroe("Nightcrawler", "Kurt Wagner", 1975, "X-Men"),
    Superheroe("Quicksilver", "Pietro Maximoff", 1964, "X-Men"),
    Superheroe("Dark Phoenix", "Jean Grey", 1963, "X-Men")
]

for super in lista:
    superheroes.insert(super, "nombre_s")

for aux in auxilar:
    superheroes.insert(aux, "nombre_s")

for i in range(superheroes.size()):
    print(superheroes.get_element_by_index(i))

print("\nA:")
elemento = superheroes.search("Capitana Marvel", "nombre_s")
if elemento:
    print("Capitana Marvel esta en la lista, su nombre real es", superheroes.get_element_by_index(elemento).nombre_p)
else:
    print("No esta.")

print("\nB:")
for i in range(superheroes.size()):
    if superheroes.get_element_by_index(i).grupo == "Guardianes de la Galaxia":
        cola.arrive(i)

print(cola.size())

print("\nC:")
for x in range(superheroes.size()):
    buscado = superheroes.get_element_by_index(x)
    if buscado.grupo == "Guardianes de la Galaxia" or buscado.grupo == "Fantastic Four":
        print(buscado.nombre_s)

print("\nD:")
for z in range(superheroes.size()):
    buscado = superheroes.get_element_by_index(z)
    if buscado.anio > 1960:
        print(buscado.nombre_s)

print("\nE:")
for a in range(superheroes.size()):
    buscado = superheroes.get_element_by_index(a)
    if buscado.nombre_p == "Natasha Romanoff":
        buscado.nombre_s = "Black Widow"
        print(f"Se le arreglo el nombre a Natasha Romanoff. Ahora es correctamente {buscado.nombre_s}")

print("\nG:")
for o in range(superheroes.size()):
    buscado = superheroes.get_element_by_index(o)
    if buscado.nombre_p.startswith('C') or buscado.nombre_p.startswith('P') or buscado.nombre_p.startswith('S'):
        print(buscado.nombre_p)
#3
#Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la  cual se almacenaban en una pila en cada misión de caza que  emprendió 
#(con la siguiente información planeta visitado, a quien  capturado, costo de la recompensa), 
# resolver las siguientes  actividades: 

# a. Mostrar los planetas visitados en el orden hizo las misiones. 
# b. Determinar cuántos créditos galácticos recaudo en total. 
# c. Determinar el número de la misión en que capturo a Han Solo y en que planeta fue, suponga que dicha misión está cargada

print("\nEJERCICIO 3: \n")

pila = Pila()
pila_c = Pila()
pila_extra = Pila()

bitacora = [
    Mision("Bespin", "Han Solo", 10000000),
    Mision("Tatooine", "una hormiga", 20),
    Mision("Redactado", "Redactado", 3),
    Mision("Dagobah", "Grogu", 70000)
]

for bita in bitacora:
    pila_extra.push(bita)

while pila_extra.size() > 0:
    aux = pila_extra.pop()
    pila.push(aux)
    pila_c.push(aux)

con = 0
creditos = 0

print("\nA:")
while pila.size() > 0:
    dato = pila.pop()
    print(f"Planeta {con + 1}:", dato.planeta)
    con += 1
    creditos += dato.recompensa

print("\nB:")
print(creditos)

print("\nC:")
conH = 0

while pila_c.size() > 0:
    dato = pila_c.pop()
    conH += 1
    if dato.captura == "Han Solo":
        print(f"Han Solo fue capturado en la mision {conH}, en el planeta {dato.planeta}.")