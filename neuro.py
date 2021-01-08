import neuro_library as nl
import matplotlib.pyplot as plt

#Создадим генетический алгоритм с обучающей выборкой
ga=nl.GeneticAlgorith()
ga.selection.append(nl.StudyMatrixItem([0,0],[0]))
ga.selection.append(nl.StudyMatrixItem([0,1],[1]))
ga.selection.append(nl.StudyMatrixItem([1,0],[1]))
ga.selection.append(nl.StudyMatrixItem([1,1],[0]))


#Создаем нейросеть
net=nl.NeuralNet(2,1)
net.create_layer(2,2,100)
net.create_layer(1,2,100)


#Выведем результат теста
for item in ga.selection:
    net.set_incomes(item.incomes)
    net.compute()
    print("Вход: ",item.incomes,"; выход желаемый: ",item.outcomes," выход реальный: ", net.outputs)

#Инициализиурем генетический алгоритм
ga.init_population_from_net(net,3)

print("-------------")

#задаем начальные массивы
x=[]
y=[]

#Проводим обучение
i=1
k=1
x.append(0)
y.append(ga.population[0].target_function) 
while i<=150:
    ga.next_age()
    x.append(i)
    y.append(ga.population[0].target_function)
    i=i+1
    k=k+1

#Выведем результат теста
print("После оптимизации")
net=ga.population[0]
for item in ga.selection:
    net.set_incomes(item.incomes)
    net.compute()
    print("Вход: ",item.incomes,"; выход желаемый: ",item.outcomes," выход реальный: ", net.outputs)
        

#Строим график
fig = plt.figure()
plt.plot(x, y)
     
#Отображаем заголовки и подписи осей
plt.title('График функции')
plt.ylabel('Ось Y')
plt.xlabel('Ось X')
plt.grid(True)
plt.show()
