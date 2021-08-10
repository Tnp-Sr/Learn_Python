import class_tank as tank

first_tank = tank.Tank('PY',5)
first_tank.name='PV'
print('f_tank')
print(first_tank.name)
print(first_tank.ammo)
first_tank.add_ammo(5)
print(first_tank.ammo)

print('s_tank')
second_tank = tank.Tank('TM',4)
print(second_tank.name)
second_tank.add_ammo(20)
print(second_tank.ammo)
second_tank.fire_ammo()
print(second_tank.ammo)

