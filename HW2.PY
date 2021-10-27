import csv
import matplotlib.pyplot as plt

data = []
with open('us_statepop.csv', 'r') as f:
    statepop = csv.reader(f)
    for row in statepop:
        data.append(row)
#print(data)

CA_chunk = data[520:541]
#print(CA_chunk)
NY_chunk = data[4070:4091]
#print(NY_chunk)

#getting actual numbers for each state
CA_numbers = []
for row in CA_chunk:
    CA_numbers.append(row[2])
NY_numbers = []
for row in NY_chunk:
    NY_numbers.append(row[2])

years = []
for row in CA_chunk:
    years.append(row[1])



xs = years
ys = NY_numbers
ps = CA_numbers

fig, ax = plt.subplots()
ax.plot(xs, ys, 'y', label = 'NY')
ax.plot(xs, ps, 'm', label = 'CA')
ax.tick_params
ax.set_xticks(ax.get_xticks()[::1])
plt.title('California vs. New York Population Growth')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.show()

#storing our data
pokedata=[]
with open('pokedex.csv', 'r') as f:
    poke_info = csv.reader(f)
    for row in poke_info:
        pokedata.append(row)
#print(pokedata)
#print(pokedata[1:2])

#getting number of grass pokemon in pokedex
grass_num = 0
for list in pokedata:
    for info in list:
        if 'Grass' == info:
            grass_num += 1

#getting number of fire pokemon in pokedex
fire_num = 0
for list in pokedata:
    for info in list:
        if 'Fire' == info:
            fire_num += 1

print(fire_num)

#getting number of steel pokemon in pokedex
steel_num = 0
for list in pokedata:
    for info in list:
        if 'Steel' == info:
            steel_num += 1
print(steel_num)

#dictionary after collecting data and needed to do my bar graph
pokegraph = {'Grass': grass_num, 'Fire': fire_num, 'Steel': steel_num}
type = pokegraph.keys()
number = pokegraph.values()

fig, ax = plt.subplots()
ax.bar(type, number)
plt.bar('Grass', height = 95, color = 'g') #changing color of bar
plt.bar('Fire', height = 64, color = 'r')  #changing color of bar
plt.bar('Steel', height = 49, color = 'k') #changing color of bar
plt.title('Measuring Number of Grass, Fire, and Steel Pokemon in Pokedex')
plt.ylabel('Frequency')
plt.xlabel('Pokemon Type')
plt.show()
