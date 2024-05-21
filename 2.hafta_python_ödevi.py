
def  euclideanDisteance(liste1):
     x1 = liste1[0]
     y1 = liste1[1]
     x2 = liste1[2]
     y2 = liste1[3]
     d=(((liste1[0] - liste1[2]) ** 2) + ((liste1[1]-liste1[3]) ** 2)) ** 0.5
     print(d)
     return "d"

def point(x,y):# koordinatlar oluşturma
  a =str(x)
  b =str(y)
  return " A{}({},{})".format(i, a, b)

print("iki farklı nokta için koordinatları giriniz.(x,y)\n")
while True:
  liste1=[]
  liste=[]
  for i in range(1,3):
    #for j in range(1,3):
      x=int(input("x="))
      y=int(input("y="))
      print("*********")
      #point(x, y)
      liste1.append(x)
      liste1.append(y)

      if liste ==[]:
         liste.append(point(x,y))
      else:
        liste.append(point(x,y))

      i+=1

  break

euclideanDisteance(liste1)


