#Author : Kudzai Simau
#Prodigy Finance Graduate Program
#Question 1
# -*- coding: utf-8 -*-

import  csv

aList=[]
Total=0
MaxValue=500000
MaxNumber=0

def SortAsc(aList):
    for passnum in range(len(aList)-1,0,-1):
        for i in range(passnum):
            if int(aList[i][1])>int(aList[i+1][1]):
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp

def  OutPutData(aList):
     Total=0
     Total=0
     MaxValue=500000
     MaxNumber=0
     aOutPutList=[]
    
    
     for i in range(len(aList)):
         
         Total=Total+int(aList[i][1])
         if Total < MaxValue:
             aOutPutList.append(aList[i])
             MaxNumber=MaxNumber+1
             print (int(aList[i][1]))
             print(",")
             pass
         elif Total==MaxValue:
             aOutPutList.append(aList[i])
             MaxNumber=MaxNumber+1
             print "Maximum Limit Reached"
             print (int(aList[i][1]))
             print(",")

             break
         else:
             MaxNumber-1
             Total=Total-int(aList[i][1])
             break

     print("The total is "+str(Total))
              
     with open("maximum_number_loans.csv", "w") as File12:
         writer = csv.writer(File12, delimiter=",")
         writer.writerow(["id", "loan amount", "applicant experience "])
         writer.writerows(aOutPutList)
         writer.writerow(["Total number of loans",str(MaxNumber)])
         writer.writerow(["Total Amount",str(Total)])


def  main():

    with  open("7385e6df-4b92-4978-ae6b-85d0f142b0ea.csv","r") as File:
    
        csv_reader=csv.reader(File)
        data=list(csv_reader)
    
        for row in  data[1:]:
            print ("[ " +row[1]+","+row[2]+"] ")
            print (" ")
            if int(row[2])>= 10 :
                 print ("in bounce")
                 print row  
                 print(" ")
                 aList.append(row)
            else:
                 print ("out of bounce")
                 print row   
                 print(" ")      
        print(aList)
        SortAsc(aList)
        print("sorted")
        print(" ")
        print(aList)
        print("   ")
        print(" ")
        print("Output")
        OutPutData(aList)

if __name__=="__main__":
    main()

