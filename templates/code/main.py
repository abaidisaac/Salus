import csv
def searchfunc():
  list_drugs=[]
  list1=[]
  list_food=[]
  global red
  global green
  with open('drugs1.csv', 'r') as csvFile:
      reader1 = csv.reader(csvFile)
      for row in reader1:
          list_drugs+=row
  csvFile.close()
  searchinp=input('enter the medication-:')
  for i in range(len(list_drugs)):
    if list_drugs[i]==searchinp:
      s=list_drugs[i+1]
    else:
      pass
  with open('Food.csv', 'r') as csvFile:
      reader2 = csv.reader(csvFile)
      for row2 in reader2:
          list_food+=row2
  csvFile.close()
  for i in range(len(list_food)):
    if s==list_food[i]:
      green=list_food[i-1]
      red=list_food[i+1]
      return(green)
      return(red)
    else:
      pass

searchfunc()