class Node:
  def __init__(self, value, next_node=None):
    # Constructor method that initializes a node object with a given value and a reference to the next node.
    # If no next node is provided, it defaults to None.
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    # Returns the value stored in the node.
    return self.value
  
  def get_next_node(self):
    # Returns the reference to the next node.
    return self.next_node
  
  def set_next_node(self, next_node):
    # Sets the reference to the next node.
    self.next_node = next_node