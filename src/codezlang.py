import random
import sys

def args(_class):
 if len(sys.argv) > 1:
  temp = sys.argv[1].split(".")
  if temp[1] == 'codezlang':
   with open(sys.argv[1], 'r') as f:
    _class.run(f.read())

    _class.exec()

class CodeZlang:
 def __init__(self):
  self.lexed = {}
  self.vars = {}

 def lexline(self, content):
  tokens = []
  content = content.split()
  index = 0
  for i in content:
      if i == 'lit':
       tokens.append(['LIT_DECLARE', i])
      elif i == 'rn':
       tokens.append(['END', 'rn'])
      elif i == 'rand':
       tokens.append(['RAND', 'rand'])
      elif i == 'do':
       tokens.append(['COMMIT', 'do'])
      elif i == 'say':
       tokens.append(['SAY', i])
      elif i == 'be':
       tokens.append(['DEC', 'be'])
      else:
       i = i.replace('|', ' ')
       tokens.append(['IDENT', i])
      index += 1
  self.lexed[len(self.lexed)] = tokens

 def run(self, str):
  str = str.split('\n')
  for line in str:
   self.lexline(line)

 def exec(self):
  lexIndex = 0
  content = []
  for i in self.lexed:
   content = self.lexed[lexIndex]
   index = 0
   if content[len(content) -1] == ['END', 'rn']:
    for i in content:
     if i[0] == 'LIT_DECLARE':
      if content[index +1][0] == 'IDENT':
       if content[index +2][0] == 'DEC':
        if content[index +2][1] == 'be':
         if content[index +3][0] == 'IDENT':
          self.vars[content[index +1][1]] = content[index +3][1]
     elif i[0] == 'SAY':
      indexs = 0
      tos = content[indexs +1][1]
      for k, v in self.vars.items():
       tos = tos.replace('<<' + k + '>>', v)
      print(tos)
     elif i[0] == 'RAND':
      if content[index +1][0] == 'COMMIT':
       if content[index +1][1] == 'do':
        if content[index +2][0] == 'IDENT':
         var = content[index +2][1]
         if content[index +3][0] == 'IDENT':
          tempMin = content[index +3][1]
          for k, v in self.vars.items():
           tempMin = tempMin.replace('<<' + k + '>>', str(v))
          min = int(tempMin)
          if content[index +4][0] == 'IDENT':
           tempMax = content[index +4][1]
           for k, v in self.vars.items():
            tempMax = tempMax.replace('<<' + k + '>>', str(v))
           max = int(tempMax)
           self.vars[var] = str(random.randint(min, max))
      
   lexIndex += 1

lang = CodeZlang()

if __name__ == '__main__':
 args(lang)
