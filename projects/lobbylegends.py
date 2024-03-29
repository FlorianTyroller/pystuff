import random
from statistics import mean
import matplotlib.pyplot as plt
import concurrent.futures

points = [0,1,2,3,4,5,6,7]
mxs = []
mis = []
avgs = []
chs = []

tries = 8000
cher = 100



def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def sim(ches):
    for che in ches:
        cs = []
        for i in range(tries):
            end = False 
            c = 0
            player = [0,0,0,0,0,0,0,0]
            while not end:
                random.shuffle(points)
                for j,p in enumerate(points):
                    if player[j] >= che and p == 7:
                        player[j] += p
                        end = True
                    else:
                        player[j] += p
                c += 1
            cs.append(c)
        mxs.append(max(cs))
        mis.append(min(cs))
        avgs.append(mean(cs))
        chs.append(che)
    
    return "done"

def main():
    
    chss = [[i*10 + j for i in range(10)] for j in range(10)]
    for ccc in chss:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(sim, ccc)
            for result in results:
                print(result)
        
    plt.plot(chs, mxs, chs, mis, chs, avgs)
    plt.ylabel('rounds')
    plt.xlabel('points needed for check')
    plt.show()
    
if __name__ == "__main__":
    main()


