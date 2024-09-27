import math


def collect_variables():
    x_1 = float(input("Enter x value of pivot point (x_1): "))
    y_1 = float(input("Enter y value of pivot point (y_1): "))

    x_2 = float(input("Enter x value of other point (x_2): "))
    y_2 = float(input("Enter y value of other point (y_2): "))

    return (x_1, y_1), (x_2, y_2)


def calc_azi(cords_1, cords_2):

    # The process is documented in my file.
    x_diff = cords_2[0] - cords_1[0]
    y_diff = cords_2[1] - cords_1[1]

    # Avoid division by 0.
    if x_diff == 0:
        return 0

    computed_arctan = math.degrees(math.atan(y_diff / x_diff))

    if x_diff >= 0 and y_diff >= 0:
        return computed_arctan

    elif y_diff <= 0 <= x_diff:
        return 90 - computed_arctan

    elif y_diff <= 0 and x_diff <= 0:
        return 180 + computed_arctan

    else:
        return 270 - computed_arctan


def main():

    while True:
        coordinates = collect_variables()
        result = calc_azi(coordinates[0], coordinates[1])

        print(f"The azimuth angle between {coordinates[0]} and {coordinates[1]}, aka α is: {result}")

        confirmation = input("Do you want to continue? Type 'no' to stop program: ")

        if confirmation.lower() == "no":
            break
main()
