def priority_scheduling(processes):
    processes.sort(key=lambda x: x[2])   
    
    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)

    for i in range(1, len(processes)):
        waiting_time[i] = processes[i-1][1] + waiting_time[i-1]


    for i in range(len(processes)):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    avg_waiting = sum(waiting_time) / len(processes)
    avg_turnaround = sum(turnaround_time) / len(processes)

    print("\n--- PRIORITY SCHEDULING (Non-preemptive) ---")
    print("Process\tBurst\tPriority\tWaiting\tTurnaround")
    for i, p in enumerate(processes):
        print(f"P{p[0]}\t{p[1]}\t{p[2]}\t\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")


def round_robin(processes, quantum):
    n = len(processes)
    rem_bt = [p[1] for p in processes]     
    waiting_time = [0] * n
    t = 0  


    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    waiting_time[i] = t - processes[i][1]
                    rem_bt[i] = 0
        if done:
            break

    turnaround_time = [processes[i][1] + waiting_time[i] for i in range(n)]

    avg_waiting = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    print("\n--- ROUND ROBIN SCHEDULING ---")
    print("Process\tBurst\tWaiting\tTurnaround")
    for i, p in enumerate(processes):
        print(f"P{p[0]}\t{p[1]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")


if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    
    processes = []
    for i in range(n):
        burst = int(input(f"Enter Burst Time for P{i+1}: "))
        priority = int(input(f"Enter Priority for P{i+1}: "))
        processes.append([i+1, burst, priority])

    priority_scheduling(processes.copy())

    quantum = int(input("\nEnter Quantum Time for Round Robin: "))
    round_robin(processes.copy(), quantum)
