import random as rnd
import matplotlib.pyplot as plt

rarity_loop_mult = {
    "common": [0,1],
    "uncommon": [1,1],
    "rare": [2,2],
    "unique": [2,3],
    "epic": [3,4],
    "legendary": [5,6],
    "mythic": [7,8]
}

base_stat_mult = {
    "armor": [1,3],
    "attack": [1,1.5],
    "agility": [1,1.5],
    "dexterity": [1,1.5],
    "luck": [1,1.5],
    "speed": [1,1.5],
    "strength": [1,1.5],
    "hp": [5,10]
}

rarity_stat_mult = {
    "common" : 0,
    "uncommon" : 0.01,
    "rare" : 0.02,
    "unique" : 0.05,
    "epic" : 0.1,
    "legendary" : 0.2,
    "mythic" : 0.3
}

material_mult = {
    "equip": {
        "cloth": -0.03,
        "cardboard": -0.03,
        "plastic": -0.03,
        "wood": -0.03,
        "leather": 0,
        "stone": 0,
        "iron": 0.03,
        "silver": 0.03,
        "gold": 0.03,
        "steel": 0.08,
        "platinum": 0.08,
        "diamond": 0.2,
        "titanium": 0.2,
        "adamantite": 0.2,
        "alien": 0.2
    },
    "pickaxe": {
        "glass": -0.03,
        "cardboard": -0.03,
        "plastic": -0.03,
        "tin": -0.03,
        "wood": -0.03,
        "stone": 0.01,
        "bronze": 0.01,
        "bone": 0.01,
        "lead": 0.01,
        "copper": 0.01,
        "iron": 0.05,
        "silver": 0.05,
        "gold": 0.05,
        "steel": 0.1,
        "platinum": 0.1,
        "paper": 0.3,
        "diamond": 0.3,
        "titanium": 0.3,
        "adamantite": 0.3,
        "alien": 0.3
    }
}

available_stats = {
    "sword" : ["attack"],
}

available_materials = {
    "sword" : ["cardboard", "plastic", "wood", "stone", "iron", "silver", "gold", "steel", "platinum", "diamond", "titanium", "adamantite", "alien"]
}

rarity_chances = {
    "common": 0.2,
    "uncommon": 0.25,
    "rare": 0.15,
    "unique": 0.15,
    "epic": 0.10,
    "legendary": 0.10,
    "mythic": 0.05
}

material_chances = {
    "glass": 0.35,
    "cloth": 0.35,
    "cardboard": 0.35,
    "plastic": 0.35,
    "tin": 0.35,
    "wood": 0.35,
    "leather": 0.3,
    "stone": 0.3,
    "bronze": 0.3,
    "bone": 0.3,
    "lead": 0.3,
    "copper": 0.3,
    "iron": 0.2,
    "silver": 0.2,
    "gold": 0.2,
    "steel": 0.1,
    "platinum": 0.1,
    "paper": 0.05,
    "diamond": 0.05,
    "titanium": 0.05,
    "adamantite": 0.05,
    "alien": 0.05
}

def gen_max_attack_for_sword(rarity, material, level):
    material_m = material_mult["equip"][material]
    rarity_loop_m = rarity_loop_mult[rarity]
    rarity_stat_m = rarity_stat_mult[rarity]
    base_stat_m = base_stat_mult["attack"]
    return rarity_loop_m[1] * base_stat_m[1] * (level + level * 2 *  (material_m + rarity_stat_m))

def gen_random_attack_for_sword(rarity, material, level):
    stat = 0
    material_m = material_mult["equip"][material]
    rarity_loop_m = rnd.choice(rarity_loop_mult[rarity])
    rarity_stat_m = rarity_stat_mult[rarity]
    for i in range(rarity_loop_m+1):
        # random float between base_stat_mult["attack"][0] and base_stat_mult["attack"][1]
        base_stat = rnd.uniform(base_stat_mult["attack"][0], base_stat_mult["attack"][1])
        stat += base_stat * (level + level * 2 *  (material_m + rarity_stat_m))
    
    return stat
    
    


    


