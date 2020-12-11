# Aaron Martin
#
# Program that takes in answers created by the machine reader program and the correct answers and grades the accuracy of the results, marking how many were incorrect for each question and how many were correct total, and the accuracy
#
# Input:
# Machine answers:
# A C C B
# D B C A
# Correct answers:
# A C C D
# D A C D
# Output:
# A C C B | A C C D | 1
# D B C A | D A C D | 2
# Correct: 5
# Accuracy: .625
#
#	1. 

import sys

def main(argv):

	f1name = argv[1]
	f2name = argv[2]

	f1 = open(f1name, "r")
	f2 = open(f2name, "r")

	correct = 0
	incorrect = 0

	for ans, gold in zip(f1.readlines(), f2.readlines()):
		ans = ans[:-1]
		gold = gold[:-1]

		anss = ans.split("\t")
		golds = gold.split("\t")

		incor = 0

		for let, glet in zip(anss, golds):

			if(let == glet):
				correct += 1
			else:
				incor += 1
				incorrect += 1

		print(ans, end="\t|\t")
		print(gold, end="\t|\t")
		print(incor)

	print("Num correct: ", correct)
	print("Accuracy: ", correct/(correct+incorrect))

	f1.close()
	f2.close()

main(sys.argv)
