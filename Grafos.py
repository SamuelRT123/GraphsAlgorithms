"""
    -Los vertices se hacen con Strings para adaptarse a cualquier escenario.
    -Los grafos se representan como mapas, donde la llave es el vertice y el valor es una lista con los vertices de destino.
    -Para los grafo ponderados se crea la función de costos, creada como un mapa con la llave como arco1 + arco2 = costo del arco.
    -La creación de la lista de vertices, arcos y pesos dependerá del contexto del problema, si es por un archivo .txt, .css, .json, etc. 
    -Si es por archivo de texto, durante la lectura del archivo es preferible crear el grafo de una vez en lugar de crear las listas a menos que sean necesarias.  
"""


def agregarVerticesYArcos(vertices,arcos):
    grafo={}
    #Se agregan los vertices al grafo
    for vertice in vertices:
        grafo[vertice] = []
    
    #Se agregan los arcos al grafo
    for arco in arcos:
        origen, destino = arco
        grafo[origen].append(destino)
    
    return grafo
   
def agregarVerticesYArcosNoDirigido(vertices,arcos):
    grafo={}
    #Se agregan los vertices al grafo
    for vertice in vertices:
        grafo[vertice] = []
    
    #Se agregan los arcos al grafo
    for arco in arcos:
        origen, destino = arco
        grafo[origen].append(destino)
        grafo[destino].append(origen)
    
    return grafo     
def Grafo1():
    
    #Grafo de ejemplo 1. Dirigino no ponderado
    vertices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]
    arcos = [("0", "7"), ("0", "14"),
         ("2", "1"), ("2", "6"),
         ("3", "2"),
         ("4", "1"), ("4", "8"),
         ("5", "6"), ("5", "8"),
         ("6","2"), ("6", "3"), ("6", "10"),
         ("7", "4"), ("7", "8"),
         ("8", "7"), ("8", "5"),
         ("9", "12"), ("9", "13"),
         ("10", "3"),("10","13"),
         ("11", "15"),
         ("12", "8"), ("12", "16"),("12", "11"),
         ("13", "9"),("13","16"),
         ("14", "11"),
         ("15", "17"),
         ("16", "15"), ("16", "12"),
         ("17", "10")]

    grafo= agregarVerticesYArcos(vertices,arcos)
    
    return grafo

def Grafo2():
    
    vertices = ["0", "1", "2", "3", "4", "5", "6", "7"]
    arcos =[
        ("0","1"),("0","3"),
        ("1","0"),("1","3"),("1","2"),("1","5"),
        ("2","1"),("2","4"),("2","6"),
        ("3","0"),("3","1"),("3","7"),
        ("4","2"),("4","7"),
        ("5","1"),("5","6"),("5","7"),
        ("6","5"),("6","2"),
        ("7","3"),("7","4"),("7","5"),
        
    ]
    
    grafo= agregarVerticesYArcosNoDirigido(vertices,arcos)
    
    return grafo

def Grafo3():
    grafo={}
    vertices=[]
    arcos=[]
    pesos=[]
    pass

def Grafo4():
    grafo={}
    vertices=[]
    arcos=[]
    pesos=[]
    pass

def Grafo5():
    grafo={}
    vertices=[]
    arcos=[]
    pesos=[]
    pass

def Grafo6():
    grafo={}
    vertices=[]
    arcos=[]
    pesos=[]
    pass

def Grafo7():
    grafo={}
    vertices=[]
    arcos=[]
    pesos=[]
    pass
