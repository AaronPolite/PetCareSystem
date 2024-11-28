from User import User
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def print_tree(self, level=0):
        indent = "  " * level
        
        #If statement that handles the initialization of different nodes depending on the data type its made up by (at the moment its only User and str)
        if isinstance(self.data, User):
            # For User nodes, print more detailed information
            print(f"{indent}User: {self.data.get_name()} (ID: {self.data.get_user_id()}, Position: {self.data.get_position()})")
        elif isinstance(self.data, str):
            # For string nodes (will later handle the pet object node logic)
            print(f"{indent}{self.data}")
        else:
            # For other types of nodes (catch case)
            print(f"{indent}{str(self.data)}")
        
        # Recursively print children
        for child in self.children:
            child.print_tree(level + 1)

def main():
    # Create admin node
    root_node = Node("Users")

    # Create users with detailed information
    user1 = User("Andrew H.", "EMP001", "Admin", "AndrewH@gmail.com", "Admin Stuff")
    user2 = User("Aaron P.", "EMP002", "User", "AaronP@gmail.com", "Member of Daycare")
    user3 = User("Thomas J.", "EMP003", "User", "ThomasJ@gmail.com", "Member of Daycare")

    # Create user nodes
    user1_node = Node(user1)
    user2_node = Node(user2)
    user3_node = Node(user3)

    # Create pet nodes for each user
    user1_pet1 = Node("Buddy (Dog)")
    user1_pet2 = Node("Whiskers (Cat)")
    user2_pet1 = Node("Luna (Cat)")
    user3_pet1 = Node("Goldie (Dog)")
    user3_pet2 = Node("Bruno (Dog)")

    # Add pets to users
    user1_node.add_child(user1_pet1)
    user1_node.add_child(user1_pet2)
    user2_node.add_child(user2_pet1)
    user3_node.add_child(user3_pet1)
    user3_node.add_child(user3_pet2)

    # Add users to admin
    root_node.add_child(user1_node)
    root_node.add_child(user2_node)
    root_node.add_child(user3_node)

    # Print the entire tree structure
    print("Organizational Tree Structure:")
    root_node.print_tree()

    # Demonstrate accessing user information
    print("\nUser Details Demonstration:")
    print(f"User 1 Name: {user1.get_name()}")
    print(f"User 1 Email: {user1.get_email()}")
    print(f"User 1 Additional Info: {user1.get_additional()}")

    # Demonstrate modifying user information
    user1.set_position("New Admin")
    print(f"\nUpdated User 1 Position: {user1.get_position()}")

if __name__ == "__main__":
    main()