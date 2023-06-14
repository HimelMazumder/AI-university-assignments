import math
import random

def calc_cost(state_p):
    cost_f = 0
    l = len(state)

    for i in range(l):
        for j in range(i + 1, l):
            if state_p[i] > state_p[j]:
                cost_f += 1

    return cost_f


def move_or_not(d_E_f):
    random.seed(417)
    num = random.uniform(0, 1)

    if 0 <= num <= math.exp(d_E_f):
        return True
    elif num > math.exp(d_E_f):
        return False



def generate_state(current_state, current_state_cost):
    best_state = []
    cost_f = 99999999

    l = len(current_state)

    for i in range(l):
        for j in range(i + 1, l):
            new_state = current_state.copy()

            temp = new_state[i]
            new_state[i] = new_state[j]
            new_state[j] = temp

            new_cost = calc_cost(new_state)

            if new_cost < current_state_cost:
                return new_state, new_cost
            elif new_cost > current_state_cost:
                d_E = current_state_cost - new_cost
                if move_or_not(d_E):
                    return new_state, new_cost
            elif new_cost == current_state_cost:
                d_E = -0.5
                if move_or_not(d_E):
                    return new_state, new_cost


def check_goal(state_p):
    if calc_cost(state_p) == 0:
        return True
    else:
        return False


state = [2, 1, 5, 0, 8, 4, 10, 0, 20, 10]
cost = calc_cost(state)

while not check_goal(state):
    state, cost = generate_state(state.copy(), cost)

print("")
print("goal state: ",  state)
