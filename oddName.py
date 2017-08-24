def main():

    Name = get_name()
    refactor = int(input("Insert the Split Factor:"))
    print_name(Name, refactor)


def print_name(Name, refactor):
    print("{}".format(Name[::refactor]))


def get_name():
    Name = str(input("Name:"))
    while Name == "":
        Name = input("Name:")
    return Name


main()