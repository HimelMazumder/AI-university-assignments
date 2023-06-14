def calc_cost(state_p):
    cost_f = 0
    l = len(state)

    for i in range(l):
        for j in range(i + 1, l):
            if state_p[i] > state_p[j]:
                cost_f += 1

    return cost_f


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

            if new_cost < cost_f:
                cost_f = new_cost
                best_state = new_state

    if cost_f < current_state_cost:
        return best_state, cost_f
    else:
        return best_state, None


def check_goal(state_p):
    if calc_cost(state_p) == 0:
        return True
    else:
        return False


state = [2, 1, 5, 0, 8, 4, 10, 0, 20, 10]
cost = calc_cost(state)

while not check_goal(state):
    state, cost = generate_state(state.copy(), cost)

    if cost is None:
        print("goal state: ", state)
        exit()

print("")
print("goal state: ",  state)
