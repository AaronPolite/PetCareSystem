from user import User
class Node:
    def __init__(self, user=User):
        self.user = user
        self.data = self.user.details
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

    def show_children(self):
        for child in self.children:
            print(child.data[2])

class Tree:
    def __init__(self, root):
        self.root = root

admin_user = User("admin", "admin", "admin@vet.com", "0", [])
admin_node = Node(admin_user)
UserTree = Tree(admin_node)

test_user = User("test", "test", "test@vet.com", "-1", [])
test_user_node = Node(test_user)
admin_node.add_child(test_user_node)

#UserTree.root.show_children()
