def printlist(self, list):
    print(list)

def insertlist(self, a, b, list):
    list.insert(a, b)
    






if __name__== '__main__':
    N = int(input())
    list = []
    while(N > 0):
        command = input()
        action = command.split(" ")
        if action[0] == 'insert':
            insertlist()
        print(action)
        N -= 1

    

        