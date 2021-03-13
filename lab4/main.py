def processing(command):
    global parentship, namespaces
    command = command.split(' ')

    if command[0] == "create":
        namespace, parent = command[1], command[2]
        parentship[parent].append(namespace)
        parentship[namespace] = []
        namespaces[namespace] = []

    elif command[0] == "add":
        namespace, var = command[1], command[2]
        namespaces[namespace].append(var)

    elif command[0] == "get":
        namespace, var = command[1], command[2]
        current_ns = namespace
        while True:
            if current_ns is None:
                print("None")
            if var in namespaces[current_ns]:
                print(current_ns)
            else:
                for ns, children in parentship.items():
                    if current_ns in children:
                        current_ns = ns
                        break


if __name__ == '__main__':
    parentship = {None: ["global"], "global": []}
    namespaces = {"global": []}
    for _ in range(int(input())):
        processing(input())


