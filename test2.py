def start():
    f_name = "Sarah"
    l_name = "Conner"
    age = 28
    gender = "Female"
    get_name(f_name,l_name,age,gender)

def get_name(f_name,l_name,age,gender):
    print("My name is {} {}. I am {} yearold {}.".format(f_name,l_name,age,gender))



if __name__ == "__main__":
    start()

