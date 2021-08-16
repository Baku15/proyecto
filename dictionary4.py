al =    [{'bise': 5 ,'points':7} ]
print(al)
aliens  =   []
for val1 in range(30):
    values1 = {'color': 'green', 'points': 5, 'speed':  'slow',}
    aliens.append(values1)
print(f"\n {aliens}")

for alien in aliens[:5]:
    print(alien)
print(f"Total number of aliens are: {len(aliens)}") 

alien1 = {'color': 'green', 'points': 5, 'speed':  'slow',}
alien2 = {'color': 'green', 'points': 5, 'speed':  'slow',}
all_aliens = [alien1,alien2]
for all_allien in all_aliens:
    print(all_allien)
print(all_aliens)