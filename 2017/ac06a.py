with open('input06a.txt', 'r') as inFile:
    for line in inFile:
        steps = 0
        state = list(map(int,line.strip().split()))
        states = {','.join(map(str, state))}
        while steps + 1 == len(states):
            m = max(state)
            mIndex = state.index(m)
            state[mIndex] = 0
            mIndex += 1
            for i in range(0,m):
                state[(mIndex + i) % len(state)] += 1
            states.add(','.join(map(str, state)))
            steps += 1
        print(steps)
