#FUNCTION=1
print()
def Players(Name, playerID, age, profession, gender, isActive):
    print(f'c_name={Name}')
    print(f'c_playerID={playerID}')
    print(f'c_age={age}')
    print(f'c_profession={profession}')
    print(f'c_geder={gender}')
    print(f'c_isActive={isActive}')
    return '---Players'
print()
print(f'Player_1 : {Players("Virat",2541,41,"Cricket","Male","True")}')
print()
print()
print(f'Player_2 : {Players("Sunil",3647,35,"Football","Male","True")}')
print()
print()
print()
#FUNTION=2
print()
def Movies(Name,MovieID, DebutYR, Type, Actor, isActive):
    print(f'M_name={Name}')
    print(f'MovieID={MovieID}')
    print(f'DebutYR-{DebutYR}')
    print(f'Type={Type}')
    print(f'Actor={Actor}')
    print(f'M_isActive={isActive}')
    return '---Players'
print()
print(f'Movie_1 : {Movies("Sanju","A8547",2019,"Biopic","Ranbir","Good")}')
print()
print()
print(f'Movie_2 : {Movies("Golmaal Again","C9857",2020,"Comedy","Ajay","Great")}')
print()



