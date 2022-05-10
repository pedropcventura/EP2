import math
def haversine(raio, a1, y1, a2, y2): 

    parte1 = (math.sin(math.radians((a2-a1)/2)))**2
    parte2 = math.cos(math.radians(a1)) * math.cos(math.radians(a2))*(math.sin(math.radians((y2-y1)/2)))**2
    return 2*raio*math.asin((parte1+parte2)**0.5)
    