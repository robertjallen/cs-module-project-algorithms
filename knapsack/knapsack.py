'''Explorer's Dilemna - aka the Knapsack Problem
After spending several days exploring a deserted island out in the Pacific, 
you stumble upon a cave full of pirate loot! There are coins, jewels, 
paintings, and many other types of valuable objects.
However, as you begin to explore the cave and take stock of what you've 
found, you hear something. Turning to look, the cave has started to flood! 
You'll need to get to higher ground ASAP. 
There IS enough time for you to fill your backpack with some of the items 
in the cave. Given that...
- you have 60 seconds until the cave is underwater
- your backpack can hold up to 50 pounds
- you want to maximize the value of the items you retrieve (since you can 
only make one trip)
HOW DO YOU DECIDE WHICH ITEMS TO TAKE?
'''
import itertools
import random
import time
class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.efficiency = 0
    def __str__(self):
        return f'{self.name}, {self.weight} lbs, ${self.value}'
    def __repr__(self):
        return self.__str__()
small_cave = []
medium_cave = []
large_cave = []
def fill_cave_with_items():
    '''Randomly generates Item objects and 
    creates caves of different sizes for testing
    '''
    names = ["painting", "jewel", "coin", "statue", "treasure chest", 
              "gold", "silver", "sword", "goblet", "hat"]
    for _ in range(5):
        n = names[random.randint(0,4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        small_cave.append(Item(n, w, v))
    for _ in range(15):
        n = names[random.randint(0,4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        medium_cave.append(Item(n, w, v))
    for _ in range(25):
        n = names[random.randint(0,4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        large_cave.append(Item(n, w, v))
def print_results(items, knapsack):
    '''Print out contents of what the algorithm  
    calculated should be added to the knapsack
    '''
    # print(f'\nItems in the cave:')
    # for i in items:
    #     print(i)
    print('\nBest items to put in knapsack: ')
    for item in knapsack:
        print(f'-{item}')
    print(f'\nResult calculated in {time.time()-start:.5f} seconds\n')
    print('\n-------------------------')
# go through the items
# add them to your backpack
# if the total weight is under 50 lbs, take another item
# take the lightest
# take the most valuable
def knapsack_solver(sack, items):
    '''# Put highest value items in knapsack until full
    (other basic, naive approaches exist)
    '''
    # Overall runtime: n log n
    # TODO - sort items by value
    items.sort(key=lambda item: item.value, reverse=True)  # O(n log n)
    # TODO - put most valuable items in knapsack until full
    sack = []
    sack_weight = 0
    max_weight = 50
    for item in items:  # O(n)
        if sack_weight + item.weight > max_weight:
            break
        sack.append(item)
        sack_weight += item.weight
    return sack
def brute_force_fill_knapsack(sack, items):
    ''' Try every combination to find the best'''
    # TODO - generate all possible combinations of items
    all_combos = []
    for r in range(1, len(items) + 1):  # r is the length of the combination
        combos_of_length_r = itertools.combinations(items, r)
        all_combos.extend(combos_of_length_r)
    # TODO - calculate the value of all combinations
    max_weight = 50
    max_value = 0
    max_sack = []
    for combo in all_combos:
        cur_weight = 0
        cur_value = 0
        for item in combo:
            cur_weight += item.weight
            cur_value += item.value
        if cur_weight > max_weight:
            continue
        if cur_value > max_value:
            max_value = cur_value
            max_sack = combo
        # find the combo with the highest value
    print(max_sack)
    return max_sack
def greedy_fill_knapsack(sack, items):
    '''Use ratio of [value] / [weight] 
    to choose items for knapsack
    '''
    # TODO - calculate efficiencies
    # TODO - sort items by efficiency
    # TODO - put items in knapsack until full
    return sack
# TESTS -
# Below are a series of tests that can be utilized to demonstrate
# the differences between each approach. Timing is included to give
# students an idea of how poorly some approaches scale. However, 
# efficiency should also be formalized using Big O notation.
fill_cave_with_items()
knapsack = []
# Test 1 - Naive
print('\nStarting test 1, naive approach...')
# items = large_cave
items = medium_cave
start = time.time()
knapsack = knapsack_solver(knapsack, items)
print_results(items, knapsack)
# Test 2 - Brute Force
print('Starting test 2, brute force...')
items = medium_cave
start = time.time()
knapsack = brute_force_fill_knapsack(knapsack, items)
print_results(items, knapsack)
# Test 3 - Brute Force
# knapsack = []
# print('Starting test 3, brute force...')
# items = large_cave
# start = time.time()
# knapsack = brute_force_fill_knapsack(knapsack, items)
# print(knapsack)
# print_results(items, knapsack)
# # Test 4 - Greedy
# print('Starting test 4, greedy approach...')
# items = medium_cave
# start = time.time()
# greedy_fill_knapsack(knapsack, items)
# print_results(items, knapsack)
# Test 5 - Greedy
# print('Starting test 5, greedy approach...')
# items = large_cave
# start = time.time()
# greedy_fill_knapsack(knapsack, items)
# print_results(items, knapsack)