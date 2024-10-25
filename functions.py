FILEPATH='todos.txt'


def get_todos(file_path=FILEPATH):
  """read a text file and return the list of to-do items."""
  with open(file_path,'r') as file:
    todos_local=file.readlines()
    
  return todos_local


def write_todos(todos_local,file_path=FILEPATH):
  """ write the to-do items List in the text file """
  with open(file_path,'w') as file:
      
    file.writelines(todos_local)
    
  

if __name__=='__main__':
  print('hello')
  print(get_todos())

# print("hello from functions")

