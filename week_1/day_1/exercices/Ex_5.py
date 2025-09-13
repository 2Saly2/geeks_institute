my_numbers = {2,3,5,7,8}
my_numbers.update({9,1})
my_numbers.remove(9)
friend_fav_numbers = {10,11,4,2,6}
our_fav_numbers= set()
our_fav_numbers.update(friend_fav_numbers , my_numbers)
# my_numbers.update(friend_fav_numbers)
# our_fav_numbers = my_numbers
print(my_numbers)
print(our_fav_numbers)