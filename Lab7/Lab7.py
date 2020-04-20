CORRECT = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', \
     'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
# Open file with the student's answers
stu_answer_file = open('stu_answers.txt', 'r')

# Populate a list with the answers from the student
for line in stu_answer_file:
    stu_answers = []
    for line in stu_answer_file:
        stu_answers.append(line.rstrip('\n'))

# Check each answer against the correct answers in CORRECT.
# Use the variable 'correct_answers' as an accumulator which
# will give the number of correct ansers on the student's work.
correct_answers = 0
for i in range(len(stu_answers)):
    if stu_answers[i] == CORRECT[i]:
        correct_answers += 1

# Check if the student passed or not, and display how they scored.
if correct_answers >= 15:
    print('The student passed with a score of ', correct_answers, 'out of 20.')
else:
    print('The student failed with a score of ', correct_answers, 'out of 20.')

# Close the file
stu_answer_file.close()