# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.
print("EJERCICIO 1:")
from arbol_binario import BinaryTree

arbol_nom = BinaryTree()
arbol_num = BinaryTree()
arbol_tipo = BinaryTree()

NOMBRE = arbol_nom
NUMERO = arbol_num
TIPO = arbol_tipo
    
print("\nA:")
pokes = [
    {"nombre":"Bulbasaur", "numero":1, "tipo":"Planta/Veneno"},
    {"nombre":"Ivysaur", "numero":2, "tipo":"Planta/Veneno"},
    {"nombre":"Charmander", "numero":4, "tipo":"Fuego"},
    {"nombre":"Squirtle", "numero":7, "tipo":"Agua"},
    {"nombre":"Pikachu", "numero":25, "tipo":"Eléctrico"},
    {"nombre":"Magnemite", "numero":81, "tipo":"Eléctrico/Acero"},
    {"nombre":"Jolteon", "numero":135, "tipo":"Eléctrico"},
    {"nombre":"Tyrantrum", "numero":697, "tipo":"Roca/Dragón"},
    {"nombre":"Lycanroc", "numero":745, "tipo":"Roca"},
    {"nombre":"Togedamaru", "numero":777, "tipo":"Eléctrico/Acero"}
]
for p in pokes:
    NOMBRE.insert_node(p["nombre"], p["numero"], p["tipo"])
    NUMERO.insert_node(p["numero"], p["nombre"], p["tipo"])
    TIPO.insert_node(p["tipo"], p["nombre"], p["tipo"])

print("\nB:")
numerito = 1
dato_numero = NUMERO.search(numerito)
if dato_numero:
    print(dato_numero.value, dato_numero.other_values, dato_numero.second_value)

buscar_nombre = NOMBRE.search_by_coincidence_and_contains("saur")
if buscar_nombre:
    print(buscar_nombre.value, buscar_nombre.other_values, buscar_nombre.second_value)

print("\nC:")
TIPO.inorden_tipos()

print("\nD:")
NOMBRE.inorden()
print()
NUMERO.inorden() 
print()
NOMBRE.order_by_level()

print("\nE:")
jolteon = NOMBRE.search("Jolteon")
if jolteon:
    print(jolteon.value, jolteon.other_values, jolteon.second_value)

lycanroc = NOMBRE.search("Lycanroc")
if lycanroc:
    print(lycanroc.value, lycanroc.other_values, lycanroc.second_value)

tyrantrum = NOMBRE.search("Tyrantrum")
if tyrantrum:
    print(tyrantrum.value, tyrantrum.other_values, tyrantrum.second_value)

print("\nF:")
print(f"Hay {TIPO.contar_elec_acero()} pokes de tipo Eléctrico/Acero")

print("\nEJERCICIO 2:")

# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas: 
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representanlacantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan; 
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda; 
# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 
# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
from grafo import Grafo
from random import randint

grafo = Grafo(dirigido=False)

personajes = [
    {"nombre":"Boba Fett", "numero":randint(1, 9)},
    {"nombre":"Din Djarin", "numero":randint(1, 9)},
    {"nombre":"Luke Skywalker", "numero":randint(1, 9)},
    {"nombre":"Darth Vader", "numero":randint(1, 9)},
    {"nombre":"Yoda", "numero":randint(1, 9)},
    {"nombre":"C 3PO", "numero":randint(1, 9)},
    {"nombre":"Leia Skywalker", "numero":randint(1, 9)},
    {"nombre":"Kylo Ren", "numero":randint(1, 9)},
    {"nombre":"Chewbacca", "numero":randint(1, 9)},
    {"nombre":"Han Solo", "numero":randint(1, 9)},
    {"nombre":"R2 D2", "numero":randint(1, 9)},
    {"nombre":"BB 8", "numero":randint(1, 9)}
]

for pers in personajes:
    grafo.insert_vertice(pers["nombre"], pers["numero"])

for i in personajes:
    for j in personajes:
        if i["nombre"] != j["nombre"] and (i["numero"] == j["numero"]) and not grafo.is_adyacent(i["nombre"], j["nombre"]):
            grafo.insert_arist(i["nombre"], j["nombre"], i["numero"])


print("\nB:")
max = 0
max_nodo = list
print(grafo.kruskal())
for vertice in grafo.kruskal():
    for nodo in vertice.split(";"):
        value = nodo.split("-")
        if value.__contains__("Yoda"):
            print("Contiene a Yoda.")
        if int(value[2] > max):
            max_nodo = value

print(f"La arista de valor máximo es {max_nodo[0]} y {max_nodo[1]} comparten {max_nodo[2]} episodios")