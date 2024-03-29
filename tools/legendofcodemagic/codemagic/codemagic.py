import sys
import math
import time
import itertools



# keywords

charge_mod = 1
charge_step = 2
charge_amount = 0
charge_change = (charge_mod - charge_amount//charge_step, charge_mod - charge_amount//charge_step)

guard_mod = 2
guard_step = 3
guard_amount = 0
guard_change = (guard_mod - guard_amount//guard_step, 0)

breakthrough_mod = 1
breakthrough_step = 5
breakthrough_amount = 0
breakthrough_change = (breakthrough_mod - breakthrough_amount//breakthrough_step, 0)

# curve  
# manacost: (desired_amount - actual_amount, desired_amount]
cm = 1.5
curve = {0:[2*cm,2*cm], 1:[5*cm,5*cm], 2:[8*cm,8*cm], 3:[5*cm,5*cm], 4:[4*cm,4*cm], 5:[3*cm,3*cm], 6:[2*cm,2*cm], 7:[2*cm,2*cm], 8:[1*cm,1*cm]}

# id: [rating, aggro, control]
cardratings = {"1": [5.0, 0.0, 0.0], "2": [4.0, 1.0, 0.0], "3": [8.0, 1.0, 1.0], "4": [6.0, 0.0, 1.0], "5": [5.0, 1.0, 0.0], "6": [5.0, 0.0, 0.0], \
"7": [7.0, 1.0, 0.0], "8": [5.0, 0.0, 0.0], "9": [7.0, 0.0, 0.0], "10": [4.0, 0.0, 1.0], "11": [5.5, 1.0, 0.0], "12": [6.5, 0.0, 1.0], "13": [5.0, 0.0, 0.0], \
"14": [4.0, 1.0, 0.0], "15": [6.0, 0.0, 0.0], "16": [3.0, 0.0, 0.0], "17": [6.0, 0.0, 0.0], "18": [8.0, 1.0, 0.0], "19": [6.0, 0.0, 0.0], "20": [3.0, 0.0, 0.0], \
"21": [5.5, 0.0, 0.0], "22": [2.0, 0.0, 0.0], "23": [4.0, 0.0, 0.0], "24": [1.0, 0.0, -1.0], "25": [4.0, 1.0, -1.0], "26": [6.0, 1.0, 0.0], "27": [5.0, 0.0, 1.0], \
"28": [6.0, 1.0, 1.0], "29": [7.0, 1.0, 1.0], "30": [6.0, 1.0, 0.0], "31": [3.0, 0.0, -1.0], "32": [7.0, 0.0, 0.0], "33": [7.0, 0.0, 1.0], "34": [6.0, 0.0, 0.0], \
"35": [1.0, 0.0, 0.0], "36": [6.0, -1.0, 0.0], "37": [9.0, 0.0, 1.0], "38": [8.5, 1.0, 1.0], "39": [7.0, 0.0, 1.0], "40": [6.0, 0.0, 1.0], "41": [6.0, 0.0, 1.0], \
"42": [4.0, 0.0, 0.0], "43": [4.0, 0.0, 1.0], "44": [6.0, 0.0, 1.0], "45": [6.0, 0.0, 0.0], "46": [4.0, 0.0, 0.0], "47": [7.0, 0.0, 1.0], "48": [9.0, 0.0, 1.0], \
"49": [8.0, 0.0, 1.0], "50": [5.0, 0.0, 0.0], "51": [7.0, 0.0, 1.0], "52": [6.0, 0.0, 0.0], "53": [8.0, 0.0, 1.0], "54": [4.5, 0.0, 0.0], "55": [3.0, -1.0, 0.0], \
"56": [6.0, -1.0, 1.0], "57": [3.0, -1.0, 0.0], "58": [2.0, 0.0, 0.0], "59": [4.0, 0.0, 0.0], "60": [1.0, 0.0, 0.0], "61": [3.0, 0.0, 0.0], "62": [2.0, -1.0, 1.0], \
"63": [5.0, 0.0, 1.0], "64": [5.0, 0.0, 1.0], "65": [7.0, 1.0, 0.0], "66": [5.5, 0.0, 0.0], "67": [5.5, 0.0, 0.0], "68": [7.0, 0.0, 0.0], "69": [10.0, 1.0, 0.0], \
"70": [7.0, 1.0, 0.0], "71": [3.0, 0.0, 0.0], "72": [5.0, 0.0, 0.0], "73": [8.0, 0.0, 1.0], "74": [4.0, 0.0, 0.0], "75": [8.0, 1.0, 0.0], "76": [6.5, 0.0, 0.0], \
"77": [5.0, 0.0, 0.0], "78": [7.5, 1.0, 0.0], "79": [6.0, 0.0, 0.0], "80": [9.0, 0.0, 1.0], "81": [8.0, 1.0, 0.0], "82": [8.0, 0.0, 1.0], "83": [5.0, 0.0, 0.0], \
"84": [7.0, 0.0, 1.0], "85": [5.0, 0.0, 0.0], "86": [4.0, 0.0, 0.0], "87": [5.0, 0.0, 0.0], "88": [6.0, 0.0, 0.0], "89": [3.0, 0.0, 0.0], "90": [5.0, 1.0, 0.0], \
"91": [9.0, 1.0, 1.0], "92": [3.0, -1.0, 0.0], "93": [7.0, 0.0, 0.0], "94": [7.0, 0.0, 1.0], "95": [8.0, 1.0, 0.0], "96": [8.0, 1.0, 0.0], "97": [6.0, 0.0, 1.0], \
"98": [7.0, 0.0, 1.0], "99": [10.0, 1.0, 1.0], "100": [7.0, 0.0, 1.0], "101": [4.0, 0.0, 0.0], "102": [3.0, 0.0, 0.0], "103": [7.0, 0.0, 1.0], "104": [5.5, 0.0, 0.0], \
"105": [6.5, 0.0, 1.0], "106": [6.0, 0.0, 0.0], "107": [3.0, 0.0, 1.0], "108": [4.0, 0.0, 1.0], "109": [6.0, 0.0, 0.0], "110": [3.0, 0.0, 0.0], "111": [5.5, 0.0, 1.0], \
"112": [4.0, 0.0, 1.0], "113": [2.0, 0.0, 1.0], "114": [7.0, 0.0, 1.0], "115": [5.0, 0.0, 0.0], "116": [7.0, -1.0, 1.0], "117": [6.5, 1.0, 0.0], "118": [7.5, 1.0, 0.0], \
"119": [6.0, 0.0, 0.0], "120": [6.0, 0.0, 1.0], "121": [4.0, -1.0, 0.0], "122": [7.0, 0.0, 1.0], "123": [6.0, 0.0, -1.0], "124": [5.0, 0.0, 1.0], "125": [3.0, 0.0, 0.0], \
"126": [4.0, 0.0, 0.0], "127": [4.0, 0.0, 0.0], "128": [6.0, 1.0, 0.0], "129": [5.0, 0.0, 0.0], "130": [4.0, 0.0, 1.0], "131": [3.0, 0.0, 0.0], "132": [3.0, 1.0, 0.0], \
"133": [5.0, 0.0, 0.0], "134": [4.5, 0.0, 0.0], "135": [6.0, 1.0, 0.0], "136": [7.0, 0.0, 0.0], "137": [4.0, 0.0, 0.0], "138": [3.0, 0.0, 0.0], "139": [5.0, 0.0, 0.0], \
"140": [2.0, 1.0, 0.0], "141": [5.0, 0.0, 1.0], "142": [8.0, 1.0, 0.0], "143": [3.0, 1.0, -1.0], "144": [7.0, 0.0, 1.0], "145": [1.0, -1.0, 0.0], "146": [1.0, 0.0, 0.0], \
"147": [4.0, 0.0, 0.0], "148": [5.0, 0.0, 1.0], "149": [2.0, 0.0, 0.0], "150": [5.0, 0.0, 0.0], "151": [6.0, 0.0, 1.0], "152": [3.0, -1.0, 1.0], "153": [4.0, 0.0, 1.0], \
"154": [3.0, 0.0, 0.0], "155": [6.0, 0.0, 1.0], "156": [4.0, 1.0, 0.0], "157": [3.0, 0.0, 1.0], "158": [8.0, 0.0, 1.0], "159": [6.0, 0.0, 1.0], "160": [2.0, 1.0, 0.0]}

all_spell_counter = 0
blue_spell_counter = 0

max_spells = 10
max_blue_spells = 10

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def knapSack(W, wt, val, n):
    cs = []
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
             
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    # stores the result of Knapsack
    res = K[n][W]
    
     
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break

        if res == K[i - 1][w]:
            continue
        else:
 
            # This item is included.
            cs.append(i - 1)


            res = res - val[i - 1]
            w = w - wt[i - 1]
    
    return (cs, res)


def knapSack2(card_damages, card_costs, card_spaces, board_space, mana, atleast_one_charge = False, abilities = []):
    n = len(card_damages)

    # generate all combinations of cards
    all_combinations = []
    for i in range(1, n + 1):
        all_combinations.extend(list(itertools.combinations(range(n), i)))
        
    max_damage = 0
    best_combination = []
    print(str(len(all_combinations)), file=sys.stderr, flush=True)
    for ac in all_combinations:
        if atleast_one_charge:
            charge = False
            for i in ac:
                if 'C' in abilities[i]:
                    charge = True
                    break
            if not charge:
                continue
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
    print(str((max_damage, best_combination)), file=sys.stderr, flush=True)
    return (max_damage, best_combination)









def evaluateDraft(eval_card, turncount):
    """
    if eval_card[3] != 0:
        return -19
    keywords = eval_card[7]
    eval_attack, eval_defense = eval_card[5], eval_card[6]

    # breakthrough
    if 'B' in keywords:
        eval_attack += breakthrough_change[0]
        eval_defense += breakthrough_change[1]

    # guard/taunt
    if 'G' in keywords:
        eval_attack += guard_change[0]
        eval_defense += guard_change[1]

    # charge
    if 'C' in keywords:
        eval_attack += guard_change[0]
        eval_defense += guard_change[1]
    
    card_value = eval_attack * eval_defense
    if eval_card[4] == 0:
        card_value = card_value/1
    elif eval_card[4] == 1:
        card_value = card_value/4
    else:
        card_value = card_value/(eval_card[4]*(eval_card[4]+1))
    """
    card_value = cardratings[str(eval_card[0])][0]

    if eval_card[3] != 0:
        if all_spell_counter >= max_spells:
            card_value *= 0.5
        if eval_card[3] == 3:
            card_value *= 1.5
            """
            if blue_spell_counter >= max_blue_spells:
                card_value *= 0.5
            """
    
    if turncount <= 10: 
        return card_value
    else:
        eval_mana_cost = eval_card[4]

        curve_mod = 0
        needed_amount, desired_amount = 0, 0
        if eval_mana_cost < 8:
            needed_amount, desired_amount = curve[eval_mana_cost][0], curve[eval_mana_cost][1]
        else: 
            needed_amount, desired_amount = curve[8][0], curve[8][1]
        
        if (needed_amount*(1/cm)) / (desired_amount*(1/cm)) > 0.5:
            curve_mod = 1
        else:
            curve_mod = needed_amount / desired_amount

    return curve_mod * card_value




def lethalDetector(p_board, o_board, p_hand, p_mana, o_hp, action):
    # check if direct damage is lethal
    p_hand_copy = [card for card in p_hand.copy() if card[9] < 0 or (card[3] == 3 and card[5] < 0) ]
    card_damages = [(-card[9]) -card[6] if card[3] == 3 else -card[9] for card in p_hand_copy]
    card_costs = [card[4] for card in p_hand_copy]
    card_spaces = [1 if card[3] == 0 else 0 for card in p_hand_copy]
    board_space = 6 - len(p_board)
    mana = p_mana
    assert len(card_damages) == len(card_costs) == len(card_spaces) 
    maxDamage, cards_to_play = knapSack2(card_damages, card_costs, card_spaces, board_space, mana)
    if maxDamage >= o_hp:
        for card in cards_to_play:
            if hand_cards[card][3] == 0:
                action += "SUMMON " + str(p_hand_copy[card][1]) + "; "
            else:
                action += "USE " + str(p_hand_copy[card][1]) + " -1" + "; "

        return action

    # check if guard on board of opponent

    o_board_taunts = [card for card in o_board if 'G' in card[7]]
    if len(o_board_taunts) == 0: # no guard minions
        # check if we have a minion that can attack
        if len(p_board) > 0:
            # we have minions on board and there are no guard minion
            # check if we have a charge minion in hand
            p_hand_charge = [card for card in p_hand if 'C' in card[7]]
            if len(p_hand_charge) > 0:
                # we have a charge minion in hand
                # take all green spells that can buff a minion
                p_hand_green_spells = [card for card in p_hand.copy() if (card[3] == 1 and card[5] > 0)]
                # add all charge minions and 
                p_hand_copy =  p_hand_green_spells + p_hand_charge + p_hand_copy
                # attack buffs from all 
                card_damages_green_spells = [card[5] for card in p_hand_green_spells]
                card_damage_charge = [card[5] for card in p_hand_charge]
                # add all damages together
                card_damages = card_damages_green_spells + card_damage_charge + card_damages
                # all costs
                card_costs = [card[4] for card in p_hand_copy]
                card_spaces = [1 if card[3] == 0 else 0 for card in p_hand_copy]
                assert len(card_damages) == len(card_costs) == len(card_spaces) 
                maxDamage, ids_to_play = knapSack2(card_damages, card_costs, card_spaces, board_space, mana)
                maxDamage_board_minions = sum(card[5] for card in p_board)
                # check if lethal
                if maxDamage+maxDamage_board_minions >= o_hp:
                    cards_to_play = [hand_cards[i] for i in ids_to_play]
                    # 1. play charge minion(s)
                    # save the biggest charge minion for the buffs
                    biggest_charge = None
                    for card in cards_to_play:
                        if 'C' in card[7]:
                            # save the biggest charge minion
                            if biggest_charge is None:
                                biggest_charge = card
                            elif card[5] > biggest_charge[5]:
                                biggest_charge = card
                            # play minion
                            action += "SUMMON " + str(card[1]) + "; "
                    # 2. play green spells
                    for card in cards_to_play:
                        if card[3] == 1:
                            action += "USE " + str(card[1]) + " " + str(biggest_charge[1]) + "; "
                    # 3. attack with charge minions opponent face and use blue spells
                    for card in cards_to_play:
                        if 'C' in card[7]:
                            action += "ATTACK " + str(card[1]) + " -1;"
                        elif card[3] == 3:
                            action += "USE " + str(card[1]) + " -1;"
                        elif card[3] == 0 and 'C' not in card[7]: # summon all other minion
                            action += "SUMMON " + str(card[1]) + "; "
                    # 4. attack with board minions
                    for card in p_board:
                        action += "ATTACK " + str(card[1]) + " -1;"

                # return action
                return action
            else:
                # we dont have a charge minion in hand
                # we have minions on board
                # take all green spells that can buff a minion
                p_hand_green_spells = [card for card in p_hand.copy() if (card[3] == 1 and card[5] > 0)]
                # add all blue spells that can target enemy face
                p_hand_copy =  p_hand_green_spells + p_hand_copy
                # attack buffs from all 
                card_damages_green_spells = [card[5] for card in p_hand_green_spells]
                # add all damages together
                card_damages = card_damages_green_spells + card_damages
                # all costs
                card_costs = [card[4] for card in p_hand_copy]
                card_spaces = [1 if card[3] == 0 else 0 for card in p_hand_copy]
                assert len(card_damages) == len(card_costs) == len(card_spaces) 
                maxDamage, ids_to_play = knapSack2(card_damages, card_costs, card_spaces, board_space, mana)
                maxDamage_board_minions = sum(card[5] for card in p_board)
                # check if lethal
                if maxDamage+maxDamage_board_minions >= o_hp:
                    cards_to_play = [hand_cards[i] for i in ids_to_play]
                    # 1. play green spells on first minion on board and use blue spells on face
                    for card in cards_to_play:
                        if card[3] == 1:
                            action += "USE " + str(card[1]) + " " + str(p_board[0][1]) + "; "
                        elif card[3] == 3:
                            action += "USE " + str(card[1]) + " -1;"
                        elif card[3] == 0:
                            action += "SUMMON " + str(card[1]) + "; " # summon all other minion
                    # 2. attack with board minions
                    for card in p_board:
                        action += "ATTACK " + str(card[1]) + " -1;"

                # return action
                return action
        else:
            # we dont have minons on board and there are no guard minions
            # check if we have a charge minion in hand
            p_hand_charge = [card for card in p_hand if 'C' in card[7]]
            if len(p_hand_charge) > 0:
                # we have a charge minion in hand
                # take all green spells that can buff a minion
                p_hand_green_spells = [card for card in p_hand.copy() if (card[3] == 1 and card[5] > 0)]
                # add all charge minions and 
                p_hand_copy =  p_hand_green_spells + p_hand_charge + p_hand_copy
                # attack buffs from all 
                card_damages_green_spells = [card[5] for card in p_hand_green_spells]
                card_damage_charge = [card[5] for card in p_hand_charge]
                # add all damages together
                card_damages = card_damages_green_spells + card_damage_charge + card_damages
                # all costs
                card_costs = [card[4] for card in p_hand_copy]
                card_spaces = [1 if card[3] == 0 else 0 for card in p_hand_copy]
                assert len(card_damages) == len(card_costs) == len(card_spaces) 
                # TODO: atleast one charge minion on board
                maxDamage, ids_to_play = knapSack2(card_damages, card_costs, card_spaces, board_space, mana, atleast_one_charge=True, abilities = [card[7] for card in p_hand_copy])

                # check if lethal
                if maxDamage >= o_hp:
                    cards_to_play = [hand_cards[i] for i in ids_to_play]
                    # 1. play charge minion(s)
                    # save the biggest charge minion for the buffs
                    biggest_charge = None
                    for card in cards_to_play:
                        if 'C' in card[7]:
                            # save the biggest charge minion
                            if biggest_charge is None:
                                biggest_charge = card
                            elif card[5] > biggest_charge[5]:
                                biggest_charge = card
                            # play minion
                            action += "SUMMON " + str(card[1]) + "; "
                    # 2. play green spells
                    for card in cards_to_play:
                        if card[3] == 1:
                            action += "USE " + str(card[1]) + " " + str(biggest_charge[1]) + "; "
                    # 3. attack with charge minions opponent face and use blue spells and summon summon damage minions
                    for card in cards_to_play:
                        if 'C' in card[7]:
                            action += "ATTACK " + str(card[1]) + " -1;"
                        elif card[3] == 3:
                            action += "USE " + str(card[1]) + " -1;"
                        elif card[3] == 0 and 'C' not in card[7]: # summon all other minion
                            action += "SUMMON " + str(card[1]) + "; "

                # return action
                return action


            else:
                # we dont have a charge minion in hand
                return action
    else:
        # enemy has a guard minion on board
        # 1. check if breakthrough minion is available
        
        # 1.2 check if we have a breakthrough minion on board
        p_board_breakthrough = [card for card in p_board if 'B' in card[7]]
        if len(p_board_breakthrough) > 0:
            # we have atleast one breakthrough minion on board
            # check if we only have one breakthough minion on board
            if len(p_board_breakthrough) == 1:
                # we have only one breakthrough minion on board
                # 1. if we dont have damage buffing green spells attack lowest hp taunt of enemy, call lethal again
                p_hand_green_spells = [card for card in p_hand.copy() if (card[3] == 1 and card[5] > 0)]
                if len(p_hand_green_spells) == 0:
                    # we dont have any green spells
                    # attack lowest hp taunt of enemy
                    # get lowest hp taunt of enemy
                    lowest_hp_taunt = min(o_board, key=lambda x: x[6])
                    # check if we have more attack than the taunt has defense
                    if p_board[5] > lowest_hp_taunt[6]:
                        # we have more attack than the taunt has defense
                        # attack lowest hp taunt of enemy
                        action += "ATTACK " + str(p_board[1]) + " " + str(lowest_hp_taunt[1]) + "; "
                        # remove taunt from opponent board
                        o_board.remove(lowest_hp_taunt)
                        # check if our breakthrough minion died
                        if p_board[6] <= lowest_hp_taunt[5]:
                            o_hp = o_hp - (p_board[6] - lowest_hp_taunt[5])
                            # our breakthrough minion died
                            # remove it from board
                            p_board.remove(p_board[0])
                        # recursion call
                        return action + lethalDetector(p_board, o_board, p_hand, p_mana, o_hp , action)
                else:
                    # we have green spells
                    # check if we have blue spells or summon damaging minions
                    if len(p_hand_copy) == 0:
                        # we dont have any blue spells or summon minions
                        # buff breakthrough minion with green spells
                        # list of green spells that can buff a breakthrough minion
                        
                    # 1. try to buff breakthrough minion with green spells
                    #
                        


            else:
                # we have more than one breakthrough minion on board
                pass
        # 1.1 check if we have a breakthough charge minion in hand
        p_hand_breakthrough = [card for card in p_hand if 'B' in card[7] and 'C' in card[7]]
        if len(p_hand_breakthrough) > 0:
            pass
        # 2. if no breakthrough minion available check if its possible to kill the guard with spells

        











# game loop
while True:
    start = time.perf_counter()
    player_stats = []
    for i in range(2):
        player_health, player_mana, player_deck, player_rune, player_draw = [int(j) for j in input().split()]
        player_stats.append([player_health, player_mana, player_deck, player_rune, player_draw])

    opponent_hand, opponent_actions = [int(i) for i in input().split()]
    for i in range(opponent_actions):
        card_number_and_action = input()
    card_count = int(input())

    hand_cards = []
    opponent_board = []
    player_board = []

    for i in range(card_count):
        inputs = input().split()
        card_number = int(inputs[0])
        instance_id = int(inputs[1])
        location = int(inputs[2])
        card_type = int(inputs[3])
        cost = int(inputs[4])
        attack = int(inputs[5])
        defense = int(inputs[6])
        abilities = inputs[7]
        my_health_change = int(inputs[8])
        opponent_health_change = int(inputs[9])
        card_draw = int(inputs[10])

        if location == 0:
            hand_cards.append([card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw])
        elif location == 1:
            player_board.append([card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw])
        elif location == -1:
            opponent_board.append([card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw])

    if player_stats[0][1] == 0:
        # --------------------- DRAFT ---------------------


        ratings = [evaluateDraft(card, player_stats[0][2]) for card in hand_cards]
        
        # get all indices with the highest ratings
        max_indices = [i for i, x in enumerate(ratings) if x == max(ratings)]

        tmp_pick = None
        if len(max_indices) > 1:
            for i in max_indices:
                if hand_cards[i][3] == 0:
                    tmp_pick = i
                    break
        if tmp_pick is not None:
            card_i = tmp_pick
        else:
            card_i = max_indices[0]        



        picked_card = hand_cards[card_i]

        if picked_card[3] != 0:
            if picked_card[3] == 3:
                blue_spell_counter += 1
            all_spell_counter += 1

        if picked_card[4] >= 8:
            curve[8][0] -= 1
        else:
            curve[picked_card[4]][0] -= 1
        
        print("PICK " + str(card_i))






    else:
        playerAction = ""
        # ----------- CHECK FOR LETHAL ------------
        hand_copy = [h for h in hand_cards.copy() if h[4] <= player_stats[0][1]]
        # removve all non charge minions, questionable maybe removelater


        lethal_action = lethalDetector(player_board.copy(), opponent_board.copy(),hand_copy, player_stats[0][1], player_stats[1][0], playerAction)
        if lethal_action != "":
            print(lethal_action[:-1])
            continue
        
        # --------------- ATTACK ------------------
        attacked = []
        deleted = []
        for card in opponent_board:
            if card in deleted:
                continue
            if 'G' in card[7]:
                defense = card[6]
                for c in player_board:
                    if c in attacked:
                        continue
                    if c[5] == defense:
                        playerAction += "ATTACK " + str(c[1]) + " " + str(card[1]) + ";"
                        attacked.append(c)
                        deleted.append(card)
                        break
        for card in opponent_board:
            if card in deleted:
                continue
            if 'G' in card[7]:
                defense = card[6]
                for c in player_board:
                    if c in attacked:
                        continue
                    if c[5] >= defense:
                        playerAction += "ATTACK " + str(c[1]) + " " + str(card[1]) + ";"
                        attacked.append(c)
                        deleted.append(card)
                        break 
        for card in opponent_board:
            if card in deleted:
                continue
            if 'G' in card[7]:
                defense = card[6]
                for c in player_board:
                    if c in attacked:
                        continue
                    if c[5] <= defense:
                        playerAction += "ATTACK " + str(c[1]) + " " + str(card[1]) + ";"
                        attacked.append(c)
                        deleted.append(card)
                        break 

        for card in player_board:
            if card not in attacked:
                playerAction += "ATTACK " + str(card[1]) + " -1" + ";"






        # --------------- SUMMON ------------------

        # To test above function
        val = [card[5] * card[6] for card in hand_cards]
        wt = [card[4] for card in hand_cards]
        W = player_stats[0][1]
        n = len(val)
        cards_to_play = knapSack(W, wt, val, n)[0]

        
        for cardIndex in cards_to_play:
            playerAction += "SUMMON " + str(hand_cards[cardIndex][1]) + ";"
        





        # --------------- END TURN ------------------
        if playerAction == "":
            print("PASS")
        else:
            print(playerAction[:-1])

        