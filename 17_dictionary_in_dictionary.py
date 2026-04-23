users = { 
	'parnian' : {
		'first_name' : 'parnian',
		'last_name' : 'rahvar',
		},
	'rojina' : {
		'first_name' : 'rojina',
		'last_name' : 'aghazadeh',
		},
}
for username, user_info in users.items():
	print("\nUsername : " + username)
	full_name = user_info['first_name'] + " " + user_info['last_name']

	print("\tFull name: " + full_name.title())