def main():
    # plot_sword_by_rarities(404, "diamond")
    # plot_sword_by_materials(404, "mythic")
    # plot_sword_by_level(404)
    plot_sword_group_by_material(404)
    # plot_sword_group_by_rarity(404)
    

    
def plot_sword_by_rarities(item_lvl, item_material):
    vs = []
    rs = []
    simulation_count = 1000000
    bin_count = 1000
    for rarity in rarity_loop_mult.keys():
        values = []
        for i in range(simulation_count):
            values.append(gen_random_attack_for_sword(rarity, item_material, item_lvl))
        vs.append(values)
        rs.append(rarity)
    # plot each list in vs in the same histogram with different colors
    for i in range(len(vs)):
        plt.hist(vs[i], bins=bin_count, alpha=0.5, label=rs[i])
    plt.legend(loc='upper right')
    plt.show()


def plot_sword_by_materials(item_lvl, item_rarity):
    vs = []
    material_names = []
    material_ms = []
    simulation_count = 1000000
    bin_count = 1000
    for material in available_materials["sword"]:
        if material_mult["equip"][material] in material_ms:
            m_index = material_ms.index(material_mult["equip"][material])
            material_names[m_index] += ", " + material
            continue

        values = []
        for i in range(simulation_count):
            values.append(gen_random_attack_for_sword(item_rarity, material, item_lvl))
        vs.append(values)
        material_names.append(material)
        material_ms.append(material_mult["equip"][material])
    # plot each list in vs in the same histogram with different colors
    for i in range(len(vs)):
        plt.hist(vs[i], bins=bin_count, alpha=0.5, label=material_names[i])
    plt.legend(loc='upper right')
    plt.show()

def plot_sword_by_level(item_lvl):
    vs = []
    simulation_count = 1000000
    bin_count = 1000
    material_rate = [material_chances[material] for material in available_materials["sword"]]
    for i in range(simulation_count):
        material = rnd.choices(available_materials["sword"], weights=material_rate, k=1)[0]
        rarity = rnd.choices(list(rarity_chances.keys()), weights=list(rarity_chances.values()), k= 1)[0]

        vs.append(gen_random_attack_for_sword(rarity, material, item_lvl))


    plt.hist(vs, bins=bin_count, alpha=0.5, label="with_mat_chance")
    plt.legend(loc='upper right')
    plt.show()

def plot_sword_group_by_rarity(item_level):
    vs = {}
    simulation_count = 1000000
    bin_count = 1000
    for rarity in rarity_chances.keys():
        vs[rarity] = []
        v = []
        for material in available_materials["sword"]:
            for i in range(simulation_count//10):
                v.append(gen_random_attack_for_sword(rarity, material, item_level))
        vs[rarity] = v
    # plot each list in vs in the same histogram with different colors
    for key in vs.keys():
        plt.hist(vs[key], bins=bin_count, alpha=0.5, label=key)

    plt.legend(loc='upper right')
    plt.show()

def plot_sword_group_by_material(item_level):
    vs = []
    material_names = []
    material_ms = []
    simulation_count = 1000000
    bin_count = 1000
    for material in available_materials["sword"]:
        if material_mult["equip"][material] in material_ms:
            m_index = material_ms.index(material_mult["equip"][material])
            material_names[m_index] += ", " + material
            continue

        values = []
        for rarity in rarity_chances.keys():
            for i in range(simulation_count//10):
                values.append(gen_random_attack_for_sword(rarity, material, item_level))
        vs.append(values)
        material_names.append(material)
        material_ms.append(material_mult["equip"][material])
    # plot each list in vs in the same histogram with different colors
    for i in range(len(vs)):
        plt.hist(vs[i], bins=bin_count, alpha=0.5, label=material_names[i])
    plt.legend(loc='upper right')
    plt.show()


if __name__ == "__main__":
    main()

