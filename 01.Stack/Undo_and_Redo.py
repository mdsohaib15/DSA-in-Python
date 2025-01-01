from stack import Stack
def text_editor(text,pattern):
          undo = Stack()
          redo = Stack()

          for i in text:
                    undo.push(i)
          
          for i in pattern:
                    if i == "u":
                              data = undo.pop()
                              redo.push(data)
                    else:
                              data = redo.pop()
                              undo.push(data)

          result = ""

          while (not undo.isempty()):
                     result =  undo.pop() + result

          print(result)

text_editor("Hello","uurruur")