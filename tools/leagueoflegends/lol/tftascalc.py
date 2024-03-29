import matplotlib.pyplot as plt

base = 1
rb = 0.40
gb = 0.15
gs = 0.01
max_as = 5

def calc(n_rb, n_g, max_time):
    bas = base + n_rb*rb + n_g
    time = 0
    res = []
    atks = 0
    while time < max_time:
        time += 1 / bas
        atks += 1
        res.append([round(time,2),round(bas,2),round(atks,2)])
        bas += n_g * gs
        if bas > max_as:
            bas = max_as
    return res

if __name__ == '__main__':
    m = 10
    d1 = calc(1, 0, m)
    d2 = calc(2, 0, m)
    d3 = calc(0, 1, m)
    d4 = calc(0, 2, m)
    d5 = calc(1, 1, m)
    ds = [d1,d2,d3,d4,d5]
    lbs = ["redbuff", "double redbuff", "rage b", "double rage b", "one both"]
    # Extract time and attack count
    for i,d in enumerate(ds):
        time = [x[0] for x in d]
        attacks = [x[2] for x in d]

        # Plot the data
        plt.plot(time, attacks, label = lbs[i])

    # Labels and title
    plt.xlabel('Time (seconds)')
    plt.ylabel('Attacks')
    plt.title('TFT Attack Speed Simulation with Rageblade')
    plt.legend()

    # Show the graph
    plt.show()

