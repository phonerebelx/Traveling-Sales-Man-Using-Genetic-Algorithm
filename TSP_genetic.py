import random
import string
import copy
import city_creation
import math


# -------------------------- pathetic variable name ---------------------------------
class update:
    def __init__(self):
        self.i = 0

    def check_common2(self):
        self.i += 1
        return self.i


graph = {}
sol = update()
if sol.check_common2() == 1:
    check = city_creation.list_Check().lst
check3 = []

for i in range(len(check) - 1):
    for j in range(len(check) - i - 2):
        check3.append(check[i])
index = 1
index2 = 0
while index2 < len(check3):
    for l in range(index, len(check) - 1):
        check3[index2] += check[l]
        index2 += 1
    index += 1

for i in range(len(check3)):
    graph[check3[i]] = random.randint(1000, 100000)



class chromo:

    def __init__(self):

        self.gene = [None] * 11

        self.gene[0] = check[0]
        self.gene[-1] = check[-1]

        for i in range(1, len(check) - 1):
            var = random.choice(string.ascii_uppercase)
            while True:
                if var in check:
                    self.gene[i] = var
                    break
                var = random.choice(string.ascii_uppercase)

        for i in range(1, len(check)):
            if check[i] not in self.gene:
                for k in range(1, len(self.gene) - 1):
                    if self.gene[k] in self.gene[k + 1:]:
                        self.gene[k] = check[i]

        self.evaluate()

    def evaluate(self):
        self.fitness = 0
        str1 = ''
        for i in range(len(self.gene) - 1):
            str1 += self.gene[i]
            str1 += self.gene[i + 1]

            if str1 not in check3:
                str1 = ''
                str1 += self.gene[i + 1]
                str1 += self.gene[i]
                # print(str1)

            self.fitness += graph[str1]
            str1 = ''


population = []
for i in range(50):
    population.append(chromo())


# -----------------------------------------------------------------------------------------------
# Just check that element will repeat or not in list
# for i in range(len(population)):
#     for j in population[i].gene:
#         if j in population[i].gene[population[i].gene.index(j)+1:]:
#             print(j)
# -----------------------------------------------------------------------------------------------



class operators:


    def truncation(self, pop):
        new_population = sorted(pop, key=lambda x: x.fitness, reverse=True)
        return new_population[0], new_population[1]

    def mutate(self,child):
        replace_obj_1 = random.randint(1,len(child.gene)-2)
        replace_obj_2 = random.randint(1,len(child.gene)-2)
        while True:
            if replace_obj_2 == replace_obj_1:
                replace_obj_2 = random.randint(1, len(child.gene) - 2)
            else:
                break
        child.gene[replace_obj_1],child.gene[replace_obj_2] = child.gene[replace_obj_2],child.gene[replace_obj_1]
        chromo.evaluate(child)
        return child


    def crossover(self, parent1, parent2):
        child2 = copy.deepcopy(parent2)
        index = math.ceil(len(parent1.gene) / 2)
        par_child_list = [parent2, parent1]
        ppp = [+1, -1]
        deleted_list = []

        for k in range(4):
            if k == 2:
                par_child_list[0], par_child_list[1] = par_child_list[1], child2
            if k % 2 == 0:
                for i in range(index, len(par_child_list[k % 2].gene) - 1):
                    pop_element = par_child_list[k % 2].gene.pop(
                        par_child_list[k % 2].gene.index(par_child_list[k % 2 + ppp[k % 2]].gene[i]))
                    deleted_list.append(pop_element)
            else:
                for i in range(index, len(par_child_list[k % 2].gene) - 1):
                    check_index = random.randint(0, len(deleted_list) - 1)
                    par_child_list[k % 2 + ppp[k % 2]].gene.insert(len(par_child_list[k % 2 + ppp[k % 2]].gene) - 1,
                                                                   deleted_list[check_index])
                    deleted_list.remove(deleted_list[check_index])


        child1 = parent1
        child2 = parent2
        chromo.evaluate(child1)
        chromo.evaluate(child2)
        return child1, child2


#
#
    def sur_truncation(self,pop):

        pop = sorted(pop, key = lambda x:x.fitness, reverse = True)

        return pop[len(pop)-10:]


solution = operators()
check_count = 0
ind = 0
check_index = float('inf')
while True:
    new_pop = []
    for i in range(5):

        parent1, parent2 = solution.truncation(population)
        child1, child2 = solution.crossover(parent1, parent2)
        number = random.random()


        if random.random() < .5:

            child1 = solution.mutate(child1)

        else:
            child2 = solution.mutate(child2)

        new_pop.append(child1)
        new_pop.append(child2)
    print('************************************ generation count',ind)
    pop = solution.sur_truncation(population+new_pop)

    new_index = pop[-1].fitness
    if new_index < check_index:
        check_index = new_index
        check_count = 0
    else:
        check_count += 1
    if check_count == 1000:
        break
    for item in pop:
        print(item.gene, item.fitness)

    ind+=1