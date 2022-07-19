import itertools



def knapSack2(card_damages, card_costs, card_spaces, board_space, mana):
    n = len(card_damages)

    # generate all combinations of cards
    all_combinations = []
    for i in range(1, n + 1):
        all_combinations.extend(list(itertools.combinations(range(n), i)))
        
    max_damage = 0
    best_combination = []
    for ac in all_combinations:
        mana_cost = sum([card_costs[i] for i in ac])
        if mana_cost > mana:
            continue
        board_space_cost = sum([card_spaces[i] for i in ac])
        if board_space_cost > board_space:
            continue
        damage = sum([card_damages[i] for i in ac])
        if damage > max_damage:
            max_damage = damage
            best_combination = ac

    return (max_damage, best_combination)

print(knapSack2([1,2,3,4,5], [1,2,3,4,5], [1,0,1,1,0], 1, 10))