CAPACITY = 5
TURNS = 50
def update_larry(memory, x):
    mem = list(memory)
    if x in mem: mem.remove(x)
    elif len(mem) == CAPACITY: mem.pop(0)
    mem.append(x)
    return tuple(mem)

def update_rob(memory, x):
    mem = list(memory)
    if x in mem: return memory
    elif len(mem) == CAPACITY: mem.pop(0)
    mem.append(x)
    return tuple(mem)

def conanicalize(larry_memory, rob_memory):
    mapping = {}
    updated_larry = []
    updated_rob = []
    for i, x in enumerate(larry_memory):
        mapping[x] = i
        updated_larry.append(i)

    for x in rob_memory:
        if x not in mapping: mapping[x] = len(mapping)
        updated_rob.append(mapping[x])
    return tuple(updated_larry), tuple(updated_rob)

def get_transitions(larry_memory, rob_memory):
    transitions = []
    present_num = set(larry_memory) | set(rob_memory)
    not_present_w = 10 - len(present_num)
    transitions = []
    for x in present_num | {-1}:
        w = 1 if x != -1 else not_present_w
        lar_point = 1 if x in larry_memory else 0
        rob_point = 1 if x in rob_memory else 0
        new_larry = update_larry(larry_memory, x)
        new_rob = update_rob(rob_memory, x)
        transitions.append((conanicalize(new_larry, new_rob), lar_point, rob_point, w))
    return transitions

start_state = ((), ())
stack = [start_state]
visited = set()
edges = {}

while stack:
    state = stack.pop()
    transitions = get_transitions(*state)
    edges[state] = transitions
    for new_state, _, _, _ in transitions:
        if new_state not in visited:
            visited.add(new_state)
            stack.append(new_state)
print(f"Total canonical states discovered: {len(visited)}")

dp = {start_state: {0: 1}}

for i in range(TURNS):
    new_dp = {}
    for state, score_dict in dp.items():
        transitions = edges[state]
        for new_state, lar_point, rob_point, w in transitions:
            if new_state not in new_dp: new_dp[new_state] = {}
            for score, count in score_dict.items():
                new_score = score + lar_point - rob_point
                if new_score not in new_dp[new_state]: new_dp[new_state][new_score] = 0
                new_dp[new_state][new_score] += count * w
    dp = new_dp

abs_score = 0
for state, score_dict in dp.items():
    for score, count in score_dict.items():
        abs_score += abs(score) * count
ans = abs_score / 10**50
print(f"Expected Value E[|L-R|]: {ans:.8f}")