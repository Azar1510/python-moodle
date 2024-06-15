Winner of Election
Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.
Examples: 
Input :  votes[] = {"john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"};
Output : John
We have four Candidates with name as 'John', 'Johnny', 'jamie', 'jackie'. The candidates John and Johny get maximum votes. Since John is alphabetically smaller, we print it. Use dictionary to solve the above problem

n = int(input())
max_average = float('-inf')
min_average = float('inf')
max_assignment = float('-inf')
min_lab = float('inf')
max_average_students = []
max_assignment_students = []
min_lab_students = []
min_average_students = []
for _ in range(n):
    name, test, assignment, lab = input().split()
    test = int(test)
    assignment = int(assignment)
    lab = int(lab)
    average = (test + assignment + lab) / 3
    if average > max_average:
        max_average = average
        max_average_students = [name]
    elif average == max_average:
        max_average_students.append(name)
    if average < min_average:
        min_average = average
        min_average_students = [name]
    elif average == min_average:
        min_average_students.append(name)
    if assignment > max_assignment:
        max_assignment = assignment
        max_assignment_students = [name]
    elif assignment == max_assignment:
        max_assignment_students.append(name)
    if lab < min_lab:
        min_lab = lab
        min_lab_students = [name]
    elif lab == min_lab:
        min_lab_students.append(name)
print(*sorted(max_average_students))
print(*sorted(max_assignment_students))
print(*sorted(min_lab_students))
print(*sorted(min_average_students))

