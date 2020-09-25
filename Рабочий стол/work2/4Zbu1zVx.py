from collections import defaultdict
import math

import numpy as np

from decimal import *

getcontext().prec = 30

class Edge:
    def __init__(self, fr, to, length, diameter):
        self.fr = fr
        self.to = to
        self.length = Decimal(length)
        self.diameter = Decimal(diameter)

p = defaultdict(lambda: None)
corner_p = set()
L1 = defaultdict(lambda: Decimal(0.0))
edges = []
get_edge = defaultdict(lambda: None)
nu1 = Decimal(1.3)
nu2 = Decimal(30)
DT = None

n_ = {}
po_ = {}
n = defaultdict(lambda: Decimal(0.0))
po = defaultdict(lambda: Decimal(0.0))

A = Decimal(0.1)
B = Decimal(0.001)

d = {}
l = {}
q = {}
s = {}
v = {}
w = {
    2: 3,
    3: 5,
    4: 5,
    5: 4,
    6: 2,
    8: 3,
    9: 5,
    10: 5,
    11: 6,
    12: 4,
    13: 5,
    14: 3,
    15: 6,
    16: 5,
    17: 4
}


def load_graph():
    p[1] = Decimal(70)
    p[7] = Decimal(60)
    p[11] = Decimal(50)
    p[5] = Decimal(40)
    p[6] = Decimal(30)
    p[10] = Decimal(20)
    p[16] = Decimal(20)
    p[17] = Decimal(40)

    for v in p.keys():
        corner_p.add(v)

    edges.append(Edge(1, 2, Decimal(20), Decimal(2)))
    edges.append(Edge(2, 3, Decimal(40), Decimal(4)))
    edges.append(Edge(3, 4, Decimal(40), Decimal(2)))
    edges.append(Edge(4, 5, Decimal(40), Decimal(4)))
    edges.append(Edge(4, 6, Decimal(40), Decimal(2)))
    edges.append(Edge(7, 2, Decimal(30), Decimal(3)))
    edges.append(Edge(7, 8, Decimal(20), Decimal(2)))
    edges.append(Edge(8, 4, Decimal(50), Decimal(5)))
    edges.append(Edge(8, 9, Decimal(40), Decimal(2)))
    edges.append(Edge(9, 10, Decimal(40), Decimal(2)))
    edges.append(Edge(9, 13, Decimal(20), Decimal(2)))
    edges.append(Edge(9, 14, Decimal(40), Decimal(4)))
    edges.append(Edge(11, 12, Decimal(25), Decimal(2)))
    edges.append(Edge(12, 13, Decimal(40), Decimal(4)))
    edges.append(Edge(13, 14, Decimal(40), Decimal(2)))
    edges.append(Edge(14, 15, Decimal(40), Decimal(2)))
    edges.append(Edge(15, 16, Decimal(40), Decimal(4)))
    edges.append(Edge(15, 17, Decimal(40), Decimal(2)))

    
    n[1] = n[7] = n[11] = Decimal(10**3)
    po[1] = po[7] = po[11] = Decimal(10**2 + 0.0)
    

    for edge in edges:
        get_edge[(edge.fr, edge.to)] = edge
        get_edge[(edge.to, edge.fr)] = edge


