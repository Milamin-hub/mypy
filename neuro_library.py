import numpy as np
import random as rnd
from abc import ABCMeta, abstractmethod
 
 
#Абстрактный класс передаточной функции
class TransFunc():
    __metaclass__=ABCMeta
 
    @abstractmethod
    def compute(self,income):
        """Рассчитать передаточную функцию"""
    
    @abstractmethod
    def get_id():
        """ИД передаточной функции"""
 
    @abstractmethod
    def mutation(level):
        """Мутация передаточной функции"""        
 
#Передаточная функция "Как есть"
class AsIs(TransFunc):
 
    def compute(self,income):
        return income
 
    def get_id(self):
        return 1    
    
assert issubclass(AsIs, TransFunc)
assert isinstance(AsIs(), TransFunc)
 
 
#Передаточная функция "Сигмоида"
class SignFunc(TransFunc):
    def __init__(self):
        self.par=1
        
    def compute(self,income):
        return 1/(1+np.exp(-self.par*income))
 
    def get_id(self):
        return 2       
    
assert issubclass(SignFunc, TransFunc)
assert isinstance(SignFunc(), TransFunc)
 
#Передаточная функция "Пороговая"
class ThresholdFunc(TransFunc):
    def compute(self,income):
        if income>0:
            return 1
        else:
            return 0
 
    def get_id(self):
        return 3       
    
assert issubclass(ThresholdFunc, TransFunc)
assert isinstance(ThresholdFunc(), TransFunc)
 
#Класс нейрона
class Neuron:
    def __init__(self, count, trans):
        self.inputs=[0]*count 
        self.weights=[rnd.random()-0.5 for i in range(count+1)]
        self.trans=trans
        self.output=0
 
    #Рассчитать нейрон
    def compute(self):
        res=0
        i=1
        count=len(self.weights)
        while i<count:
            res = res+(self.weights[i] * self.inputs[i-1])
            i=i+1
        res=res+self.weights[0]
        self.output = self.trans.compute(res)
 
print('Нейрон с передаточной функцией "Абстрактная"');
neuron=Neuron(5, TransFunc())
neuron.inputs=[1,2,3,4,5]
print(neuron.inputs)
print(neuron.weights)
neuron.compute()
print(neuron.output)
 
print('Нейрон с передаточной функцией "Как есть"');
neuron=Neuron(5, AsIs())
neuron.inputs=[1,2,3,4,5]
print(neuron.inputs)
print(neuron.weights)
neuron.compute()
print(neuron.output)
 
print('Нейрон с передаточной функцией "Сигмоида"');
neuron=Neuron(5, SignFunc())
neuron.inputs=[1,2,3,4,5]
print(neuron.inputs)
print(neuron.weights)
neuron.compute()
print(neuron.output)
 
print('Нейрон с передаточной функцией "Пороговая"');
neuron=Neuron(5, ThresholdFunc())
neuron.inputs=[1,2,3,4,5]
print(neuron.inputs)
print(neuron.weights)
neuron.compute()
print(neuron.output)
