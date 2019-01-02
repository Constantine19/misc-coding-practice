class Node():
    def __init__(self):
        self.value = 0
        self.nxt = 0

    


my_list = Node()
my_list.value = 5
my_list.nxt = Node()
my_list.nxt.nxt = Node()

count = 0
while my_list.nxt != 0:
    count += 1
    my_list = my_list.nxt

print count
