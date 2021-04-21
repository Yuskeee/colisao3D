from math import sqrt

class Vector:
    def __init__(vector, *args):#inicia instancia de vetor
        if len(args) == 0: 
        	vector.coordinates = (0, 0, 0)
        else: 
        	vector.coordinates = args
        
    def norm_squared(vector):#calcula a norma^2 do vetor
        return sum(x * x for x in vector)

    def norm(vector):#calcula a norma do vetor
        return sqrt(vector.norm_squared())

    def normalize(vector):#normaliza o vetor
        norm = vector.norm()
        normed = tuple(x / norm for x in vector)
        return vector.__class__(*normed)
    
    def inner(vector, other):#produto interno com outro vetor
        if isinstance(other, Vector):
        	return sum(a * b for a, b in zip(vector, other))
    
    def __mul__(vector, other):#multiplicacao por escalar
        if isinstance(other, (int, float)):
            result = tuple(a * other for a in vector)
            return vector.__class__(*result)
    
    def __add__(vector, other):#soma de vetores
        if isinstance(other, Vector):
            result = tuple(a + b for a, b in zip(vector, other))
        return vector.__class__(*result)
    
    def __getitem__(vector, index):#possibilita uso de operador[] com o vetor
        return vector.coordinates[index]