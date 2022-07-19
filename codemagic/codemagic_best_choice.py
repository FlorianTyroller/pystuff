import sys
import math
import time
import itertools
import copy

card_number = 'card_number'
instance_id = 'instance_id'
card_type = 'card_type'
cost = 'cost'
attack = 'attack'
defense = 'defense'
abilities = 'abilities'
my_health_change = 'my_health_change'
opponent_health_change = 'opponent_health_change'
card_draw = 'card_draw'
can_attack = 'can_attack'
has_attacked = 'has_attacked'

# kws
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
    # print(str(len(all_combinations)), file=sys.stderr, flush=True)
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
    # print(str((max_damage, best_combination)), file=sys.stderr, flush=True)
    return (max_damage, best_combination)


def hash_function(a):
    # convert to string and return hash of string
    return hash(str(a))


def evaluateDraft(eval_card, turncount):
    card_value = cardratings[str(eval_card[card_number])][0]

    if eval_card[card_type] != 0:
        if all_spell_counter >= max_spells:
            card_value *= 0.5
        if eval_card[card_type] == 3:
            card_value *= 1.5
            """
            if blue_spell_counter >= max_blue_spells:
                card_value *= 0.5
            """
    
    if turncount <= 10: 
        return card_value
    else:
        eval_mana_cost = eval_card[cost]

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


def moveToString(moves):
    st = ""
    for move in moves:
        try:
            if len(move) == 3:
                if move[2] == -1:
                    st += move[0] + " " + str(move[1][instance_id]) + " -1;"
                else:
                    st += move[0] + " " + str(move[1][instance_id]) + " " + str(move[2][instance_id]) + ";" 
            elif len(move) == 2:
                st += move[0] + " " + str(move[1][instance_id]) + ";"
            else:
                print("invalid move length: " + str(move), file=sys.stderr, flush=True)
        except:
            print("invalid move: " + str(move), file=sys.stderr, flush=True)
            print("-----")
    return st


def getStateRating(board_state): # TODO add draw
    player_board, opponent_board, hand_cards, player_health, player_mana, opponent_health = board_state
    if player_health <= 0:
        return -99999999
    if opponent_health <= 0:
        return 9999999999
    guard_bonus = 2
    state_rating = 0
    guard_defense = 0
    for card in player_board:
        if "G" in card[abilities]:
            state_rating += card[defense] * guard_bonus
            guard_defense += card[defense]
        else: 
            state_rating += card[defense]
        if card[abilities].count("-") < 6:
            state_rating += 3
        state_rating += card[attack]
    opponent_attack = 0
    for card in opponent_board:
        if "G" in card[abilities]:
            state_rating -= card[defense] * guard_bonus
        else:
            state_rating -= card[defense]
        if card[abilities].count("-") < 6:
            state_rating -= 3
        opponent_attack += card[attack]

    if opponent_attack > guard_defense:
        state_rating -= 10
    else:
        state_rating -= opponent_attack
    
    state_rating -= opponent_health
    state_rating += player_health

    return state_rating


def generateAllMoves(board_state):
    dupe_count = 0
    all_moves = getAllMoves(board_state)
    all_unique_moves_and_ratings = []
    all_unique_hashes = []
    """
    moves_to_do = [[latest_move, [latest_move], (state := getStateFromMove(latest_move, board_state)), getStateRating(state)] for latest_move in all_moves]
    """
    moves_to_do = []
    for latest_move in all_moves:
        state = getStateFromMove(latest_move, board_state)
        state_rating = getStateRating(state)
        moves_to_do.append([latest_move, [latest_move], state, state_rating])

    while len(moves_to_do) > 0:
        # print(str(moves_to_do[0]), file=sys.stderr, flush=True)
        latest_move, all_moves, state, rating = moves_to_do.pop(0)
        if rating > 90000:
            return [(all_moves, rating)]
        if rating < -90000:
            continue

        # sort playerboard by instance id
        sortet_board = sorted(state[0], key=lambda x: x[instance_id])
        ha = hash_function([sortet_board, state[1], state[2], state[3], state[4], state[5]])
        if ha in all_unique_hashes:
            # print("duplicated move", file=sys.stderr, flush=True)
            dupe_count += 1
            continue
        all_unique_hashes.append(ha)


        all_unique_moves_and_ratings.append((all_moves,rating))
        """
        moves_to_do.extend([(move, all_moves + [move], (new_state := getStateFromMove(move, state)), getStateRating(new_state)) for move in getAllMoves(state)])
        """
        maxRating = -9999999999999
        max_new_move = None
        for move in getAllMoves(state):
            new_all_moves = all_moves + [move]
            new_state = getStateFromMove(move, state)
            new_rating = getStateRating(new_state)
            if new_rating > maxRating:
                maxRating = new_rating
                max_new_move = [move, new_all_moves, new_state, new_rating]
        if max_new_move is not None:
            moves_to_do.append(max_new_move)

    print("duped moves: " + str(dupe_count), file=sys.stderr, flush=True)
    print("move count: " + str(len(all_unique_hashes)), file=sys.stderr, flush=True)
    return all_unique_moves_and_ratings


