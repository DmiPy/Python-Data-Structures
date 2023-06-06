from node import Node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def insert_end(self,new_value):
    new_node = Node(new_value)
    current_node = self.head_node
    next_node = current_node.get_next_node()
    while next_node != None:
      current_node = next_node
      next_node = current_node.get_next_node()
    current_node.set_next_node(new_node)

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

  def remove_nodes(self, value_to_remove):
    current_node = self.get_head_node()
    while current_node and current_node.get_value() == value_to_remove:
        self.head_node = current_node.get_next_node()
        current_node = self.head_node

    while current_node and current_node.get_next_node() is not None:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
            current_node.set_next_node(next_node.get_next_node())
        else:
            current_node = current_node.get_next_node()

# ll = LinkedList(5)
# ll.insert_beginning(15)
# ll.insert_beginning(3)
# ll.insert_beginning(8)
# ll.insert_beginning(10)
# ll.insert_beginning(15)
# ll.insert_beginning(15)
# ll.insert_beginning(15)
# print(ll.remove_nodes(15))
# print(ll.insert_end(55))
# print(ll.stringify_list())