def calc_n():
    global n_
    n_ = {}
    n_[2] = n[2] + Decimal(0.0012) / w[2] * (A * po[2] * n[2] * w[2] + n[1] * s[(1, 2)] * v[(1, 2)] - Decimal(2 * math.pi) * n[1] * Decimal(21.97 * 10**(-3)) * l[(1, 2)] + n[7] * s[(7, 2)] * v[(7, 2)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[7] * l[(7, 2)] - n[2] * s[(2, 3)] * v[(2, 3)]) 
    n_[3] = n[3] + Decimal(0.0012) / w[3] * (A * po[3] * n[3] * w[3] + n[2] * s[(2, 3)] * v[(2, 3)] - Decimal(2 * math.pi) * n[2] * Decimal(21.97 * 10**(-3)) * l[(2, 3)] - n[3] * v[(3, 4)] * s[(3, 4)]) 
    n_[4] = n[4] + Decimal(0.0012) / w[4] * (A * po[4] * n[4] * w[4] + n[3] * s[(3, 4)] * v[(3, 4)] - Decimal(2 * math.pi) * n[3] * Decimal(21.97 * 10**(-3)) * l[(3, 4)] + n[8] * s[(8, 4)] * v[(8, 4)] - Decimal(2 * math.pi) * n[8] * Decimal(21.97 * 10**(-3)) * l[(8, 4)] - n[4] * s[(4, 5)] * v[(4, 5)] - n[4] * s[(4, 6)] * v[(4, 6)]) 
    n_[5] = n[5] + Decimal(0.0012) / w[5] * (A * po[5] * n[5] * w[5] + n[4] * s[(4, 5)] * v[(4, 5)] - Decimal(2 * math.pi) * n[4] * Decimal(21.97 * 10**(-3)) * l[(4, 5)]) 
    #### in the line below was (5, 6) instead of (4, 6), but such edge doesn't exist
    n_[6] = n[6] + Decimal(0.0012) / w[6] * (A * po[6] * n[6] * w[6] + n[4] * s[(4, 6)] * v[(4, 6)] - Decimal(2 * math.pi) * n[4] * Decimal(21.97 * 10**(-3)) * l[(4, 6)])
    n_[8] = n[8] + Decimal(0.0012) / w[8] * (A * po[8] * n[8] * w[8] + n[7] * s[(7, 8)] * v[(7, 8)] - Decimal(2 * math.pi) * n[7] * Decimal(21.97 * 10**(-3)) * l[(7, 8)] - n[8] * s[(8, 9)] * v[(8, 9)] - n[8] * s[(8, 4)] * v[(8, 4)]) 
    n_[9] = n[9] + Decimal(0.0012) / w[9] * (A * po[9] * n[9] * w[9] + n[8] * s[(8, 9)] * v[(8, 9)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-2)) * n[8] * l[(8, 9)] - n[9] * s[(9, 10)] * v[(9, 10)] - n[9] * s[(9, 13)] * v[(9, 13)] - n[9] * s[(9, 14)] * v[(9, 14)]) 
    n_[10] = n[10] + Decimal(0.0012) / w[10] * (A * po[10] * n[10] * w[10] + n[9] * s[(9, 10)] * v[(9, 10)] - Decimal(2 * math.pi) * n[9] * Decimal(21.97 * 10**(-3)) * l[(9, 10)]) 
    n_[12] = n[12] + Decimal(0.0012) / w[12] * (A * po[12] * n[12] * w[12] + n[11] * s[(11, 12)] * v[(11, 12)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-3)) * n[11] * l[(11, 12)] - n[12] * s[(12, 13)] * v[(12, 13)]) 
    n_[13] = n[13] + Decimal(0.0012) / w[13] * (A * po[13] * n[13] * w[13] + n[12] * s[(12, 13)] * v[(12, 13)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-3)) * n[12] * l[(12, 13)] + n[9] * s[(9, 13)] * v[(9, 13)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[9] * l[(9, 13)] - n[13] * s[(13, 14)] * v[(13, 14)]) 
    n_[14] = n[14] + Decimal(0.0012) / w[14] * (A * po[14] * n[14] * w[14] + n[13] * s[(13, 14)] * v[(13, 14)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-3)) * n[13] * l[(13, 14)] + n[9] * s[(9, 14)] * v[(9, 14)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[9] * l[(9, 14)] - n[14] * s[(14, 15)] * v[(14, 15)]) 
    n_[15] = n[15] + Decimal(0.0012) / w[15] * (A * po[15] * n[15] * w[15] + n[14] * s[(14, 15)] * v[(14, 15)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-3)) * n[14] * l[(14, 15)] - n[15] * s[(15, 16)] * v[(15, 16)] - n[15] * s[(15, 17)] * v[(15, 17)]) 
    #### in the line below was (15, 115) instead of (15, 16), but such edge doesn't exist
    n_[16] = n[16] + Decimal(0.0012) / w[16] * (A * po[16] * n[16] * w[16] + n[15] * s[(15, 16)] * v[(15, 16)] - Decimal(2 * math.pi) * n[15] * Decimal(21.97 * 10**(-3)) * l[(15, 16)]) 
    n_[17] = n[17] + Decimal(0.0012) / w[17] * (A * po[17] * n[17] * w[17] + n[15] * s[(15, 17)] * v[(15, 17)] - Decimal(2 * math.pi) * n[15] * Decimal(21.97 * 10**(-3)) * l[(15, 17)]) 

