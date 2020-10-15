import math 
def distancia_euclidiana(x_1, y_1, x_2, y_2):
    x = x_2 - x_1
    x1=math.pow(x,2)
    y = y_2 - y_1
    y1=math.pow(y,2)
    resultado = x1+y1
    return(math.sqrt(resultado))