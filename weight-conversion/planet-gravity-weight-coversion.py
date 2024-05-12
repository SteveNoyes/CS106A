"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():

    MERCURY_CONST = .376

    VENUS_CONST = .889

    MARS_CONST = 0.378

    JUPITER_CONST = 2.36

    SATURN_CONST = 1.081

    URANUS_CONST = .815

    NEPTUNE_CONST = 1.14


    user_weight = input("Enter a weight on Earth:")

    user_planet = input("Enter a planet:")


    if user_planet == "Mercury":
        merc_weight = user_weight * MERCURY_CONST
        print("The equivalent weight on Mars:", merc_weight)

    if user_planet == "Venus":
        ven_weight = user_weight * VENUS_CONST
        print("The equivalent weight on Venus:", ven-weight)

    user_weight = float(user_weight)

    user_weight = user_weight * MARS_CONST

    user_weight = round(user_weight, 2)

    print("The equivalent weight on Mars:", user_weight)



if __name__ == "__main__":
    main()