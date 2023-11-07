from cola import Cola
import linecache

def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split

class NodeTree():

    def __init__(self, value, other_values = None, second_value = None):
        self.value = value
        self.other_values = other_values
        self.second_value = second_value    
        self.left = None
        self.right = None
        self.height = 0


class BinaryTree:

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_values=None, second_value = None):

        def __insertar(root, value, other_values, second_value):
            if root is None:
                return NodeTree(value, other_values, second_value)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values, second_value)
            else:
                root.right = __insertar(root.right, value, other_values, second_value)
            # print('izquierda', self.height(root.left) - self.height(root.right))
            # print('derecha', self.height(root.right) - self.height(root.left))
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values, second_value)

    def inorden(self):
        #muestra en orden ascendente el arbol luego de ordenarlas
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def inorden_tipos(self):
            #muestra en orden ascendente el arbol luego de ordenarlas
            def __inorden(root):
                if root is not None:
                    if (root.value.__contains__("Agua") or root.value.__contains__("Fuego") or root.value.__contains__("Eléctrico") or root.value.__contains__("Planta")):
                        __inorden(root.left)
                        print(f"{root.other_values} es tipo {root.value}")
                        __inorden(root.right)

            __inorden(self.root)
    
    def contar_elec_acero(self):
        def __contar(root):
            count = 0
            if root is not None:
                if root.value == "Eléctrico/Acero":
                    count = 1
                count += __contar(root.left)
                count += __contar(root.right)
            return count
        
        return __contar(self.root)


    def postorden(self):
        #te los muestran en orden descendente luego de ordenarlas
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self):
        #te lo muestra segun ramas (el primero de todo, después su primero a la izq o derecha (segun lo que tenga) - y de esos sus izquierdos y derechos, y lo mismo con los nodos del otro lado) antes de ordernarlas
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)

    
    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value

            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value
    
    ##creadas por "Mi":

    def hijoMinimo(self):
        if self is not None:
            nodo = self.root
            while nodo.left:
                nodo = nodo.left
            return nodo.value
        else:
            raise Exception("No se enecontraron valores")   
        
    def hijoMayor(self):
        if self is not None:
            nodo = self.root
            while nodo.right:
                nodo = nodo.right
            return nodo.value
        else:
            raise Exception("No se encontraron valores.")

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count
        
        return __contar(self.root, value)

    def contar_heroes(self, is_hero):
        def __contar_heroes(root, is_hero):
            count = 0
            if root is not None:
                if root.other_values is is_hero:
                    count = 1
                count += __contar_heroes(root.left, is_hero)
                count += __contar_heroes(root.right, is_hero)

            return count
            
        return __contar_heroes(self.root, is_hero)
        
    def contar_pares_impares(self):

        def __contar_p_i(root):
            count = 0
            if root is not None:
                if (root.value % 2 == 0):
                    count = 1
                count += __contar_p_i(root.left)
                count += __contar_p_i(root.right)
            
            return count
        
        return __contar_p_i(self.root)

    def inorden_heroe_o_villano(self, is_hero):

        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)
            
        __inorden_s_v(self.root, is_hero)

    def starts_with(self, string):

        def __inorden_starts_with(root, string):
            if root is not None:
                __inorden_starts_with(root.left, string)
                if root.other_values is True and root.value.upper().startswith(string):
                    print(root.value)
                __inorden_starts_with(root.right, string)
        
        __inorden_starts_with(self.root, string)

    def search_by_coincidence(self, string):

        def __search_coincidence(root, cadena):
            if root is not None:
                if root.value.startswith(cadena):
                    print(root.value, root.other_values, root.second_value)
                __search_coincidence(root.left, cadena)
                __search_coincidence(root.right, cadena)

        __search_coincidence(self.root, string)

    def search_by_coincidence_and_contains(self, string):

        def __search_coincidence(root, cadena):
            if root is not None:
                if root.value.startswith(cadena) or root.value.__contains__(cadena):
                    print(root.value, root.other_values, root.second_value)
                __search_coincidence(root.left, cadena)
                __search_coincidence(root.right, cadena)

        __search_coincidence(self.root, string)

    def get_heroe_villano(self, arbol_a, arbol_b):

        def __search_s_v(root, arbol_a, arbol_b):
            if root is not None:
                __search_s_v(root.left, arbol_a, arbol_b)
                if root.other_values is True:
                    arbol_a.insert_node(root.value, root.other_values)#, root.other_values
                else:
                    arbol_b.insert_node(root.value, root.other_values)
                __search_s_v(root.right, arbol_a, arbol_b)


        return __search_s_v(self.root, arbol_a, arbol_b)

    def order_by_level(self):
        if self.root is not None:
            cola = Cola()
            cola.arrive(self.root)
            while cola.size() > 0:
                node = cola.atenttion()
                print(node.value)
                if node.left is not None:
                    cola.arrive(node.left)
                if node.right is not None:
                    cola.arrive(node.right)

    def inorden_file_by_rank(self, file_name):  #es lo mismo que inorden, pero esta muestra otros valores.
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)
                
        __inorden_file(self.root, file_name)
    
        # def inorden_tipos(self, arbol):
        #     def __inorden_file(root, arbol):
        #         if root is not None:
        #             __inorden_file(root.left, arbol)
        #             valor = 
        #             if value[1] == hero:
        #                 print(f'{root.value} fue derrotado/a por {hero}')
        #             __inorden_file(root.right, file_name, hero)
            
        #     __inorden_file(self.root, file_name, hero)

# arbol = BinaryTree()

# for i in range(15):
#     arbol.insert_node(name, {'derrotado_por': derrotado})


# pos.other_values['capurado_por'] = 'asdas'
# arbol.preorden()

# arbol.root = arbol.balancing(arbol.root)



# print(arbol.root)
# arbol.insert_node('F')
# arbol.insert_node('B')
# # arbol.insert_node('E')
# arbol.insert_node('K')
# arbol.insert_node('H')
# arbol.insert_node('J')
# arbol.insert_node('I')
# arbol.insert_node('R')

# arbol.preorden()

# print()
# deleted = arbol.delete_node('F')
# # if deleted:
# #     print('el valor fue eliminado', deleted)
# # print()
# arbol.preorden()
# deleted = arbol.delete_node('Z')
# print()
# arbol.preorden()
# deleted = arbol.delete_node('K')
# print()
# arbol.preorden()


# print()
# pos = arbol.search('Z')
# print(pos)
# if pos:
#     print('valor encontrado', pos.value)
