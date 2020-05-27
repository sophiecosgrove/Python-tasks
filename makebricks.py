def make_bricks(small, big, goal):
   sinch = 1
   binch = 5
   if (small * sinch) + (big * binch) == goal:
    return True
   elif ((small * sinch) + (big * binch) - goal) % sinch == 0 or ((small * sinch) + (big * binch) - goal) % binch == 0:
    return True
   elif (goal - (small * sinch) + (big * binch)) % sinch == 0 or (goal - (small * sinch) + (big * binch)) % binch == 0:
    return True
   else:  
    return False

print(make_bricks(3,1,9))