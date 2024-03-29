import pygame
import random
from math import sqrt

from pygame.locals import *


pygame.font.init() 
myfont = pygame.font.SysFont("Times New Roman",20)

# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 820,820

scale = 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def dist(a,b):
    d = (a[0][0] - b[0][0])**2 + (a[0][1] - b[0][1])**2
    return int(sqrt(d))

def generateMap(nodeCount = 10, min_dist = 100, max_connections = 3, min_connections = 2):
    nodeList = []

    # generate a random x and y coordinate inside the screen
    while len(nodeList) < nodeCount:
        x = random.randint(0, SCREEN_WIDTH//scale)
        y = random.randint(0, SCREEN_HEIGHT//scale)


        # check if the node is too close to another node
        tooClose = False
        for node in nodeList:
            if (x - node[0][0])**2 + (y - node[0][1])**2 < min_dist**2:
                tooClose = True
                break
        
        if tooClose:
            continue
        name = str(len(nodeList))
        nodeList.append(((x,y),name))

    # make a adjacency matrix for the connections between the nodes
    adjMatrix = [[0 for i in range(nodeCount)] for j in range(nodeCount)]
    # for every node generate an edge to another node between  and inclusive min_connections and max_connections, 
    for i in range(nodeCount):
        connections = random.randint(min_connections, max_connections)
        
        # get the index of the nearest nodes to the current node where there is no connection yet
        nearestNodes = []
        for j in range(nodeCount):
            if i != j:
                nearestNodes.append((j,dist(nodeList[i],nodeList[j])))
        nearestNodes.sort(key=lambda x: x[1])

        # only get the first connections nodes
        nearestNodes = nearestNodes[:connections]

        for node in nearestNodes:
            if adjMatrix[i][j] == 0 and adjMatrix[j][i] == 0:
                nodeIndex = node[0]
                distance = dist(nodeList[i],nodeList[nodeIndex])
                adjMatrix[i][nodeIndex] = distance
                adjMatrix[nodeIndex][i] = distance

    """# print the adjacency matrix
    for i in range(nodeCount):
        print(adjMatrix[i])"""
    
    return nodeList, adjMatrix


def fitness(nodeList,adjMatrix,order, problemNodes):
    fitness = 0

    for node_ind in order:
        if node_ind in problemNodes:
            fitness -= 100000
    
    for i in range(len(order)):
        if adjMatrix[order[i]][order[(i+1) % len(order)]] == 0:
            fitness += 100000
        fitness += adjMatrix[order[i]][order[(i+1) % len(order)]]
    
    return fitness


            
def solveProblem(nodeList,adjMatrix,problemNodes, problemAdjMatrix = None, population = None):
    # generate adjMatrix but only with the problem nodes from the given adjMatrix
    if problemAdjMatrix == None:
        problemAdjMatrix = [[0 for i in range(len(problemNodes))] for j in range(len(problemNodes))]
        for i in range(len(problemNodes)):
            for j in range(len(problemNodes)):
                problemAdjMatrix[i][j] = adjMatrix[problemNodes[i]][problemNodes[j]]

    # generate initial generation
    if population == None:
        population = []
        while len(population) < 100:
            order = random.sample(range(len(nodeList)),len(nodeList))
            if order not in population:
                population.append(order)
    else:
        # only keep the best 50 solutions
        population = population[:50]
        # generate 50 new solutions
        while len(population) < 100:
            # choose a solution and swap 2 random nodes
            order = population[random.randint(0,len(population)-1)].copy()
            a = random.randint(0,len(order)-1)
            b = random.randint(0,len(order)-1)
            order[a],order[b] = order[b],order[a]
            if order not in population:
                population.append(order)

            
        
    

    # calculate the fitness of the initial generation
    fitnesses = []
    for order in population:
        fitnesses.append(fitness(nodeList,adjMatrix,order,problemNodes))
    
    # sort the population according to the fitness
    population = [x for _,x in sorted(zip(fitnesses,population))]
    fitnesses.sort()




    return problemAdjMatrix, population


        

        



def main():
    run = True
    draw_edges = True
    draw_weight = True
    draw_names = True
    bestSolution = []
    node_count = 30
    node_problem_count = 30
    max_connections = 5
    min_connections = 2
    min_dist = 100
    problemNodes = []
    nodeList, adjMatrix = generateMap(node_count,min_dist,max_connections,min_connections)
    problemAdjMatrix = None
    population = None

    while run:
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:

                e = event.key 
                if e == K_ESCAPE:
                    run = False
                elif e == K_SPACE:
                    nodeList, adjMatrix = generateMap(node_count,min_dist,max_connections,min_connections)
                    # clear the screen
                    """print(nodeList)
                    print(adjMatrix)"""
                elif e == K_e:
                    draw_edges = not draw_edges
                elif e == K_w:
                    draw_weight = not draw_weight
                elif e == K_n:
                    draw_names = not draw_names
                elif e == K_s:
                    # select random nodes, according to the node_problem_count, there should be no duplicate nodes
                    problemNodes = []
                    if node_problem_count > node_count:
                        node_problem_count = node_count
                    while len(problemNodes) < node_problem_count:
                        node = random.randint(0,node_count-1)
                        if node not in problemNodes:
                            problemNodes.append(node)
                    
                    print(problemNodes)
                elif e == K_c:
                    # solve the problem
                    for i in range(5000):
                        problemAdjMatrix, population = solveProblem(nodeList,adjMatrix,problemNodes,problemAdjMatrix,population)
                    bestSolution = population[0]
                    print(bestSolution)
                    # print(adjMatrix)

                screen.fill((0,0,0))

            elif event.type == pygame.QUIT:
                    run = False
        
        
        
        # draw the edges
        if draw_edges:
            for i in range(node_count):
                for j in range(node_count):
                    if adjMatrix[i][j] != 0:
                        pygame.draw.line(screen, (255,255,255), nodeList[i][0], nodeList[j][0], 1)
                        # add a label to the edge with the weight
                        if draw_weight:
                            textsurface = myfont.render(str(adjMatrix[i][j]), False, (255, 255, 255))
                            screen.blit(textsurface,((nodeList[i][0][0] + nodeList[j][0][0])//2,(nodeList[i][0][1] + nodeList[j][0][1])//2))
        

        # draw the best solution
        if len(bestSolution) > 0:
            for i in range(len(bestSolution)):
                pygame.draw.line(screen, (255,0,0), nodeList[bestSolution[i]][0], nodeList[bestSolution[(i+1) % len(bestSolution)]][0], 2)

        # draw the nodes
        for i,node in enumerate(nodeList):
            if i in problemNodes:
                pygame.draw.circle(screen, (255,100,0), node[0], 7)
            else:
                pygame.draw.circle(screen, (200,200,200), node[0], 5)
            if draw_names:
                textsurface = myfont.render(node[1], False, (0, 255, 255))
                screen.blit(textsurface,(node[0][0],node[0][1]))
        
        pygame.display.flip()


    pygame.quit()


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")