train_mass = 22680.14
train_acceleration = 10.07
train_distance = 100

bomb_mass = 1


def f_to_c(f_temp) -> float:
    c_temp = (f_temp - 32) * (5/9)
    return c_temp


def c_to_f(c_temp) -> float:
    f_temp = c_temp * (9/5) + 32
    return f_temp


def get_force(mass, acceleration) -> float:
    return mass * acceleration


def get_energy(mass, c=(3*10**8)) -> float:
    return mass * (c**2)


def get_work(mass, acceleration, distance) -> float:
    return get_force(mass, acceleration) * distance


f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
train_force = get_force(train_mass, train_acceleration)
bomb_energy = get_energy(bomb_mass)
train_work = get_work(train_mass, train_acceleration, train_distance)

print(train_force)
print('The GE train supplies {} Newtons of force.'.format(train_force))
print('A 1kg bomb supplies {} Joules.'.format(bomb_energy))
print('The GE train does {0} Joules of work over {1} meters.'.format(train_work, train_distance))
