from time import time
udt=list('0123456789')
N=50
pila=[]
EP=[]
elp=[]
exp=[]
expresion=[]
tope=-1
start=time()
def llena():
    if(tope==(N-1)):
        
        return True
    return False

def vacia():
    if(tope==-1):
        
        return True
    return False

def push(dato):
    if(llena()!=True):
        global tope
        tope=tope+1
        pila.insert(tope,dato)

def pop():
    if(vacia()!=True):
        global tope
        aux=pila[tope]
        del pila[tope]
        tope=tope-1
        return aux
    else:
        return -9999

def infijo(i, EI):
    if(EI[i]=='^'):
        prioridadop=4
        return prioridadop
    elif(EI[i]=='*'):
        prioridadop=2
        return prioridadop
    elif(EI[i]=='/'):
        prioridadop=2
        return prioridadop
    elif(EI[i]=='+'):
        prioridadop=1
        return prioridadop
    elif(EI[i]=='-'):
        prioridadop=1
        return prioridadop
    elif(EI[i]=='('):
        prioridadop=5
        return prioridadop

def pripila(pila):
    if(pila[tope]=='^'):
        prioridadpi=3
        return prioridadpi
    elif(pila[tope]=='*'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='/'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='+'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='-'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='('):
        prioridadpi=0
        return prioridadpi

eistring=input('Ingrese Operacion sin espacios: ')
EI=list(eistring.upper()) #El método upper () devuelve una copia de la cadena en la que todos los caracteres basados ​​en mayúsculas y minúsculas se han duplicado.

for i in range(len(EI)):
    if(EI[i] in udt):      #EI es operando
        EP.append(EI[i]) #agrega un solo elemento al final de la lista
    elif(EI[i]!=')'):                       #EI es diferente a ')'
        if (tope==-1):                      #Pila no esta vacia
            push(EI[i])
        else:
            if(infijo(i,EI)<=pripila(pila)):#operador de EI es <= a operador de pila
                EP.append(pop())                
                push(EI[i])
            elif(infijo(i,EI)>pripila(pila)):#operador de EI es > a operador de pila
                push(EI[i])
    elif(EI[i]==')'):                       #EI es igual a ')'
        while (pila[tope]!='('):            #Pila es diferente a '('
            EP.append(pop())
        if(pila[tope]=='('):                #Pila es igual a '('
            pop()
        elif(tope!=-1):                     #Pila no esta vacia
            EP.append(pop())

while (tope>-1):                
    EP.append(pop())
s= ''
for i in range(len(EP)):
    if(EP[i] in udt):
        elp.append(EP[i])
    else:
        expresion=str(EP[i])   
        if(len(elp)>0):
            expresion=expresion+str(elp.pop()) 
            if(len(elp)>0):
                expresion=str(elp.pop())+expresion
            exp.append(expresion)
        elif(len(exp)>0):
            expresion=expresion+str(exp.pop())
            exp.append(expresion)

print ('posfijo: ' + s.join(EP)+'\n') 
lim=len(exp)

for i in range(lim):
   print(exp.pop()+'\n')
    
end=time()-start
print('tiempo de ejecucion: '+str(end))