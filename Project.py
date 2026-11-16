
def calculate_speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    speed = distance / time
    print("Speed =", speed, "m/s")


def calculate_distance():
    speed = float(input("Enter speed (m/s): "))
    time = float(input("Enter time (s): "))
    distance = speed * time
    print("Distance =", distance, "m")


def calculate_acceleration():
    velocity = float(input("Enter final velocity (m/s): "))
    initial_velocity = float(input("Enter initial velocity (m/s): "))
    time = float(input("Enter time (s): "))
    acceleration = (velocity - initial_velocity) / time
    print("Acceleration =", acceleration, "m/s²")


def calculate_force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    force = mass * acceleration
    print("Force =", force, "N")


def calculate_kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    kinetic_energy = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", kinetic_energy, "Joules")


while True:
    print("\n===== PHYSICS OPERATIONS =====")
    print("1. Calculate Speed")
    print("2. Calculate Distance")
    print("3. Calculate Acceleration")
    print("4. Calculate Force")
    print("5. Calculate Kinetic Energy")

    choice = input("Select an operation (1-5): ")

    if choice == "1":
        calculate_speed()
    elif choice == "2":
        calculate_distance()
    elif choice == "3":
        calculate_acceleration()
    elif choice == "4":
        calculate_force()
    elif choice == "5":
        calculate_kinetic_energy()
    else:
        print("Invalid choice!")

    answer = input(
        "\nDo you want to perform another operation? (yes/no): "
    )

    if answer.lower() != "yes":
        print("Thank you for using Mark's Physics Operation Program!")
        break
