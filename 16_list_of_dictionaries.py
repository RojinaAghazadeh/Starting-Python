human_0 = {'color': 'white', 'points': -1}
human_1 = {'color': 'black', 'points': 5}
human_2 = {'color': 'brown', 'points': 10}
human_3 = {'color': 'green', 'points': 20}

humans = [human_0,human_1,human_2,human_3]

for human in humans:
	print(human)

aliens = []
for alien_number in range(30):
	new_alien = {'color' : 'green' , 'points' : 100, 'speed' : 'slow'}
	aliens.append(new_alien)

for alien in aliens[:10]:
	print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))
print("Total number of humans: " + str(len(humans)))
