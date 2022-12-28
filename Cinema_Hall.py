"""
Hall management system

Seat system:
A1 A2 A3 A4
B1 B2 B3 B4
C1 C2 C3 C4 
D1 D2 D3 D4

when a seat booked then it replace by 'X', example
A1 A2 A3 A4
B1  X B3 B4
C1 C2 C3 C4 
D1 D2 D3 D4
"""

class Star_Cinema():
    __hall_list=[]
    def _entry_hall(self,object):
        self.__hall_list.append(object)

#public fuction
#this function return A0=0,0 // A1=0,1

def seat_to_no(str):
    row=ord(str[0])-ord('A')
    str2=""
    for i in range(1,len(str)):
        str2+=str[i]
    col=int(str2)
    return row,col

#public fuction
#this function return number to seat 0,0=A0
def no_to_seat(row,col):
    str=""
    str+=chr(row+ord('A'))
    str+=chr(col+ord('0'))
    return str


#Hall class 
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self._seats={}
        self._show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        super()._entry_hall(self)
    
    def entry_show(self,id,movie_name,time):
        tp=(id,movie_name,time)
        self._show_list.append(tp)
        hall_seats=[[False for i in range(self.__rows)]for j in range(self.__cols)]
        self._seats[id]=hall_seats
    
    def book_seats(self,name,phone_number,id,lst):
        for t in lst:
            self._seats[id][t[0]][t[1]]=True
        print()
        print("#### TICKET BOOKED SUCCESSFULLY!! ####\n")
        print("-------------------------------------------------------------------")
        print(f"NAME: {name}")
        print(f"PHONE NUMBER: {phone_number}\n")
        for tp in self._show_list:
            if tp[0]==id:
                print(f"MOVIE NAME: {tp[1]}\t\tTIME: {tp[2]}")
        print("TICKETS: ",end="")
        for i in lst:
            print(no_to_seat(i[0],i[1]),end=" ")
        print()
        print(f"HALL: {self.__hall_no}")
        print("-------------------------------------------------------------------\n")

    def view_show_list(self):
        print()
        print("-------------------------------------------------------------------")
        for tp in self._show_list:
            print(f'MOVIE NAME: {tp[1]}\tSHOW ID: {tp[0]}\tMOVIE TIME: {tp[2]}')      
        print("-------------------------------------------------------------------\n")
        
    def view_available_seats(self,id):
        flag=False
        for dic in self._seats:
            if id == dic:
                flag=True
                break
        if flag==True:
            print()
            for tp in self._show_list:
                if tp[0]==id:
                    print(f'MOVIE NAME: {tp[1]}\t\tTIME: {tp[2]}') 
            print("X for already booked seats")
            print()
            print("--------------------------------------------------------")
            for i in range(len(self._seats[id])):
                for j in range(len(self._seats[id][i])):
                    if self._seats[id][i][j]==False:
                        print(no_to_seat(i,j),end="\t\t")
                    else:
                        print("X",end="\t\t")
                print()
            print("--------------------------------------------------------\n")
        else:
            print()
            print("--------------------------------------------------------")
            print("ID DIDN'T MATCH WITH ANY SHOW!")
            print("--------------------------------------------------------\n")
         

    def get_rows(self):
        return self.__rows
    def get_cols(self):
        return self.__cols
        
        

        


hall=Hall(4,4,"AB33") #initially set row and column number and hall name
hall.entry_show('as15','Avengers','Nov 2 2022 3.00 PM') #set entry show 
hall.entry_show('as54','Spider man','Nov 2 2022 10.00 PM')



while True:    
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    n=int(input("ENTER OPITON: "))
    if n==1:
        hall.view_show_list()
    elif n==2:
        id=input("ENTER ID: ")
        hall.view_available_seats(id)
    elif n==3:
        name=input("ENTER CUSTOMER NAME: ")
        number=input("ENTER CUSTOMER PHONE NUMBER: ")
        id=input("ENTER SHOW ID: ")
        chk=False
        flag=False
        for i in hall._seats:
            if i==id:
                chk=True
                break
        if chk==False:
            print()
            print("--------------------------------------------------------")
            print("ID DID'T MATCH WITH ANY SHOW!")
            print("--------------------------------------------------------\n")
            continue
        k=int(input("ENTER NUMBER OF TICKETS: "))
        lst=[]
        for i in range(k):
            seat=input("ENTER SEAT NO: ")
            if(len(seat)>2):
                flag=False
                print()
                print("--------------------------------------------------------")
                print(f"INVALID SEAT NO - {seat}. TRY AGAIN!")
                print("--------------------------------------------------------\n")
                break
            row,col=seat_to_no(seat)
            tup=(row,col)
            if row>hall.get_rows() or col>hall.get_cols():
                flag=False
                print()
                print("--------------------------------------------------------")
                print(f"INVALID SEAT NO - {seat}. TRY AGAIN!")
                print("--------------------------------------------------------\n")
                break
            if hall._seats[id][row][col]!=True:
                flag=True
                lst.append(tup)
            else:
                flag=False
                print()
                print("--------------------------------------------------------")
                print(f"THESE SEATS WERE BOOKED - {seat}")
                print("--------------------------------------------------------\n")
                break
        if flag==True:
            hall.book_seats(name,number,id,lst)

    else:
        break