alien = {'color':'green', 'points': '5'}
new_point = alien['points']
print(alien)
print(f"You won {new_point}")
alien['color'] = 'red'
alien['x_position'] =   0
alien['y_position'] =   25
print(alien)

alien['speed']  =   'slow'
print(f"The original position is: {alien['x_position']}.")
if alien['speed']   ==   'slow':
    x_increment =   1
elif alien['speed'] ==  'medium':
    x_increment =   2
else:
    x_increment =   3
alien['x_position'] =   alien['x_position'] +   x_increment
print(f"The new position is: {alien['x_position']}.")

