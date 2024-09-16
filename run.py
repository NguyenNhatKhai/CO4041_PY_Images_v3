#

import subprocess

run_times = 10
compare_times = 5

for i in range(run_times):
    print(f"Performing {i}{'th' if 10 <= i % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(i % 10, 'th')} iteration")
    output_file_name = f"Output/output_{i}.txt"
    subprocess.run(["python", "main.py", output_file_name])

print(f"Calculating averages")
sums = [0.0] * compare_times
for i in range(run_times):
    output_file_name = f"Output/output_{i}.txt"
    with open(output_file_name, 'r') as file:
        lines = file.readlines()
        for j in range(compare_times):
            sums[j] += float(lines[j].strip())
averages = [sum / run_times for sum in sums]
with open(f"Output/output.txt", 'w') as file:
    for average in averages:
        file.write(f"{average:.32f}\n")