def fcfs(processes):
    processes.sort(key=lambda x: x['arrival'])
    time = 0
    for p in processes:
        if time < p['arrival']:
            time = p['arrival']
        p['wt'] = time - p['arrival']
        time += p['burst']
        p['tat'] = p['wt'] + p['burst']
    return processes


def sjf(processes):
    processes.sort(key=lambda x: (x['arrival'], x['burst']))
    time = 0
    completed = []
    ready = []
    remaining = processes.copy()

    while remaining or ready:
        for p in remaining[:]:
            if p['arrival'] <= time:
                ready.append(p)
                remaining.remove(p)

        if ready:
            ready.sort(key=lambda x: x['burst'])
            p = ready.pop(0)
            p['wt'] = time - p['arrival']
            time += p['burst']
            p['tat'] = p['wt'] + p['burst']
            completed.append(p)
        else:
            time += 1

    return completed


def priority_scheduling(processes):
    processes.sort(key=lambda x: x['arrival'])
    time = 0
    completed = []
    ready = []
    remaining = processes.copy()

    while remaining or ready:
        for p in remaining[:]:
            if p['arrival'] <= time:
                ready.append(p)
                remaining.remove(p)

        if ready:
            ready.sort(key=lambda x: x['priority'])  
            p = ready.pop(0)
            p['wt'] = time - p['arrival']
            time += p['burst']
            p['tat'] = p['wt'] + p['burst']
            completed.append(p)
        else:
            time += 1

    return completed


def round_robin(processes, quantum):
    queue = []
    time = 0
    remaining_burst = {p['pid']: p['burst'] for p in processes}
    completed = []

    processes.sort(key=lambda x: x['arrival'])
    next_proc = 0

    while next_proc < len(processes) or queue:
        while next_proc < len(processes) and processes[next_proc]['arrival'] <= time:
            queue.append(processes[next_proc])
            next_proc += 1

        if queue:
            p = queue.pop(0)
            exec_time = min(quantum, remaining_burst[p['pid']])
            remaining_burst[p['pid']] -= exec_time
            time += exec_time

            while next_proc < len(processes) and processes[next_proc]['arrival'] <= time:
                queue.append(processes[next_proc])
                next_proc += 1

            if remaining_burst[p['pid']] > 0:
                queue.append(p)
            else:
                p['tat'] = time - p['arrival']
                p['wt'] = p['tat'] - p['burst']
                completed.append(p)
        else:
            time += 1

    return completed

if __name__ == "__main__":
    processes = [
        {"pid": 1, "arrival": 0, "burst": 7, "priority": 2},
        {"pid": 2, "arrival": 2, "burst": 4, "priority": 1},
        {"pid": 3, "arrival": 4, "burst": 1, "priority": 3},
        {"pid": 4, "arrival": 5, "burst": 4, "priority": 2},
    ]

    print("\n===== FCFS Scheduling =====")
    for p in fcfs([p.copy() for p in processes]):
        print(p)

    print("\n===== SJF Scheduling =====")
    for p in sjf([p.copy() for p in processes]):
        print(p)

    print("\n===== Priority Scheduling =====")
    for p in priority_scheduling([p.copy() for p in processes]):
        print(p)

    print("\n===== Round Robin (Quantum = 2) =====")
    for p in round_robin([p.copy() for p in processes], quantum=2):
        print(p)
