from stack import Stack
def reverse_string(text):
          print('orignal string:',text)
          s = Stack()
          for i in text:
                    s.push(i)
          result = ''
          while(not s.isempty()):
                    result =  result + s.pop()

          print('reversed string:',result)

reverse_string("Hello")