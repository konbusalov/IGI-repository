from services.shapes import Hexagon, HexagonDrawer

def task4():
    try:
        length = float(input("Input side length (positive number): "))
        if length <= 0:
            raise ValueError("Length must be positive")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

    try:
        color = input("Input color: ").strip()
        if not color:
            raise ValueError("Color cannot be empty")
        if not color.isalpha():
            raise ValueError("Color should contain only letters")
    except ValueError as e:
        print(f"Invalid color: {e}. Please try again.")

    hexagon = Hexagon(length, color)

    try:
        label = input("Input label: ").strip()
        if not label:
            raise ValueError("label cannot be empty")
    except ValueError as e:
        print(f"Invalid color: {e}. Please try again.")

    info = hexagon.get_info()
    print('-'*148)
    print(info)
    print('-'*148)

    hexagon_drawer = HexagonDrawer()

    hexagon_drawer.draw_hexagon(hexagon, label)
    hexagon_drawer.save_to_file("hexagon.png")


    