def getStateFromMove(move, board_state):
    player_board, opponent_board, hand_cards, player_health, player_mana, opponent_health = board_state
    if move[0] == 'ATTACK':
        # check if opponent is face or minion
        if move[2] == -1: # face
            # change face hp
            opponent_health -= move[1][attack]

            # change can attack to false
            player_board_copy = copy.deepcopy(player_board)
            player_board_copy[player_board.index(move[1])][can_attack] = False
            player_board_copy[player_board.index(move[1])][has_attacked] = True
            return (player_board_copy, opponent_board, hand_cards, player_health, player_mana, opponent_health)
        else: # minion
            player_board_copy = copy.deepcopy(player_board)
            opponent_board_copy = copy.deepcopy(opponent_board)
            # enemy minion checks
            # check if it has ward
            target_i = opponent_board.index(move[2])
            target_copy = opponent_board_copy[target_i]
            source_i = player_board.index(move[1])
            source_copy = player_board_copy[source_i]
            target_damage = 0
            source_damage = 0
            source_copy[has_attacked] = True
            source_copy[can_attack] = False
            # ward
            if 'W' in move[2][abilities]:
                target_copy[abilities].replace('W', '-')
                target_damage = 0 # damage the target takes
            else:
                target_damage = source_copy[attack]
            
            if 'W' in move[1][abilities]:
                target_copy[abilities].replace('W', '-')
                source_damage = 0 # damage the source takes
            else:
                source_damage = target_copy[attack]
            
            # Drain
            if 'D' in move[2][abilities]:
                opponent_health += source_damage
            if 'D' in move[1][abilities]:
                player_health += target_damage

            # breakthrough
            if 'B' in move[1][abilities]:
                if target_damage > target_copy[defense]:
                    opponent_health -= target_damage - target_copy[defense]
            
            # lethal
            if 'L' in move[1][abilities]:
                target_damage *= 99
            if 'L' in move[2][abilities]:
                source_damage *= 99

            target_copy[defense] -= target_damage
            source_copy[defense] -= source_damage
            # check if dead
            if target_copy[defense] <= 0:
                opponent_board_copy.pop(target_i)
            if source_copy[defense] <= 0:
                player_board_copy.pop(source_i)
            return (player_board_copy, opponent_board_copy, hand_cards, player_health, player_mana, opponent_health)

    elif move[0] == 'USE':
        player_hand_copy = copy.deepcopy(hand_cards)
        # remove card in player hand copy where the instance_id == move[1][instance_id]
        rem = False
        for i,c in enumerate(player_hand_copy):
            if c[instance_id] == move[1][instance_id]:
                player_hand_copy.pop(i)
                rem = True
                break
        if rem == False:
            print("this move doesnt work l:363" + str(move), file=sys.stderr, flush=True)
            print("error: card not in hand", file=sys.stderr, flush=True)

        # check if opponent is face or minion
        if move[2] == -1:
            # check what type of spell it is
            if move[1][card_type] != 3:
                print("this move tried to attack face: " + str(move), file=sys.stderr, flush=True)
                assert False
            # change face hp
            opponent_health += move[1][defense]
            opponent_health += move[1][opponent_health_change]
            player_health += move[1][my_health_change]

            #change player mana
            player_mana -= move[1][cost]
            return (player_board, opponent_board, player_hand_copy, player_health, player_mana, opponent_health)
        else:
            # check what type of spell it is
            if move[1][card_type] == 1: # green spell
                player_board_copy = copy.deepcopy(player_board)
                target_i = player_board.index(move[2])
                target_copy = player_board_copy[target_i]
                player_health += move[1][my_health_change]
                target_copy[attack] += move[1][attack]
                target_copy[defense] += move[1][defense]
                for a in move[1][abilities]:
                    if a == 'C' and a not in target_copy[abilities]:
                        if target_copy[has_attacked] == False:
                            target_copy[can_attack] = True
                        target_copy[abilities] += a
                    elif a not in target_copy[abilities]:
                        target_copy[abilities] += a
                player_mana -= move[1][cost]
                return (player_board_copy, opponent_board, player_hand_copy, player_health, player_mana, opponent_health)
            elif move[1][card_type] == 2: # red spell
                opponent_board_copy = copy.deepcopy(opponent_board)
                target_i = opponent_board_copy.index(move[2])
                target_copy = opponent_board_copy[target_i]

                opponent_health += move[1][opponent_health_change]
                target_copy[defense] += move[1][defense]
                target_copy[attack] += move[1][attack]
                # check if target has negative attack
                if target_copy[attack] < 0:
                    target_copy[attack] = 0
                # remove all abilities from target that are also in the abilities of the spell
                for a in move[1][abilities]:
                    if a in target_copy[abilities]:
                        target_copy[abilities].replace(a, '-')
                # check if target is dead
                if target_copy[defense] <= 0:
                    opponent_board_copy.pop(target_i)
                player_mana -= move[1][cost]
                return (player_board, opponent_board_copy, player_hand_copy, player_health, player_mana, opponent_health)
            elif move[1][card_type] == 3: # blue spell # TODO check if targeted own minions
                opponent_board_copy = copy.deepcopy(opponent_board)
                target_i = opponent_board.index(move[2])
                target_copy = opponent_board_copy[target_i]
                target_copy[defense] += move[1][defense]

                opponent_health += move[1][opponent_health_change]
                player_health += move[1][my_health_change]

                # check if target is dead
                if target_copy[defense] <= 0:
                    opponent_board_copy.pop(target_i)
                player_mana -= move[1][cost]
                return (player_board, opponent_board_copy, player_hand_copy, player_health, player_mana, opponent_health)
    elif move[0] == 'SUMMON':
        player_board_copy = copy.deepcopy(player_board)
        player_hand_copy = copy.deepcopy(hand_cards)
        player_hand_copy.pop(hand_cards.index(move[1]))
        # add minion to board
        move[1][has_attacked] = False
        if 'C' in move[1][abilities]:
            move[1][can_attack] = True
        else:
            move[1][can_attack] = False
        player_board_copy.append(move[1])
        # change player mana
        player_mana -= move[1][cost]


        # change player hp and opponent hp
        player_health += move[1][my_health_change]
        opponent_health += move[1][opponent_health_change]
        return (player_board_copy, opponent_board, player_hand_copy, player_health, player_mana, opponent_health)


