#! python3


def ground(weight) -> float:
    if weight <= 2:
        return (1.50 * weight) + 20
    elif weight <= 6:
        return (3.00 * weight) + 20
    elif weight <= 10:
        return (4.00 * weight) + 20
    else:
        return (4.75 * weight) + 20


def drone(weight) -> float:
    if weight <= 2:
        return 4.50 * weight
    elif weight <= 6:
        return 9.00 * weight
    elif weight <= 10:
        return 12.00 * weight
    else:
        return 14.25 * weight


def ship(weight):
    if ground(weight) < drone(weight) and ground(weight) < 125:
        diff = drone(weight) - ground(weight)
        print("At only ${:.2f}, ground shipping will be the cheapest option for a {} lb package. \n".format(
            ground(weight), weight, drone(weight), diff))
    elif drone(weight) < ground(weight) and drone(weight) < 125:
        diff = ground(weight) - drone(weight)
        print("At only ${:.2f}, drone shipping will be the cheapest option for a {} lb package. Ground shipping would "
              "cost ${:.2f}. That's a savings of ${:.2f}! \n".format(
                drone(weight), weight, ground(weight), diff))
    elif drone(weight) == ground(weight) and drone(weight) < 125:
        print("Either ground or drone shipping will cost ${}. \n".format(drone(weight)))
    elif ground(weight) > 125 and drone(weight) > 125:
        print(
            "Premium shipping will be the cheapest option for a package of {} lbs, and will cost $125.00. Ground "
            "shipping would cost ${:.2f}, and drone shipping would cost ${:.2f}. \n".format(
                weight, ground(weight), drone(weight)))


assert ground(8.4) == 53.60
assert drone(1.5) == 6.75

for i in range(1, 250):
    ship(i / 10)
