import random
import matplotlib.pyplot as plt
# imoprt deep copy
import copy


def main_gen(steps = 20, gens = 1000000):
    best_mut = 10
    rand_mut = 20
    m_rate = 0.5
    building_count = 2
    init_evos = best_mut + rand_mut
    # generate initial unique evos
    evos = []
    for i in range(init_evos):
        evos.append([[[0,0] for i in range(steps)], None])


    ev_cutoff = 200
    
    
    for gens in range(0, gens+1):

        # get the 10 best evos and 20 random evos and mutae them
        for i in range(0, best_mut):
            old_evo = evos[i][0]
            new_evo = mutate(old_evo,rate=m_rate)
            if hash(str(new_evo)) is not hash(str(old_evo)):
                evos.append([new_evo, sim(new_evo)])
            
        for i in range(0, rand_mut):
            old_evo = random.choice(evos)[0]
            new_evo = mutate(old_evo,rate=m_rate)
            # calculate the the hash of the new evolution and check if it is already in the list

            if hash(str(new_evo)) is not hash(str(old_evo)):
                evos.append([new_evo, sim(new_evo)])



        
        # calculate fitness of each evolution
        for i in range(0, len(evos)):
            if evos[i][1] is None:
                # print("simt",sim(evos[i][0]))
                evos[i][1] = sim(evos[i][0])
        
        # sort evolutions by fitness, highest first
        evos.sort(key=lambda x: x[1][0], reverse=True)
        # get the best x evolutions
        evos = evos[:ev_cutoff]

        '''

        # plot the all evos
        if gens % 100 == 0:
            print("Generation:", gens, "Best:", evos[0][1][0], "Best IR:", evos[0][1][1])
            # plot all evos, y axis goin from 0 to max of all evos
            plt.plot([e[1][0] for e in evos])
            plt.ylim([0, evos[0][1][0]])
            plt.show()


            
            #plt.plot([i for i in range(len(evos))],[e[1][0] for e in evos])
            #plt.show()

        '''
        



        
        # print(evos[0])



        
        if gens % 1000 == 0 and gens > 0:
            print("Generation:", gens)
            for i in range(0, 3):
                print(evos[i][0], evos[i][1])
        
 

# mutatuion function
def mutate_percent(evo, rate = 0.1):
    mut_range = 0.1
    # copy the evolution
    new_evo = evo.copy()
    # get a random index
    index = random.randint(0, len(new_evo) - 1)
    # mutate the index by adding or substracting an integer between +/- 10% of the current value
    new_evo[index] += random.randint(-int(new_evo[index] * mut_range)-1, int(new_evo[index] * mut_range+1))
    if new_evo[index] < 0:
        new_evo[index] = 0
    # mutate the new evolution again
    return mutate(new_evo, rate*0.6) if random.random() < rate else new_evo

def mutate(evo, rate = 0.1):
    # deep copy the evolution
    new_evo = copy.deepcopy(evo)
    # get a random index
    index = random.randint(0, len(new_evo) - 1)
    index2 = random.randint(0, len(new_evo[index]) - 1)
    # mutate the index by adding or substracting an integer between +/- 1 of the current value
    new_evo[index][index2] += random.randint(-1, 1)
    if new_evo[index][index2] < 0:
        new_evo[index][index2] = 0
    # mutate the new evolution again
    return mutate(new_evo, rate*0.6) if random.random() < rate else new_evo


def sim(arr):
    cpm = 0.1 # cookies per minute, start at 0.1
    building_count = [1,0] # start with 1 cursor
    building_cost = [0.1,100] # cursor cost 15, grandma cost 100
    building_cpm = [4,1] # cursor gives 0.1 cpm, grandma gives 1 cpm
    price_mult = 1.15 # price multiplier
    cookies = 50
    
    


    for s in arr:
        for building, upgrades in enumerate(s):
            for i in range(upgrades):
                cookies -= building_cost[building] * price_mult ** building_count[building]
                building_count[building] += 1
                cpm += building_cpm[building]
        if cookies < 0:
            return -9999, -9999
        
        cookies += cpm

    if cookies < 0:
        return -9999, -9999

    return cookies, cpm



if __name__ == '__main__':
    # print(sim([[2, 7], [1, 1], [2, 0], [6, 11], [7, 7]]))
    main_gen()
    