'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 
2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem 
que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem 
avisando se o número informado pertence ou não a sequência. 

  

IMPORTANTE:  

	Esse número pode ser informado através de qualquer entrada de sua preferência ou
 pode ser previamente definido no código; '''
 
def fib():
    fib = int(input('Digite um numero: '))
    isfib = False    
    fib_list = [0,1]
    
    while fib_list[-1] < fib:
        head = fib_list[-1]
        tail = fib_list[-2]
        head = head + tail
        
        if fib == head:
            isfib = True
            break
        
        fib_list.append(head)
        print(fib_list)
    
    if isfib:
        print("Pertence")
    else:
        print("Não pertence")
        
fib()