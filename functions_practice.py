def hello():
    print("Welcome to python3!")

hello()

def pack(pack1,pack2,pack3):
    pack_list = [pack1,pack2,pack3]
    return pack_list

print(pack("pillow", "blanket", "clothes"))    

def eat_lunch(list):
    if len(list) == 0:        
        print("My lunchbox is empty!")

    for item in list:

        if item == list[0]:
            print(f"First I eat {item}")
        elif item != list[0]:
            print(f"Next I eat {item}")



lunch = ["apple", "pizza", "pepsi"]
breakfast= ["cereal"]
no_lunch = []
eat_lunch(lunch)
eat_lunch(breakfast)
eat_lunch(no_lunch)
