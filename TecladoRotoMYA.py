#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:43:54 2021

@author: MYA
"""

class Node:
    def __init__(self, val=None, next=None):
        self.val= val
        self.next = next
def imprimirLista(head):
    temp = head
    while temp:
        print(temp.val, end="")
        temp=temp.next
    print() 
def broken(s: str):
    cabeza = Node() #defino la cabeza como un nodo
    tail = cabeza #hago la cabeza igual a la cola
    pos = tail #hago la posicion actual la cola
    for ch in s:
        if ch == "[":
            pos = cabeza #hago la posicion igual a la cabeza(como poner ese caracter de primero)
            continue
        elif ch == "]":
            pos = tail  #hago la posicion igual a la cola (caracter al final)
            continue
        node = Node(ch, pos.next)
        pos.next = node #el Nodo con el caracter apunta al siguiente de pos
        if pos == tail: 
            tail = node #hago la cola ese caracter específico
        pos = node #en las otras posiciones pongo el nodo
       
    return cabeza.next


s="A[BC]D"
S1=broken(s)
ss=imprimirLista(S1)