def getAllMoves(board_state):
    player_board, opponent_board, hand_cards, player_health, player_mana, opponent_health = board_state
    moves = []
    # TODO: also append resulting board state
    # attacks
    for card in player_board:
        # check if it has attack / TODO check if it can attack
        if card[attack] > 0 and card[can_attack] == True and card[has_attacked] == False:
            # check if opponent has guard minions on on board
            o_board_taunts = [card for card in opponent_board if 'G' in card[abilities]]
            if len(o_board_taunts) > 0:
                for taunt_card in o_board_taunts:
                    move = ("ATTACK", card, taunt_card)
                    moves.append(move)

            else:
                for opponent_card in opponent_board:
                    move = ("ATTACK", card, opponent_card)
                    moves.append(move)
                # face attack
                move = ("ATTACK", card, -1)
                moves.append(move)

    # spells and summons
    for card in hand_cards:
        # check if enough mana to play the card
        if player_mana >= card[cost]:
            if card[card_type] == 0: # monster
                # check for board space
                if len(player_board) < 6:
                    move = ("SUMMON", card)
                    moves.append(move)
            elif card[card_type] == 1: # green item
                for board_card in player_board:
                    move = ("USE", card, board_card)
                    moves.append(move)
            elif card[card_type] == 2: # red item
                for board_card in opponent_board:
                    move = ("USE", card, board_card)
                    moves.append(move)
            elif card[card_type] == 3: # blue item # TODO: make it able to target own minions aswell
                # if the defense of the card is not 0 it can be targetet to face or a creature, can also target own creatures
                if card[defense] < 0:
                    for board_card in opponent_board:
                        move = ("USE", card, board_card)
                        moves.append(move)
                move = ("USE", card, -1)
                moves.append(move)

    return moves






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
        card_number2 = int(inputs[0])
        instance_id2 = int(inputs[1])
        location2 = int(inputs[2])
        card_type2 = int(inputs[3])
        cost2 = int(inputs[4])
        attack2 = int(inputs[5])
        defense2 = int(inputs[6])
        abilities2 = inputs[7]
        my_health_change2 = int(inputs[8])
        opponent_health_change2 = int(inputs[9])
        card_draw2 = int(inputs[10])
        # can attack is ind 11

        if location2 == 0: # hand cards can normally not attack
            hand_cards.append({'card_number': card_number2, 'instance_id': instance_id2, 'card_type': card_type2, 'cost': cost2, 'attack': attack2, 'defense': defense2, 'abilities': abilities2, 'my_health_change': my_health_change2, 'opponent_health_change': opponent_health_change2, 'card_draw': card_draw2, 'can_attack': False, 'has_attacked': False})
        elif location2 == 1:
            player_board.append({'card_number': card_number2, 'instance_id': instance_id2, 'card_type': card_type2, 'cost': cost2, 'attack': attack2, 'defense': defense2, 'abilities': abilities2, 'my_health_change': my_health_change2, 'opponent_health_change': opponent_health_change2, 'card_draw': card_draw2, 'can_attack': True, 'has_attacked': False})
        elif location2 == -1:
            opponent_board.append({'card_number': card_number2, 'instance_id': instance_id2, 'card_type': card_type2, 'cost': cost2, 'attack': attack2, 'defense': defense2, 'abilities': abilities2, 'my_health_change': my_health_change2, 'opponent_health_change': opponent_health_change2, 'card_draw': card_draw, 'can_attack': False, 'has_attacked': False})

    if player_stats[0][1] == 0:
        # --------------------- DRAFT ---------------------


        ratings = [evaluateDraft(card, player_stats[0][2]) for card in hand_cards]
        
        # get all indices with the highest ratings
        max_indices = [i for i, x in enumerate(ratings) if x == max(ratings)]

        tmp_pick = None
        if len(max_indices) > 1:
            for i in max_indices:
                if hand_cards[i][card_type] == 0:
                    tmp_pick = i
                    break
        if tmp_pick is not None:
            card_i = tmp_pick
        else:
            card_i = max_indices[0]        



        picked_card = hand_cards[card_i]

        if picked_card[card_type] != 0:
            if picked_card[card_type] == 3:
                blue_spell_counter += 1
            all_spell_counter += 1

        if picked_card[cost] >= 8:
            curve[8][0] -= 1
        else:
            curve[picked_card[cost]][0] -= 1
        
        print("PICK " + str(card_i))

    else:
        # generate all possible moves recursively 
        board_state = (player_board, opponent_board, hand_cards, player_stats[0][0], player_stats[0][1], player_stats[1][0])
        allMoves = generateAllMoves(board_state)
        
        move_count = len(allMoves)
        # sort all moves by their rating stored in allmoves[i][1] in descending order if there us more than one move
        if move_count >= 1:
            allMoves.sort(key=lambda x: x[1], reverse=True)
            # get the 3 best moves if there are more than 3 moves available (if there are less than 3 moves available, allMoves will be returned)
            if move_count > 3:
                allMoves = allMoves[:3]
            else:
                allMoves = allMoves[:]

    # --------------------- END TURN ---------------------
            first = True
            for move in allMoves:
                if first:
                    print(moveToString(move[0])[:-1])
                    first = False
                    continue
                print(moveToString(move[0]), file=sys.stderr, flush=True)
        else:
            print("PASS")

