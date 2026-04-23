import random

def get_answer(answer_num):
	if answer_num == 1:
		return 'YES'
	elif answer_num == 2:
		return 'I guess so'
	elif answer_num == 3:
		return 'I hope so'
	elif answer_num == 4:
		return 'Ask again later'
	elif answer_num == 5:
		return 'No'
	elif answer_num == 6:
		return 'not so good'
	elif answer_num == 7:
		return 'Very doubtful'
	elif answer_num == 8:
		return 'Ask again'
	elif answer_num == 9:
		return 'Yeeee!'

r = random.randint(1,9)
fortune = get_answer(r)
print(fortune)
