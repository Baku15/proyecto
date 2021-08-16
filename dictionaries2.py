favorite_languages  =   {
    'sara': 'c',
    'carlos':   'ruby',
    'maria':    'java',
}
for k,v in favorite_languages.items():
    print(f"\n {k} Favorite languages is: {v.title()}")


print(favorite_languages)
print(f"the favorite languages is: {favorite_languages['carlos'].title()}.")

alien_0 = {'color': 'green', 'speed': 'slow',}
verificar   = alien_0.get('points')
print(verificar)

user = {'first_name': 'carlos', 
        'last_name':'bazan' , 
        'age':15 ,  
        'city':'Bolivia',}
for key ,  value in user.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value}" )
