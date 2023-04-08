import random

# place the changer randomly
def build_bag():
    # bag is initialized empty
    bag = [False, False, False, False]
    # outside is initialized empty
    outside = False

    # 80% change the charger is in the bag
    is_in_bag = random.randint(0, 4) > 0

    if is_in_bag:
        # place the changer in the bag randomly
        bag_index = random.randint(0, 3)
        bag[bag_index] = True
    else:
        # the charger is not in the bag
        outside = True

    return bag, outside


# checks to see if the charger is in the bag
def check_bag(bag):
    return True in bag

# checks the first 3 compartments of the bag for the charger
def filter_bag(bag):
    return True in bag[:3]

def run():
    # randomly place the charger in the bag or outside
    bag, outside = build_bag()
    # check for bags that have the charger in one of the first 3 compartments
    if filter_bag(bag):
        return 0
    else:
        # check whether the charger is in the bag or not
        return 1 if outside else -1

run_count = 1000000 # one millions runs
filtered = 0 # how many are not valid runs
inside = 0 # number where the charger is in the last compartment
outside = 0 # number where the charger is not in the bag

for i in range(run_count):
    # check the bag
    value = run()
    # if it is in one of the first 3 compartments
    if value == 0:
        filtered += 1
    # if it is outside the bag
    elif value == 1:
        outside += 1
    # if it is in the last compartment
    else:
        inside += 1

# valid runs are ones where the charger was not in the first 3 compartments
valid_runs = run_count - filtered

print(f'filtered = {filtered / run_count}')
print(f'inside = {inside / valid_runs}')
print(f'outside = {outside / valid_runs}')
