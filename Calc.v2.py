# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YiJu5uhj3zAYopWvCjaJfcsx0F0mq23K
"""

#Inicio
print("Bem vindo à calculadora")

x = float(input("Primeiro nº:"))
op = input("Operação:")
y = float(input("Segundo nº:"))

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    if y == 0:
        print("Erro: divisão por 0 não permitida")
    else:
        print(x / y)
else:
    print("Operação inválida ou não suportada")

#Fim