def calc_d():
    for edge in edges: 
        e = (edge.fr, edge.to) 
        d[e] = d[e] - Decimal(21.97 * 10**(-3)) * (Decimal(10**(-6)) / d[e]) * abs((n[edge.fr] + n[edge.to])) * Decimal(0.0012)

def change_n_and_po_if_d_is_negative():
    if d[(1, 2)] < 0:
        n_[2] = n[2] + Decimal(0.0012) / w[2] * (A * po[2] * n[2] * w[2] + n[7] * s[(7, 2)] * v[(7, 2)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[7] * l[(7, 2)] - n[2] * s[(2, 3)] * v[(2, 3)] ) 
        po_[2] = po[2] + Decimal(0.0012) / w[2] * (-B * po[2] * n[2] * w[2] + po[7] * s[(7, 2)] * v[(7, 2)] - po[2] * s[(2, 3)] * v[(2, 3)]) 
    if d[(2, 3)] < 0 :
        n_[3] = n[3] 
        po_[3] = po[3] 
        n_[2] = n[2] + Decimal(0.0012) / w[2] * (A * po[2] * n[2] * w[2] + n[1] * s[(1, 2)] * v[(1, 2)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[1] * l[(1, 2)] +n[7] * s[(7, 2)] * v[(7, 2)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[7] * l[(7, 2)]) 
        po_[2] = po[2] + Decimal(0.0012) / w[2] * (-B * po[2] * n[2] * w[2] + po[1] * s[(1, 2)] * v[(1, 2)] + po[7] * s[(7, 2)] * v[(7, 2)]) 
    if d[(3, 4)] < 0:
        n_[3] = n[3] + Decimal(0.0012) / w[3] * (A * po[3] * n[3] * w[3] + n[2] * s[(2, 3)] * v[(2, 3)] - Decimal(2 * math.pi) * n[2] * Decimal(21.97 * 10**(-3)) * l[(2, 3)]) 
        po_[3] = po[3] + Decimal(0.0012) / w[3] * (-B * po[3] * n[3] * w[3] + po[2] * s[(2, 3)] * v[(2, 3)]) 
        n_[4] = n[4] + Decimal(0.0012) / w[4] * (A * po[4] * n[4] * w[4] + n[8] * s[(8, 4)] * v[(8, 4)] - Decimal(2 * math.pi) * n[8] * Decimal(21.97 * 10**(-3)) * l[(8, 4)] - n[4] * s[(4, 5)] * v[(4, 5)] - n[4] * s[(4, 6)] * v[(4, 6)]) 
        po_[4] = po[4] + Decimal(0.0012) / w[4] * (-B * po[4] * n[4] * w[4] + po[8] * s[(8, 4)] * v[(8, 4)] - po[4] * s[(4, 5)] * v[(4, 5)] - po[4] * s[(4, 6)] * v[(4, 6)]) 
    if d[(7, 2)] < 0:
        n_[2] = n[2] + Decimal(0.0012) / w[2] * (A * po[2] * n[2] * w[2] + n[1] * s[(1, 2)] * v[(1, 2)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[1] * l[(1, 2)] - n[2] * s[(2, 3)] * v[(2, 3)]) 
        po_[2] = po[2] + Decimal(0.0012) / w[2] * (-B * po[2] * n[2] * w[2] + po[1] * s[(1, 2)] * v[(1, 2)] - po[2] * s[(2, 3)] * v[(2, 3)]) 
    if d[(7, 8)] < 0:
        n_[8] = n[8] 
        po_[8] = po[8] 
    if d[(8, 9)] < 0:
        n_[9] = n[9] 
        po_[9] = po[9] 
        n_[8] = n[8] + Decimal(0.0012) / w[8] * (A * po[8] * n[8] * w[8] + n[7] * s[(7, 8)] * v[(7, 8)] - Decimal(2 * math.pi) * n[7] * Decimal(21.97 * 10**(-3)) * l[(7, 8)] - n[8] * s[(8, 4)] * v[(8, 4)])
        po_[8] = po[8] + Decimal(0.0012) / w[8] * (-B * po[8] * n[8] * w[8] + po[7] * s[(7, 8)] * v[(7, 8)] - po[8] * s[(8, 4)] * v[(8, 4)]) 
    if d[(8, 4)] < 0:
        n_[4] = n[4] + Decimal(0.0012) / w[4] * (A * po[4] * n[4] * w[4] + n[3] * s[(3, 4)] * v[(3, 4)] - Decimal(2 * math.pi) * n[3] * Decimal(21.97 * 10**(-3)) * l[(3, 4)] - n[4] * s[(4, 5)] * v[(4, 5)] - n[4] * s[(4, 6)] * v[(4, 6)]) 
        po_[4] = po[4] + Decimal(0.0012) / w[4] * (-B * po[4] * n[4] * w[4] + po[3] * s[(3, 4)] * v[(3, 4)] - po[4] * s[(4, 5)] * v[(4, 5)] - po[4] * s[(4, 6)] * v[(4, 6)]) 
        n_[8] = n[8] + Decimal(0.0012) / w[8] * (A * po[8] * n[8] * w[8] + n[7] * s[(7, 8)] * v[(7, 8)] - Decimal(2 * math.pi) * n[7] * Decimal(21.97 * 10**(-3)) * l[(7, 8)] - n[8] * s[(8, 9)] * v[(8, 9)] ) 
        po_[8] = po[8] + Decimal(0.0012) / w[8] * (-B * po[8] * n[8] * w[8] + po[7] * s[(7, 8)] * v[(7, 8)] - po[8] * s[(8, 9)] * v[(8, 9)]) 
    if d[(9, 13)] < 0:
        n_[9] = n[9] + Decimal(0.0012) / w[9] * (A * po[9] * n[9] * w[9] + n[8] * s[(8, 9)] * v[(8, 9)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-2)) * n[8] * l[(8, 9)] - n[9] * s[(9, 10)] * v[(9, 10)] - n[9] * s[(9, 14)] * v[(9, 14)]) 
        n_[13] = n[13] + Decimal(0.0012) / w[13] * (A * po[13] * n[13] * w[13] + n[12] * s[(12, 13)] * v[(12, 13)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-3)) * n[12] * l[(12, 13)] - n[13] * s[(13, 14)] * v[(13, 14)]) 
    if d[(9, 14)] < 0:
        n_[9] = n[9] + Decimal(0.0012) / w[9] * (A * po[9] * n[9] * w[9] + n[8] * s[(8, 9)] * v[(8, 9)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-2)) * n[8] * l[(8, 9)] - n[9] * s[(9, 10)] * v[(9, 10)] - n[9] * s[(9, 13)] * v[(9, 13)]) 
        po_[9] = po[9] + Decimal(0.0012) / w[9] * (-B * po[9] * n[9] * w[9] + po[8] * s[(8, 9)] * v[(8, 9)] - po[9] * s[(9, 10)] * v[(9, 10)] - po[9] * s[(9, 13)] * v[(9, 13)]) 
        n_[14] = n[14] + Decimal(0.0012) / w[14] * (A * po[14] * n[14] * w[14] + n[13] * s[(13, 14)] * v[(13, 14)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-3)) * n[13] * l[(13, 14)] - n[14] * s[(14, 15)] * v[(14, 15)]) 
        po_[14] = po[14] + Decimal(0.0012) / w[14] * (-B * po[14] * n[14] * w[14] + po[13] * s[(13, 14)] * v[(13, 14)] - po[14] * s[(14, 15)] * v[(14, 15)]) 
    if d[(11, 12)] < 0:
        n_[12] = n[12] 
        po_[12] = po[12] 
    if d[(12, 13)] < 0:
        n_[12] = n[12] + Decimal(0.0012) / w[12] * (A * po[12] * n[12] * w[12] + n[11] * s[(11, 12)] * v[(11, 12)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-3)) * n[11] * l[(11, 12)]) 
        po_[12] = po[12] + Decimal(0.0012) / w[12] * (-B * po[12] * n[12] * w[12] + po[11] * s[(11, 12)] * v[(11, 12)]) 
        n_[13] = n[13] + Decimal(0.0012) / w[13] * (A * po[13] * n[13] * w[13] + n[9] * s[(9, 13)] * v[(9, 13)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[9] * l[(9, 13)] - n[13] * s[(13, 14)] * v[(13, 14)]) 
        po_[13] = po[13] + Decimal(0.0012) / w[13] * (-B * po[13] * n[13] * w[13] + po[9] * s[(9, 13)] * v[(9, 13)] - po[13] * s[(13, 14)] * v[(13, 14)]) 
    if d[(13, 14)] < 0:
        n_[13] = n[13] + Decimal(0.0012) / w[13] * (A * po[13] * n[13] * w[13] + n[12] * s[(12, 13)] * v[(12, 13)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-3)) * n[12] * l[(12, 13)] + n[9] * s[(9, 13)] * v[(9, 13)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[9] * l[(9, 13)]) 
        po_[13] = po[13] + Decimal(0.0012) / w[13] * (-B * po[13] * n[13] * w[13] + po[12] * s[(12, 13)] * v[(12, 13)] + po[9] * s[(9, 13)] * v[(9, 13)]) 
        n_[14] = n[14] + Decimal(0.0012) / w[14] * (A * po[14] * n[14] * w[14] + n[9] * s[(9, 14)] * v[(9, 14)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[9] * l[(9, 14)] - n[14] * s[(14, 15)] * v[(14, 15)]) 
        po_[14] = po[14] + Decimal(0.0012) / w[14] * (-B * po[14] * n[14] * w[14] + po[9] * s[(9, 14)] * v[(9, 14)] - po[14] * s[(14, 15)] * v[(14, 15)]) 
    # (15, 15) is strange
    if d[(14, 15)] < 0:
        n_[14] = n[14] + Decimal(0.0012) / w[14] * (A * po[14] * n[14] * w[14] + n[13] * s[(13, 14)] * v[(13, 14)] - Decimal(2 * math.pi) * Decimal(21.97 * 10**(-3)) * n[13] * l[(13, 14)] + n[9] * s[(9, 14)] * v[(9, 14)] - Decimal(2 * math.pi * 21.97 * 10**(-3)) * n[9] * l[(9, 14)])
        po_[14] = po[14] + Decimal(0.0012) / w[14] * (-B * po[14] * n[14] * w[14] + po[13] * s[(13, 14)] * v[(13, 14)] + po[9] * s[(9, 14)] * v[(9, 14)])
        n_[15] = n[15] 
        po_[15] = po[15]

def calc_po():
    global po_
    po_ = {} 
    po_[2] = po[2] + Decimal(0.0012) / w[2] * (-B * po[2] * n[2] * w[2] + po[1] * s[(1, 2)] * v[(1, 2)] + po[7] * s[(7, 2)] * v[(7, 2)] - po[2] * s[(2, 3)] * v[(2, 3)]) 
    po_[3] = po[3] + Decimal(0.0012) / w[3] * (-B * po[3] * n[3] * w[3] + po[2] * s[(2, 3)] * v[(2, 3)] - po[3] * s[(3, 4)] * v[(3, 4)]) 
    po_[4] = po[4] + Decimal(0.0012) / w[4] * (-B * po[4] * n[4] * w[4] + po[3] * s[(3, 4)] * v[(3, 4)] + po[8] * s[(8, 4)] * v[(8, 4)] - po[4] * s[(4, 5)] * v[(4, 5)] - po[4] * s[(4, 6)] * v[(4, 6)]) 
    po_[5] = po[5] + Decimal(0.0012) / w[5] * (-B * po[5] * n[5] * w[5] + po[4] * s[(4, 5)] * v[(4, 5)]) 
    po_[6] = po[6] + Decimal(0.0012) / w[6] * (-B * po[6] * n[6] * w[6] + po[4] * s[(4, 6)] * v[(4, 6)]) 
    po_[8] = po[8] + Decimal(0.0012) / w[8] * (-B * po[8] * n[8] * w[8] + po[7] * s[(7, 8)] * v[(7, 8)] - po[8] * s[(8, 9)] * v[(8, 9)] - po[8] * s[(8, 4)] * v[(8, 4)]) 
    po_[9] = po[9] + Decimal(0.0012) / w[9] * (-B * po[9] * n[9] * w[9] + po[8] * s[(8, 9)] * v[(8, 9)] - po[9] * s[(9, 10)] * v[(9, 10)] - po[9] * s[(9, 13)] * v[(9, 13)] - po[9] * s[(9, 14)] * v[(9, 14)])
    po_[10] = po[10] + Decimal(0.0012) / w[10] * (-B * po[10] * n[10] * w[10] + po[9] * s[(9, 10)] * v[(9, 10)]) 
    po_[12] = po[12] + Decimal(0.0012) / w[12] * (-B * po[12] * n[12] * w[12] + po[11] * s[(11, 12)] * v[(11, 12)] - po[12] * s[(12, 13)] * v[(12, 13)]) 
    po_[13] = po[13] + Decimal(0.0012) / w[13] * (-B * po[13] * n[13] * w[13] + po[12] * s[(12, 13)] * v[(12, 13)] + po[9] * s[(9, 13)] * v[(9, 13)] - po[13] * s[(13, 14)] * v[(13, 14)]) 
    po_[14] = po[14] + Decimal(0.0012) / w[14] * (-B * po[14] * n[14] * w[14] + po[13] * s[(13, 14)] * v[(13, 14)] + po[9] * s[(9, 14)] * v[(9, 14)] - po[14] * s[(14, 15)] * v[(14, 15)]) 
    po_[15] = po[15] + Decimal(0.0012) / w[15] * (-B * po[15] * n[15] * w[15] + po[14] * s[(14, 15)] * v[(14, 15)] - po[15] * s[(15, 16)] * v[(15, 16)] - po[15] * s[(15, 17)] * v[(15, 17)]) 
    po_[16] = po[16] + Decimal(0.0012) / w[16] * (-B * po[16] * n[16] * w[16] + po[15] * s[(15, 16)] * v[(15, 16)]) 
    po_[17] = po[17] + Decimal(0.0012) / w[17] * (-B * po[17] * n[17] * w[17] + po[15] * s[(15, 17)] * v[(15, 17)])


def find_pressures():
    vertex_id = defaultdict(lambda: None)
    vertex_by_id = defaultdict(lambda: None)
    c = 0
    for i in range(1, 18):
        if i not in corner_p:
            vertex_id[i] = c
            vertex_by_id[c] = i
            c += 1

    coefficients = [[0.0 for _ in range(9)] for _ in range(9)]
    values = [0.0 for _ in range(9)]

    def process_edge(eq_id, u, v, sign):
        e = get_edge[(u, v)]
        L1_ = L1[(u, v)]
        L2_ = e.length - L1_
        if sign == -1:
            (u, v) = (v, u)

        coef = math.pi * float(e.diameter**4) / (128.0 * (float(nu1) * float(L1_) + float(nu2) * float(L2_)))
        if u not in corner_p:
            coefficients[eq_id][vertex_id[u]] += coef
        else:
            values[eq_id] -= coef * float(p[u])
        if v not in corner_p:
            coefficients[eq_id][vertex_id[v]] -= coef
        else:
            values[eq_id] += coef * float(p[v])

    process_edge(0, 1, 2, 1)
    process_edge(0, 2, 3, -1)
    process_edge(0, 7, 2, 1)
    
    process_edge(1, 2, 3, 1)
    process_edge(1, 3, 4, -1)

    process_edge(2, 3, 4, 1)
    process_edge(2, 4, 5, -1)
    process_edge(2, 4, 6, -1)
    process_edge(2, 8, 4, 1)
    
    process_edge(3, 7, 8, 1)
    process_edge(3, 8, 4, -1)
    process_edge(3, 8, 9, -1)

    process_edge(4, 8, 9, 1)
    process_edge(4, 9, 10, -1)
    process_edge(4, 9, 13, -1)
    process_edge(4, 9, 14, -1)

    process_edge(5, 11, 12, 1)
    process_edge(5, 12, 13, -1)

    process_edge(6, 12, 13, 1)
    process_edge(6, 9, 13, 1)
    process_edge(6, 13, 14, -1)

    process_edge(7, 13, 14, 1)
    process_edge(7, 14, 15, -1)
    process_edge(7, 9, 14, 1)

    process_edge(8, 14, 15, 1)
    process_edge(8, 15, 16, -1)
    process_edge(8, 15, 17, -1)

    for i in range(9):
        for j in range(9):
            coefficients[i][j] = float(coefficients[i][j])
        values[i] = float(values[i])
    coeffs = np.array(coefficients)
    vals = np.array(values)

    result = list(map(Decimal, np.linalg.solve(coeffs, values)))
    print('Equation system solution: ' + str(result))

    for i in range(9):
        p[vertex_by_id[i]] = result[i]

    
    for edge in edges:
        e = (edge.fr, edge.to)
        re = (edge.to, edge.fr)
        d[e] = d[re] = edge.diameter
        l[e] = l[re] = edge.length
        q[e] = Decimal(math.pi) * edge.diameter**4 * abs(p[edge.fr] - p[edge.to]) / (Decimal(128 * 10**(-3)) * edge.length)
        s[e] = Decimal(math.pi) * edge.diameter**4 / Decimal(4)
        v[e] = q[e] / s[e]

    calc_n()
    calc_d()
    change_n_and_po_if_d_is_negative()
    calc_po()
    
    for vv in n_.keys():
        n[vv] = n_[vv]
    for vv in po_.keys():
        po[vv] = po_[vv]


def find_DT():
    dt = Decimal('Infinity')
    for edge in edges:
        L1_ = L1[(edge.fr, edge.to)]
        L2_ = edge.length - L1_
        v = abs(edge.diameter**2 * abs(p[edge.fr] - p[edge.to]) / (Decimal(32.0) * (nu1 * L1_ + nu2 * L2_)))
        new_dt = Decimal(0.01) * edge.length / v
        dt = min(dt, new_dt)
    return dt


def find_L1():
    new_l1 = defaultdict(lambda: Decimal(0.0))
    for edge in edges:
        L1_ = L1[(edge.fr, edge.to)]
        L2_ = edge.length - L1_
        new_l1[(edge.fr, edge.to)] = L1_ + DT * (edge.diameter**2 * (p[edge.fr] - p[edge.to])) / (Decimal(32) * (nu1 * L1_ + nu2 * L2_))
    for edge in edges:
        L1[(edge.fr, edge.to)] = new_l1[(edge.fr, edge.to)]

def to_str(d):
    s = ''
    for i, k in enumerate(d.keys()):
        s += str(k) + ': ' + str(d[k])
        if i + 1 < len(d.keys()):
            s += '\n'
    return s

def process():
    global DT
    step = 1
    while step <= 120:
        print('Processing step %d...' % step)
        find_pressures()
        DT = find_DT()
        print('Using DT = %.10f' % DT)
        find_L1()

        print('Pressures:\n' + to_str(p))
        print('L1:\n' + to_str(L1))
        
        print('N:\n' + to_str(n))
        ss = ''
        for i, k in enumerate(d.keys()):
            ss += str(k) + ': ' + (('d[%s] is full' % k) if d[k] < 0 else str(d[k]))
            if i + 1 < len(d.keys()):
                ss += '\n'
        print('D:\n' + ss)
        

        print('PO:\n' + to_str(po))
        
        print()
        
        all_L1_full = True
        for edge in edges:
            if abs(L1[(edge.fr, edge.to)] - edge.length) > 1e-5:
                all_L1_full = False
        if all_L1_full:
            break
        step += 1

def main():
    load_graph()
    process()

if __name__ == '__main__':
    main()