import random
from typing import List

Genome = List[int]
Population = List[Genome]

def gen_genome(length: int) -> Genome:
    return random.choices([0, 1], k=length)

def gen_population(size: int, genome_length: int) -> Population:
    return [gen_genome(genome_length) for _ in range(size)]


def fitness(genome: Genome, things: [Thing], weight_limit: int) -> int:
    