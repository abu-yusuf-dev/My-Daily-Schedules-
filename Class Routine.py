a=input("Enter Your Name  Please : ")
print("Welcome Mr.",a)

b=input("Please Choose a Day : \n 1.Friday \n 2.Saterday \n 3.Sunday \n 4.Monday \n 5.Tuesday \n 6.Wednesday \n 7.Thursday \n 8.Show Class Routine \n 9.Is there any Class test/Assignment? \n")


if b=="1":
    print(" Today is your off day..... Have Fun!! \n ")

elif b=="2":
    print(" Today is your off day.... You can do some extra work of your own today.  \n ")

elif b=="3":
    print(" You Have Two Classes Today :( \n 1.CMC Lab in Communicaton lab (11am - 1 pm) \n 2.Ts Class in 704 no. Room (2pm - 3:30 pm)  \n ")


elif b=="4":
    print(" You have 4 Classes Today :'( \n 1.CMC Class in Annex lab-3 ( 8:30am to 10 am ) \n 2.SQA Class in Annex lab-1 (10:15am - 11:45am) \n 3.SQA Lab Class in Annex lab-1(12 pm-2 pm) \n 4.SAD Class in Annex lab-1 (2pm - 3:30 pm) \n What a Sad Life Bro :( \n  ")


elif b=="5":
    print(" You have 4 Classes Today :( \n 1.TS Lab Class in Communication Lab (8:30am-10:30am) \n 2.DWDM Class in Annex Lab-1 (12pm-1pm) \n 3.TS class in Annex Lab-1 (2pm-3:30pm) \n ")


elif b=="6":
    print(" You have 3 Classes Today :( \n 1.SQA Class in Annex lab-1 (8:30am-10am) \n 2.CMC Class in Annex lab-1 (10:15am-11:45am) \n 3.SAD Class in Annex lab-1 (12 pm-1:30pm) \n ")


elif b=="7":
    print(" You have 2 Classes Today :D :D  \n 1.DWDM Lab Class in Annex lab-1 (10:45pm-12:45pm) \n 2.DWDM Class in Annex lab-1 (3:45pm-5:15pm) \n  ")

elif b == "8":
 import os

 os.startfile("F:routine.jpg")
elif b == "9":

     print("Yes. You Have 4 Class Test and 1 Assignment in this fucking Week :( \n")
     print(" 1.TS CT in Sunday \n 2.CMC & SQA CT in Monday \n 3.DWDM & SAD CT in Wednesday \n And 1 Assignment of SQA \n ")

else:
    print("Sorry ! The System is Error.")
