def jobseq(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True)

    max_deadline = max(job[2] for job in jobs)
    slots = [None] * (max_deadline + 1)

    total_profit = 0

    for job_id, profit, deadline in jobs:
        for slot in range(deadline, 0, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                break

    chronological_order = [job for job in slots if job is not None]

    return total_profit, chronological_order


Job_list = [
    ('J1', 35, 3),
    ('J2', 30, 4),
    ('J3', 25, 4),
    ('J4', 20, 2),
    ('J5', 15, 3),
    ('J6', 12, 1),
    ('J7', 5, 2)
]

profit, sequence = jobseq(Job_list)

print(f"Maximum profit: {profit}")
print(f"Chronological sequence: {sequence}")