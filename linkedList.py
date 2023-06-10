from node import Node  # import Node from another file

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)  # Initialize the linked list with a head node
  
  def get_head_node(self):
    return self.head_node  # Return the head node of the linked list
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)  # Create a new node with the given value
    new_node.set_next_node(self.head_node)  # Set the next node of the new node to the current head node
    self.head_node = new_node  # Set the new node as the new head node
    
  def insert_end(self, new_value):
    new_node = Node(new_value)  # Create a new node with the given value
    current_node = self.head_node
    next_node = current_node.get_next_node()
    while next_node is not None:
      current_node = next_node  # Move to the next node
      next_node = current_node.get_next_node()
    current_node.set_next_node(new_node)  # Set the new node as the next node of the current node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() is not None:
        string_list += str(current_node.get_value()) + "\n"  # Add the value of the current node to the string list
      current_node = current_node.get_next_node()  # Move to the next node
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:  # If the head node has the value to remove
      self.head_node = current_node.get_next_node()  # Set the next node as the new head node
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:  # If the next node has the value to remove
          current_node.set_next_node(next_node.get_next_node())  # Remove the next node by skipping it
          current_node = None
        else:
          current_node = next_node  # Move to the next node
    
  def remove_nodes(self, value_to_remove):
    current_node = self.get_head_node()
    while current_node and current_node.get_value() == value_to_remove:  # Remove consecutive nodes with the value to remove from the beginning
        self.head_node = current_node.get_next_node()
        current_node = self.head_node

    while current_node and current_node.get_next_node() is not None:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:  # If the next node has the value to remove
            current_node.set_next_node(next_node.get_next_node())  # Remove the next node by skipping it
        else:
            current_node = current_node.get_next_node()  # Move to the next node

# Create an instance of the LinkedList class
ll = LinkedList(5)
ll.insert_beginning(15)
ll.insert_beginning(3)
ll.insert_beginning(8)
ll.insert_beginning(10)
ll.insert_beginning(15)
ll.insert_beginning(15)
ll.insert_beginning(15)

print(ll.remove_nodes(15))  # Remove all nodes with the value 15
print(ll.insert_end(55))  # Insert a node with the value 55 at the end
print(ll.stringify_list())  # Print the values of the linked list