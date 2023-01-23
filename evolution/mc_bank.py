import random
import matplotlib.pyplot as plt




def simulate(threshold, goal):
    level_up_cost = 10000
    balance = 5000
    minutes_passed = 0
    interest_rate = 0.1
    interest_increase = 0.1
    level_up_threshold = threshold
    mult = 1
    while balance < goal:
        minutes_passed += 1
        if minutes_passed % 10 == 0:
            mult += 1
        balance += balance * interest_rate 
        if balance >= goal:
            return(level_up_threshold, minutes_passed)
            break
        if balance >= mult*level_up_cost + level_up_threshold:
            balance -= level_up_cost * mult
            interest_rate += interest_increase * mult

def random_sim(minutes):
    level_up_cost = 10000
    balance = 5000
    minutes_passed = 0
    interest_rate = 0.1
    interest_increase = 0.1
    mult = 1
    choices = {}
    while minutes_passed < minutes:
        minutes_passed += 1
        balance += balance * interest_rate 
        if balance >= level_up_cost:
            max_upgrades = int(balance // level_up_cost)
            # get random amount between 0 and max_upgrades
            upgrades = random.randint(0, max_upgrades)
            if upgrades > 0:
                choices[minutes_passed] = (upgrades, balance)
            balance -= level_up_cost * upgrades
            interest_rate += interest_increase * upgrades
    return (balance, interest_rate, choices)

def random_sim_2(goal):
    level_up_cost = 10000
    balance = 5000
    minutes_passed = 0
    interest_rate = 0.1
    interest_increase = 0.1
    mult = 1
    choices = {}
    while balance < goal:
        minutes_passed += 1
        balance += balance * interest_rate 
        if balance >= level_up_cost:
            max_upgrades = int(balance // level_up_cost)
            # get random amount between 0 and max_upgrades
            upgrades = random.randint(0, max_upgrades)
            if upgrades > 0:
                choices[minutes_passed] = (upgrades, balance)
            balance -= level_up_cost * upgrades
            interest_rate += interest_increase * upgrades
    return (minutes_passed, interest_rate, choices)




def main():
    min_mins = 9999
    max_ir = 0
    max_choices = {}
    c = 0
    while True:
        c += 1
        m,i_r,ch = random_sim_2(goal=100000000)
        if m < min_mins:
            max_ir = i_r
            min_mins = m
            max_choices = ch
            print("New min:", min_mins, "New max:", max_ir, "c:", c, "ch:", max_choices)
        else:
            if c % 500000 == 0:
                print("New min:", min_mins, "New max:", max_ir, "c:", c, "ch:", max_choices)





def main3():
    max_ir = 0
    max_b = 0
    max_choices = {}
    c = 0
    while True:
        c += 1
        b,i_r,ch = random_sim(minutes=30)
        if b > max_b:
            max_ir = i_r
            max_b = b
            max_choices = ch
            print("max_ir:", max_ir, "max_b:", max_b, "c:", c, "ch:", max_choices)
        elif b == max_b:
            if i_r > max_ir:
                max_ir = i_r
                max_b = b
                max_choices = ch
                print("max_ir:", max_ir, "max_b:", max_b, "c:", c, "ch:", max_choices)
        else:
            if c % 100000 == 0:
                print("max_ir:", max_ir, "max_b:", max_b, "c:", c, "ch:", max_choices)
    
def main2():
    max_ir = 0
    max_b = 0
    max_choices = {}
    c = 0
    while True:
        c += 1
        b,i_r,ch = random_sim(minutes=30)
        if i_r > max_ir:
            max_ir = i_r
            max_b = b
            max_choices = ch
            print("max_ir:", max_ir, "max_b:", max_b, "c:", c, "ch:", max_choices)
        elif i_r == max_ir:
            if b > max_b * 1.01:
                max_ir = i_r
                max_b = b
                max_choices = ch
                print("max_ir:", max_ir, "max_b:", max_b, "c:", c, "ch:", max_choices)
        else:
            if c % 100000 == 0:
                print("max_ir:", max_ir, "max_b:", max_b, "c:", c, "ch:", max_choices)
# plot the results
# disable scientific notation
def main1():
    goal = 1000000
    next_threshold = 100
    last_min_passed = 9999
    min_minutes_passed = 9999
    multi = 0.5
    last_threshold = next_threshold
    last_c = 0
    last_m = 9999
    while True:
        if last_min_passed == last_m:
            last_c += 1
            if last_c > 35:
                break
        else:
            last_c = 0
            last_m = last_min_passed

        threshold, min_passed = simulate(next_threshold, goal)
        print(last_threshold, last_min_passed)
        if min_passed <= last_min_passed:
            if threshold >= last_threshold:
                last_threshold = threshold
                last_min_passed = min_passed
                next_threshold = threshold * (1 + multi)
            else:
                last_threshold = threshold
                last_min_passed = min_passed
                next_threshold = threshold * (1 - multi)
            
            min_minutes_passed = min_passed
        else:
            multi *= 0.99
            if threshold > last_threshold:
                last_threshold = threshold
                last_min_passed = min_passed
                next_threshold = threshold * (1 - multi)
            else:
                last_threshold = threshold
                last_min_passed = min_passed
                next_threshold = threshold * (1 + multi)

        






def main_gen(minutes = 30, gens = 1000000):
    best_mut = 10
    rand_mut = 20
    m_rate = 0.5
    init_evos = best_mut + rand_mut
    # generate initial unique evos
    evos = []
    for i in range(init_evos):
        evos.append([[0 for i in range(minutes)], None])


    ev_cutoff = 200
    
    
    for gens in range(0, gens+1):

        # get the 10 best evos and 20 random evos and mutae them
        for i in range(0, best_mut):
            new_evo = mutate(evos[i][0],rate=m_rate)
            if new_evo not in [e[0] for e in evos]:
                evos.append([new_evo, None])
            
        for i in range(0, rand_mut):
            new_evo = mutate(random.choice(evos)[0],rate=m_rate)
            if new_evo not in [e[0] for e in evos]:
                evos.append([new_evo, None])
        
        # calculate fitness of each evolution
        for i in range(0, len(evos)):
            if evos[i][1] is None:
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
        



        




        
        if gens % 1000 == 0 and gens > 0:
            print("Generation:", gens)
            for i in range(0, 3):
                print(evos[i][0], evos[i][1])
        
 

# mutatuion function
def mutate(evo, rate = 0.1):
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


def sim(arr):

    level_up_cost = 20000
    balance = 5000
    minutes_passed = 0
    interest_rate = 0.2
    interest_increase = 0.1

    for i in arr:
        balance -= level_up_cost * i
        interest_rate += interest_increase * i
        minutes_passed += 1
        balance += balance * interest_rate
    
    return (balance, interest_rate)



if __name__ == '__main__':
    main_gen()