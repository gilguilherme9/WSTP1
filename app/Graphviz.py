# -*- coding: utf-8 -*-
from grafo import Grafo
from graphviz import Source
import pandas as pd
from staticvars.staticpaths import pathtocsv
import re

relations = []
triples = []
pathtocsv= pathtocsv

def maketriples(filepath):
    counter = 1
    csvfile = pd.read_csv(filepath)
    csvfile.drop_duplicates(inplace=True, keep='first')
    for row in csvfile:
        relations.append(row)

    for relation in relations:
        for value in csvfile[relation]:
            triples.append((counter, relation, value))
            counter += 1
        counter = 1
    return triples

graph = Grafo()
triples=maketriples(pathtocsv)


for triple in triples:
    graph.add(triple[0],triple[1],triple[2])

def triples2dot(triples):
    dot = \
        """ 
        graph "grafo" { 
        overlap = "scale"; 
        """

    for s, p, o in triples:
        dot = dot + ('%s -- %s [label=%s]\n' % (re.sub('[^A-Za-z0-9]+', '', str(s)), re.sub('[^A-Za-z0-9]+', '', str(o)), re.sub('[^A-Za-z0-9]+', '', str(p))))
    dot = dot + "}"
    return dot

def tracegraph():
    triples = graph.triples(None,None,None)
    dot = triples2dot(list(triples))
    g = Source(dot, "relations.gv", "dotout", "pdf", "neato")
    g.render(view=False)
