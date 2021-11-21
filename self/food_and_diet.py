def reqcalories(h,w,a,g,act):
     rw=23*((h*h)/10000)
     cal=0
     scal=0
     if g=='Male':
          cal=int(((66.5+13.8*(w)+5*(h))-(6.8*a))*(0.9+(act/10)))
     elif g=='Female':
          cal=int(((655.1+9.6*(w)+1.9*(h))-(4.7*a))*(0.9+(act/10)))
     if (w-rw)<0:
          scal=(round((cal+256)/100)*100)-100
          line1=(f"Follow diet of {scal} calories per day for {int(-(w-rw))} months.")
     elif (w-rw)>0:
          scal=(round((cal-256)/100)*100)-100
          line1=(f"Follow diet of {scal} calories per day for {int(w-rw)} months.")
     elif w-rw==0:
          rcal=(round(cal/100))*100
          line1=("Your diet is perfectly fine")
     f=open("self\\source\\diets.txt","r")
     d=f.readlines()
     for i in d:
          #print(i,str(scal))
          if i==(str(scal)+'\n'):
               ind=d.index(i)
               line2=(f"You should follow a diet plan of as follows:\nBreakfast: {d[ind+1]}Lunch: {d[ind+2]}Dinner: {d[ind+3]}Snack {d[ind+4]}")
     line=line1+line2
     return line


'''
h=int(input("Enter hieght(cm):"))
w=int(input("Enter wieght(kg):"))
a=int(input("enter age:"))
g=input("enter gender:")
act=int(input("enter amount of exercise or physical work between 1 to 3 (1=low or no physical work, 2=avg physical work, 3= high physical work):"))
'''
