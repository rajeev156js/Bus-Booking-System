from tkinter import *
from tkinter.messagebox import *
from datetime import date
import sqlite3
con=sqlite3.Connection('database')
cur=con.cursor()


class Test:
    def w1(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))  
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=w//3)
        Label(root,text='Online Bus Booking System',font='Arial 20 bold',bg='light blue',fg='red').grid(row=1,column=0)
        Label(root,text='Name: Rajeev Ranjan',font="Arial 14 bold",fg='dark blue').grid(row=2,column=0,pady=h//30)
        Label(root,text='Er : 211b242',font="Arial 14 bold",fg='dark blue').grid(row=3,column=0,pady=h//250)
        Label(root,text='Mobile: 7209030660',font="Arial 14 bold",fg='dark blue').grid(row=4,column=0,pady=h//30)
        Label(root,text='Submitted to : Dr. Mahesh kumar',font="Arial 16",bg='light blue',fg='red').grid(row=5,column=0,)
        Label(root,text="Project Based Learning",font="Arial 16",fg='red').grid(row=6,column=0)
        def function(rajeev=0):
            root.destroy()
            self.w2()
        root.bind('<KeyPress>',function)
        root.mainloop()
        
#/............................................................................................................................................................
        
    def w2(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=w//3,columnspan=15)
        Label(root,text="Online Bus Booking System",font="Arial 24 bold",bg='light blue',fg='red').grid(row=1,column=0,columnspan=15,pady=h//40 )
        def seat_booking(rajeev=0):
            root.destroy()
            self.Seat_booking()
        Button(root,text="Seat Booking",command=seat_booking,font="Arial 20 bold",bg='light green',fg='black').grid(row=2,column=0 , padx=150)
        def check_booked_seat(rajeev=0):
            root.destroy()
            self.Check_booked_seat()
        Button(root,text="Checked Book Seat",command=check_booked_seat,font="Arial 20 bold",bg='forest green',fg='black').grid(row=2,column=1)
        def add_bus_details(rajeev=0):
            root.destroy()
            self.Add_bus_details()
        Button(root,text="Add Bus Detail",command=add_bus_details,font='Arial 20 bold',bg='dark green',fg='black').grid(row=2,column=2,padx=100,pady=h//30)
        Label(root,text='For Admin Only',font='Arial 8 bold',fg='red').grid(row=3,column=2)
        root.mainloop()
        #def function(rajeev=0):
         #   root.destroy()
          #  self.w3()
        #root.bind('<KeyPress>',function)
#/...................................................................................................................................................................     

    def Add_bus_details(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=w//3,columnspan=15)
        Label(root,text="Online Bus Booking System",font="Arial 24 bold",bg='light blue',fg='red').grid(row=1,column=0,columnspan=15,pady=h//40 )
        Label(root,text="Add New Details to DataBase" ,font="Arial 16 bold",fg='dark green').grid(row=2,column=1,columnspan=13)
        def new_operator(rajeev=0):
            root.destroy()
            self.New_operator()
        Button(root,text="New Operator",command=new_operator, font="Arial 10 bold",bg='light green' ).grid(row=3,column=0,columnspan=10 )
        def new_bus(rajeev=0):
            root.destroy()
            self.New_bus()
        Button(root,text="New Bus",command=new_bus, font="Arial 10 bold" ,bg='orange').grid(row=3,column=1,columnspan=11  )
        def new_route(rajeev=0):
            root.destroy()
            self.New_route()
        Button(root,text="New Route",command=new_route, font="Arial 10 bold" ,bg='light blue').grid(row=3,column=2,columnspan=12,pady=h//30)
        def new_run(rajeev=0):
            root.destroy()
            self.New_run()
        Button(root,text="New Run",command=new_run, font="Arial 10 bold",bg='salmon' ).grid(row=3,column=4,columnspan=14 )
        root.mainloop()
#/....................................................................................................................................................................
    def New_operator(self):
        import sqlite3
        con=sqlite3.Connection('database')
        cur=con.cursor()
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=w//3,columnspan=25)
        Label(root,text="Online Bus Booking System",font="Arial 24 bold",bg='light blue',fg='red').grid(row=1,column=0,columnspan=15,pady=h//40 )
        Label(root,text="Add Bus Operator Details" ,font="Arial 16 bold",fg='dark green').grid(row=2,column=1,columnspan=15)

        Label(root,text="Operator id" , font="Arial 10 bold"  ).grid(row=3,column=0 )
        op_id=Entry(root)
        op_id.grid(row=3,column=1)
        Label(root,text="Name" , font="Arial 10 bold"   ).grid(row=3,column=2   )
        name=Entry(root)
        name.grid(row=3,column=3)

        Label(root,text="Address" , font="Arial 10 bold" ).grid(row=3,column=4 ,pady=h//30)
        address=Entry(root)
        address.grid(row=3,column=5)

        Label(root,text="Phone" , font="Arial 10 bold"   ).grid(row=3,column=6 )
        phone=Entry(root)
        phone.grid(row=3,column=7)

        Label(root,text="Email" , font="Arial 10 bold"   ).grid(row=3,column=8  )
        email=Entry(root)
        email.grid(row=3,column=9)


        def Add():
            def insert():
                cur.execute('insert into operator(op_id,name,address,phone,email) values (?,?,?,?,?)',(op_id.get(),name.get(),address.get(),phone.get(),email.get()))
                raj=str(op_id.get())+" "+str(name.get())+" "+str(address.get())+" "+str(phone.get())+" "+str(email.get())
                Label(root,text=raj).grid(row=6,column=4)
                con.commit()
                #con.close()
                                                
                                                                                                       
            if len(op_id.get())==0 or len(name.get())==0 or len(address.get())==0 or len(phone.get())==0 or len(email.get())==0:
                showerror('error','Please fill all values...')
            else:
                insert()
        def Edit():
            cur.execute('delete from operator where op_id={};'.format(op_id.get()))
            con.commit()

            cur.execute('insert into operator(op_id,name,address,phone,email) values (?,?,?,?,?)',(op_id.get(),name.get(),address.get(),phone.get(),email.get()))
            raj=str(op_id.get())+" "+str(name.get())+" "+str(address.get())+" "+str(phone.get())+" "+str(email.get())
            Label(root,text=raj).grid(row=6,column=4)
            con.commit()
            con.close()
            

        Button(root,text="Add",command=Add, font="Arial 10 bold",bg='light green' ).grid(row=3,column=10 )
        Button(root,text="Edit",command=Edit, font="Arial 10 bold",bg='light green' ).grid(row=3,column=11 )
        def Home(rajeev=0):
             root.destroy()
             self.w2()
        img1=PhotoImage(file='.\\home.png')
        Button(root,image=img1,command=Home).grid(row=4,column=11)
        root.mainloop()


                                                                                                                
 
 
#/............................................................................................................................................................................


    def New_bus(self):
        
        import sqlite3
        con=sqlite3.Connection('database')
        cur=con.cursor()
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=w//3,columnspan=25)
        Label(root,text="Online Bus Booking System",font="Arial 24 bold",bg='light blue',fg='red').grid(row=1,column=0,columnspan=15,pady=h//40 )
        Label(root,text="Add Bus Details" ,font="Arial 16 bold",fg='dark green').grid(row=2,column=1,columnspan=15)

        Label(root,text="Bus Id" , font="Arial 10 bold"  ).grid(row=3,column=0 )
        bus_id=Entry(root)
        bus_id.grid(row=3,column=1)

        Label(root,text="Bus type" , font="Arial 10 bold"   ).grid(row=3,column=2)
        bus_type=StringVar()
        option=['AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2x1','Non-AC Sleeper 2x1']
        menu=OptionMenu(root,bus_type,*option)
        menu.grid(row=3,column=3)

        Label(root,text="Capacity" , font="Arial 10 bold" ).grid(row=3,column=4 ,pady=h//30)
        capacity=Entry(root)
        capacity.grid(row=3,column=5)

        Label(root,text="Fare Rs" , font="Arial 10 bold"   ).grid(row=3,column=6 )
        fare=Entry(root)
        fare.grid(row=3,column=7)

        Label(root,text="Operator ID" , font="Arial 10 bold"   ).grid(row=3,column=8  )
        op_id=Entry(root)
        op_id.grid(row=3,column=9)

        Label(root,text="Route ID" , font="Arial 10 bold"   ).grid(row=3,column=10 )
        route_id=Entry(root)
        route_id.grid(row=3,column=11)

        def Add_Bus():
            def insert():
                cur.execute('insert into bus(bus_id  ,bus_type  ,capacity  ,fare , r_id  ,operator_id) values (?,?,?,?,?,?)',(bus_id.get(),bus_type.get(),capacity.get(),fare.get(),route_id.get(),op_id.get()))
                raj=str(bus_id.get())+" "+str(bus_type.get())+" "+str(capacity.get())+" "+str(fare.get())+" "+str(route_id.get())+" "+str(op_id.get())
                Label(root,text=raj).grid(row=6,column=4)
                con.commit()
                #con.close()
                                             
                                                                                                       
            if len(bus_id.get())==0  or len(capacity.get())==0 or len(fare.get())==0 or len(route_id.get())==0 or  len(op_id.get())==0:
                showerror('error','Please fill all values...')
            else:
                insert()
        def Edit_Bus():
            cur.execute('delete from bus where bus_id={};'.format(bus_id.get()))
            con.commit()

            cur.execute('insert into bus(bus_id  ,bus_type  ,capacity  ,fare , r_id  ,operator_id) values (?,?,?,?,?,?)',(bus_id.get(),bus_type.get(),capacity.get(),fare.get(),route_id.get(),op_id.get()))
            raj=str(bus_id.get())+" "+str(bus_type.get())+" "+str(capacity.get())+" "+str(fare.get())+" "+str(route_id.get())+" "+str(op_id.get())
            Label(root,text=raj).grid(row=6,column=4)
            con.commit()
            con.close()
            


        Button(root,text="Add Bus",command=Add_Bus, font="Arial 10 bold",bg='light green' ).grid(row=4,column=6 )
        Button(root,text="Edit Bus",command=Edit_Bus, font="Arial 10 bold",bg='light green' ).grid(row=4,column=7 )
         
                                                                                                                
        def Home(rajeev=0):
            
            root.destroy()
            self.w2()
        img1=PhotoImage(file='.\\home.png')
        Button(root,image=img1,command=Home).grid(row=4,column=8)
        root.mainloop()
#/................................................................................................................................................................................

    def New_route(self):
        
        import sqlite3
        con=sqlite3.Connection("database")
        cur=con.cursor()

        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=w//3,columnspan=25)
        Label(root,text="Online Bus Booking System",font="Arial 24 bold",bg='light blue',fg='red').grid(row=1,column=0,columnspan=15,pady=h//40 )
        Label(root,text="Add Bus Route Details" ,font="Arial 16 bold",fg='dark green').grid(row=2,column=1,columnspan=15)

        Label(root,text="Route ID" , font="Arial 10 bold"  ).grid(row=3,column=0 )
        route_id = Entry(root)
        route_id.grid(row=3,column=1)

        Label(root,text="Station Name" , font="Arial 10 bold"   ).grid(row=3,column=2   )
        s_name = Entry(root)
        s_name.grid(row=3,column=3)

        Label(root,text="Station Id" , font="Arial 10 bold" ).grid(row=3,column=4 ,pady=h//30)
        s_id = Entry(root)
        s_id.grid(row=3,column=5)



        def Add_route():
            def insert():
                cur.execute('insert into route(route_id,station_name,station_id) values (?,?,?)',(route_id.get(),s_name.get(),s_id.get()))
                raj=str(route_id.get())+" "+str(s_name.get())+" "+str(s_id.get())
                Label(root,text=raj).grid(row=6,column=4)
                con.commit()
                #con.close()
                                                
                                                                                                       
            if len(route_id.get())==0 or len(s_name.get())==0 or len(s_id.get())==0:
                showerror('error','Please fill all values...')
            else:
                insert()
        def delete_route():
            cur.execute('delete from route where route_id={};'.format(route_id.get()))
            con.commit()

            raj=str(route_id.get())+" "+str(s_name.get())+" "+str(s_id.get())
            Label(root,text=raj).grid(row=6,column=4)
            #con.commit()
            con.close()





         
        Button(root,text="Add Route",command=Add_route, font="Arial 10 bold",bg='light green' ).grid(row=3,column=6 )
        Button(root,text="Delete Route",command=delete_route, font="Arial 10 bold",bg='light green',fg='red' ).grid(row=3,column=7 )
         
        def Home(rajeev=0):
            
            root.destroy()
            self.w2()
        img1=PhotoImage(file='.\\home.png')
        Button(root,image=img1,command=Home).grid(row=4,column=6)
        root.mainloop()
#/.......................................................................................................................................................................................

    def New_run(self):
        import sqlite3
        con=sqlite3.Connection("database")
        cur=con.cursor()

        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=w//3,columnspan=25)
        Label(root,text="Online Bus Booking System",font="Arial 24 bold",bg='light blue',fg='red').grid(row=1,column=0,columnspan=15,pady=h//40 )
        Label(root,text="Add Bus Running Details" ,font="Arial 16 bold",fg='dark green').grid(row=2,column=1,columnspan=15)

        Label(root,text="Bus ID" , font="Arial 10 bold"  ).grid(row=3,column=0 )
        bus_id = Entry(root)
        bus_id.grid(row=3,column=1)

        Label(root,text="Running Date" , font="Arial 10 bold"   ).grid(row=3,column=2   )
        running_date = Entry(root)
        running_date.grid(row=3,column=3)

        Label(root,text="Seat Available" , font="Arial 10 bold" ).grid(row=3,column=4 ,pady=h//30)
        seat_available = Entry(root)
        seat_available.grid(row=3,column=5)





        def Add_run():
            def insert():
                cur.execute('insert into run(b_id,running_date,seat_available) values (?,?,?)',(bus_id.get(),running_date.get(),seat_available.get()))
                raj=str(bus_id.get())+" "+str(running_date.get())+" "+str(seat_available.get())
                Label(root,text=raj).grid(row=6,column=4)
                con.commit()
                #con.close()
                                                
                                                                                                       
            if len(bus_id.get())==0 or len(running_date.get())==0 or len(seat_available.get())==0:
                showerror('error','Please fill all values...')
            else:
                insert()
        def Delete_run():
            cur.execute('delete from run where b_id={};'.format(bus_id.get()))
        ##    con.commit()

             
            raj=str(bus_id.get())+" "+str(running_date.get())+" "+str(seat_available.get())
            Label(root,text=raj).grid(row=6,column=4)
            con.commit()
            con.close()
            







         
        Button(root,text="Add Run",command=Add_run, font="Arial 10 bold",bg='light green' ).grid(row=3,column=6 )
        Button(root,text="Delete Run",command=Delete_run, font="Arial 10 bold",bg='light green' ).grid(row=3,column=7 )
         
 

        def Home(rajeev=0):
            root.destroy()
            self.w2()
        img1=PhotoImage(file='.\\home.png')
        Button(root,image=img1,command=Home ).grid(row=4,column=6)
        root.mainloop()
#/......................................................................................................................................................................................

    #def Home(self):

    def Check_booked_seat(self):
        
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        import sqlite3
        con=sqlite3.Connection("database")
        cur=con.cursor()
        #cur.execute("select * from booking_history where phone={}".format(int(Enter_your_mobile_no_entry.get())))
        def check_error():
            if len(Enter_your_mobile_no_entry.get())==0:
                showerror('Value Missing','Please Enter mobile number')
            else :
                
                Frame2=Frame(root,relief="groove",bd=15)
                Frame2.grid(row=11,column=0,columnspan=10)
                Label(root,text="").grid(row=10,column=0)
                cur.execute("select * from booking_history where phone={}".format(int(Enter_your_mobile_no_entry.get())))
                info=cur.fetchall()
                if(len(info)== 0):
                    ch = askyesno('No Booking Found', 'Do you want  to book seat now')
                    if(ch):
                        con.close()
                        root.destroy()
                        self.Seat_booking()
                else:
                    ac=(info[0][9])/info[0][10]
                    Label(Frame2,text='Passenger Name : '+str(info[0][1]),font='Arial 13 bold').grid(row=0,column=0,sticky='w')

                    Label(Frame2,text='No of seats : '+str(info[0][10]),font='Arial 13 bold').grid(row=1,column=0,sticky='w')

                    Label(Frame2,text='age : '+str(info[0][6]),font='Arial 13 bold').grid(row=2,column=0,sticky='w')

                    Label(Frame2,text='booking ref : '+str(info[0][0]),font='Arial 13 bold').grid(row=3,column=0,sticky='w')

                    Label(Frame2,text='travel On : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

                    Label(Frame2,text='gender : '+str(info[0][5]),font='Arial 13 bold').grid(row=0,column=1,sticky='w')

                    Label(Frame2,text='phone number : '+str(info[0][2]),font='Arial 13 bold').grid(row=1,column=1,sticky='w')

                    Label(Frame2,text='fare : '+str(ac),font='Arial 13 bold').grid(row=2,column=1,sticky='w')

                    Label(Frame2,text='booked on '+str(info[0][4]),font='Arial 13 bold').grid(row=3,column=1,sticky='w')

                    Label(Frame2,text='boarding point '+str(info[0][7]),font='Arial 13 bold').grid(row=4,column=1,sticky='w')

                    #Label(Frame2,text='Phone : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

                    Label(Frame2,text='* Total fare of '+str(info[0][9])+' /- to be paid at the time of boarding the bus',font='Arial 12 italic').grid(row=5,column=0,columnspan=10)

                

        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        title=Label(Frame_3,text="Check Your Booking",fg="green",font="Arial 13 bold",bg="light green")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=6,column=0)

        Enter_your_mobile_no=Label(root,text="Enter Your Mobile No")
        Enter_your_mobile_no.grid(row=7,column=0,sticky=E,columnspan=5)
        Enter_your_mobile_no_entry=Entry(root)
        Enter_your_mobile_no_entry.grid(row=7,column=5,sticky=W,padx=20,columnspan=3)
        

        Button(root,text="Check Booking",command=check_error).grid(row=7,column=6)
        def Home(rajeev=0):
            con.close()
            root.destroy()
            self.w2()
             
        img_1=PhotoImage(file=".\\home.png")
        Button(root,image=img_1,command=Home).grid(row=7,column=7)
        root.mainloop()
#/.......................................................................................................................................................................................

    def Seat_booking(self):
        
        con=sqlite3.Connection("database")
        cur=con.cursor()
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        frame_4=Frame(root)
        frame5=Frame(root)
        check=0
        def clicked(value):
            global check
            check=value
            


        def show_bus_details():
            con=sqlite3.Connection("database")
            cur=con.cursor()
            r=IntVar()
            frame_4.grid(row=8,column=0,columnspan=10)
            cur.execute('select * from route where station_name=:to',
                        {
                            "to":to_entry.get()
                        }
                        )
            to_records=cur.fetchall()
            #print(to_records)
            cur.execute('select * from route where station_name=:from',
                        {
                            "from":from_entry.get()
                        }
                        )
            from_records=cur.fetchall()
            #print(from_records)
            if(to_records==[]):
                showinfo("sorry"," we have no bus on this route")
                return
            if(from_records==[]):
                showinfo("sorry"," we have no bus on this route")
                return
            i=0
            j=0
            tempid=0
            for record in to_records:
                for rec in from_records:
                    if(to_records[i][0]==from_records[j][0]):
                        if(to_records[i][1]>from_records[j][1]):
                            tempid=to_records[i][0]
                    j=j+1
                i=i+1
                j=0
            if(tempid==0):
                showinfo('no bus found','sorry,no buses are available')
                return
            cur.execute('select * from run where b_id in(select bus_id from bus where r_id=:tempid) and running_date=:jdate and seat_available>0',
                        {
                            'tempid':tempid,
                            'jdate':journey_date_entry.get()
                        }
                        )
            run_info=cur.fetchall()
            if(run_info==[]):
                showinfo("sorry","no bus found")
                return
            for widget in frame_4.winfo_children():
                widget.destroy()
            Label(frame_4,text='select bus',fg="green3",font="Arial 13 bold").grid(row=0,column=0,padx=20)
            Label(frame_4,text="operator",fg="green3",font="Helvetica 12 bold").grid(row=0,column=2,padx=20)
            Label(frame_4,text="bus type",fg="green3",font="Helvetica 12 bold").grid(row=0,column=4,padx=20)
            Label(frame_4,text="Available/capacity",fg="green3",font="Helvetica 12 bold").grid(row=0,column=6,padx=20)
            Label(frame_4,text="fare",fg="green3",font="Helvetica 12 bold").grid(row=0,column=8,padx=20)
            Button(frame_4,text='Proceed To Book',fg="black", bg='green2',command=book).grid(row=2,column=10,padx=20)
            cur.execute('select count(*) from run where b_id in(select bus_id from bus where r_id=:tempid) and running_date=:jdate and seat_available>0',
                        {
                            'tempid':tempid,
                            'jdate':journey_date_entry.get()
                        }
                        )
            no_of_labels=cur.fetchall()
            enteries=no_of_labels[0][0]
            counter=0
            while(enteries!=0):
                cur.execute('select * from bus where bus_id=:busid',
                            {
                                "busid":run_info[counter][0]
                            }
                            )
                bus_info=cur.fetchall()

                cur.execute("select name from operator where op_id=:oid",
                            {
                                'oid':bus_info[0][5]
                            }
                            )
                op_name=cur.fetchall()
                Radiobutton(frame_4,text='bus'+str(counter+1),font="Helvetica 11",variable=r,value=counter+1,command=lambda : clicked(r.get())).grid(row=counter+1,column=0,padx=20,pady=5)
                Label(frame_4,text=op_name[0][0],fg='blue',font='helvetica 12 italic').grid(row=counter+1,column=2,padx=20,pady=5)
                Label(frame_4,text=bus_info[0][1],fg='blue',font='helvetica 12 bold').grid(row=counter+1,column=4,padx=20,pady=5)
                Label(frame_4,text=str(run_info[counter][2])+'/'+str(bus_info[0][2]),fg='blue',font='helvetica 12 bold').grid(row=counter+1,column=6,padx=20,pady=5)
                Label(frame_4,text=bus_info[0][3],fg='blue',font='helvetica 12 bold').grid(row=counter+1,column=8,padx=20,pady=5)
                counter=counter+1
                enteries=enteries-1
        def book():
            global check
            if(check==0):
                showerror("field missing","please select a bus")
                frame5.grid_forget()
                return
            def confirm():
                con=sqlite3.Connection("database")
                cur=con.cursor()
            

                if(cname.get()==""):
                    showerror("field missing ","please enter name")
                elif(gender.get()=="select"):
                    showerror("field missing","please enter gender")
                elif(mno.get()==""):
                    showerror("field missing","please enter mobile number")
                elif(cage.get()==""):
                    showerror("field missing","please enter age")
                elif(cseat.get()==""):
                    showerror("field missing","please enter No of seats")
                else:
                    
                    global check
                    int(mno.get())

                    int(cage.get())

                    int(cseat.get())

                    if(len(mno.get())!=10):
                        showerror("Wrong input","please enter a valid mobile number")
                        mno.delete(0,END)
                        return
                    if(int(cage.get())>130):
                        showerror("wrong error","please enter a valid age")
                        cage.delete(0,END)
                        return
                    cur.execute("select * from route where station_name=:to",
                                {
                                    'to':to_entry.get()
                                }
                                )
                    to_records=cur.fetchall()

                    cur.execute("select * from route where station_name=:from",
                                {
                                    'from':from_entry.get()
                                }
                                )
                    from_records=cur.fetchall()
                    i=0
                    j=0
                    tempid=0
                    for record in to_records:
                        for rec in from_records:
                            if(to_records[i][0]==from_records[j][0]):
                                if(to_records[i][1]>from_records[j][1]):
                                    tempid=to_records[i][0]
                            j=j+1
                        i=i+1
                        j=0
                    cur.execute("select * from run where b_id in(select bus_id from bus where r_id=:tempid) and running_date=:jdate and seat_available>0",
                                {
                                    'tempid':tempid,
                                    'jdate':journey_date_entry.get()
                                }
                                )
                    run_info=cur.fetchall()

                    if(int(cseat.get())>run_info[check-1][2] or int(cseat.get())<1):
                        showerror('invalid input',"please enter a valid number of seats")
                        cseat.delete(0,END)
                        return
                    cur.execute('select * from bus where bus_id=:busid',
                                {
                                    "busid":run_info[check-1][0]
                                }
                                )
                    bus_info=cur.fetchall()
                    cur.execute("select booking_id,phone from booking_history")
                    ref=cur.fetchall()
                    h=0
                    cur.execute("select count(*) from booking_history")
                    lastid=cur.fetchall()
                    reference=lastid[0][0]+1
                    for ph in ref:
                        if(ref[h][1]==int(mno.get())):
                            showinfo("record exist","booking from this number already exit..")
                            return
                        h=h+1
                    choice=askyesno("confimation","your fare is "+str(int(cseat.get())*bus_info[0][3])+'\nConfirm booking?')
                    cur.execute("INSERT INTO Booking_history(booking_id,p_name,phone,travel_on,booked_on,gender,age,source,destination,fare,seats) VALUES(:ref, :pname, :phone,:travelon, :bookedon, :gender,:age,:source,:destination,:fare,:seat)",

                                    {

                                        'pname': cname.get(),

                                        'ref': reference,

                                        'phone': mno.get(),

                                        'travelon': journey_date_entry.get(),

                                        'bookedon': date.today(),

                                        'gender': gender.get(),

                                        'age' : cage.get(),

                                        'source': from_entry.get(),

                                        'destination': to_entry.get(),

                                        'fare': (int(cseat.get())*bus_info[0][3]),

                                        'seat': cseat.get()

                                    }

                                    )
                    new=run_info[check-1][2]-int(cseat.get())
                    cur.execute("update run set seat_available=:seat where b_id=:busid and running_date=:journey_date",
                                {
                                    'seat': new,
                                    'busid': bus_info[0][0],
                                    'journey_date':journey_date_entry.get()
                                }
                                )
                    if(choice==1):

                        showinfo('Success','Seat booked!')

                        cname.delete(0,END)

                        cage.delete(0,END)

                        cseat.delete(0,END)

                        mno.delete(0,END)

                        gender.set("Select")

                        frame5.grid_forget()

                        frame_4.grid_forget()

                        to_entry.delete(0,END)

                        from_entry.delete(0,END)

                        journey_date_entry.delete(0,END)

                        con.commit()
                        def funtion_ticket(ravi=0):
                            root.destroy()
                            self.Ticket()
                        funtion_ticket()
                        #root.destroy()

                        #import Bus_Ticket

                

                    showerror('Invalid Entry','Booking already exist or you may have entered wrong values\nPlease enter valid values...')

                    cname.delete(0,END)

                    cage.delete(0,END)

                    cseat.delete(0,END)

                    mno.delete(0,END)

                    gender.set("Select")

                

                

                con.commit()

                con.close()

                


            Label(frame5,text='Fill Passenger Details',fg='Red',bg='LightBlue1',font="Arial 21 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)

            frame5.grid(row=9,column=0,columnspan=10)

            Label(frame5,text="Name",font='Arial 11 bold').grid(row=1,column=0)

            cname=Entry(frame5)

            cname.grid(row=1,column=1)



            Label(frame5,text="Gender",font='Arial 11 bold').grid(row=1,column=2)

            gender=StringVar()

            gender.set("Select")

            option=["Male","Female","Other"]

            menu=OptionMenu(frame5,gender,*option)

            menu.grid(row=1,column=3)



            Label(frame5,text="Mobile No",font='Arial 11 bold').grid(row=1,column=4)

            mno=Entry(frame5)

            mno.grid(row=1,column=5)



            Label(frame5,text="Age",font='Arial 11 bold').grid(row=1,column=6)

            cage=Entry(frame5,width=10)

            cage.grid(row=1,column=7)



            Label(frame5,text="No Of Seats",font='Arial 11 bold').grid(row=1,column=8)

            cseat=Entry(frame5,width=10)

            cseat.grid(row=1,column=9)



            Button(frame5,text='Book Seat',fg="black",bg='white',font='Arial 15',command=confirm).grid(row=1,column=10,padx=10)




        def fun1_check_error():
            if len(to_entry.get())==0:
                showerror('Value Missing','Please Enter Destination')
            elif len(from_entry.get())==0:
                showerror('Value Missing','Please Enter From')
            elif len(journey_date_entry.get())==0:
                showerror('Value Missing','Please Enter Date')
            else:
                show_bus_details()

        img=PhotoImage(file=".\\Bus_for_project.png")
        Frame_1=Frame(root)
        Frame_1.grid(row=0,column=0,columnspan=10)
        Label(Frame_1,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame_2=Frame(root)
        Frame_2.grid(row=3,column=0,columnspan=10)
        title=Label(Frame_2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        title=Label(Frame_3,text="Enter Journey Details",fg="green",font="Arial 13 bold",bg="light green")
        title.grid(row=1,column=0,padx=w//2.5,columnspan=7)
        Label(root,text="").grid(row=6,column=0)

        to=Label(root,text="To")
        to.grid(row=7,column=0,sticky=E)
        to_entry=Entry(root)
        to_entry.grid(row=7,column=1,sticky=W,padx=20)

        from_=Label(root,text="From")
        from_.grid(row=7,column=1,sticky=E)
        from_entry=Entry(root)
        from_entry.grid(row=7,column=2,sticky=W,padx=20)

        journey_date=Label(root,text="Journey Date")
        journey_date.grid(row=7,column=3,sticky=E)
        journey_date_entry=Entry(root)
        journey_date_entry.grid(row=7,column=4,sticky=W,padx=20)

        Button(root,text="Show Bus",bg="light green",command=fun1_check_error).grid(row=7,column=5)
        def home(pravin=0):
            con.close()
            root.destroy()
            self.w2()
        img_1=PhotoImage(file=".\\home.png")
        Button(root,image=img_1,command=home).grid(row=7,column=6)
        root.mainloop()
         
#/.................................................................................................................................................................................

    def Ticket(self):
        con=sqlite3.Connection("database")
        cur=con.cursor()
        root=Tk()

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()

        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file='Bus_for_project.png')

        Frame1=Frame(root)

        Frame1.grid(row=0,column=0,columnspan=10,padx=w/2.5)

        Label(Frame1,image=img).pack()

        Label(Frame1,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold").pack()

            
        Label(Frame1,text='Bus Ticket',fg='black',font="Arial 15 bold",pady=5).pack()

        Frame2=Frame(root,relief='groove',bd=5)

        Frame2.grid(row=1,column=0,columnspan=10,padx=w/2.5,pady=10)

        #con.commit()

        cur.execute("SELECT count(*) FROM booking_history")

        lastid = cur.fetchall()

        cur.execute("SELECT * FROM booking_history where booking_id=:lastid",
                        {
                            'lastid': lastid[0][0]
                        }
                        )
        info = cur.fetchall()
        ac=(info[0][9])/info[0][10]
        for widget in Frame2.winfo_children():
            widget.destroy()
        Label(Frame2,text='Passenger Name : '+str(info[0][1]),font='Arial 13 bold').grid(row=0,column=0,sticky='w')

        Label(Frame2,text='No of seats : '+str(info[0][10]),font='Arial 13 bold').grid(row=1,column=0,sticky='w')

        Label(Frame2,text='age : '+str(info[0][6]),font='Arial 13 bold').grid(row=2,column=0,sticky='w')

        Label(Frame2,text='booking ref : '+str(info[0][0]),font='Arial 13 bold').grid(row=3,column=0,sticky='w')

        Label(Frame2,text='travel On : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

        Label(Frame2,text='gender : '+str(info[0][5]),font='Arial 13 bold').grid(row=0,column=1,sticky='w')

        Label(Frame2,text='phone number : '+str(info[0][2]),font='Arial 13 bold').grid(row=1,column=1,sticky='w')

        Label(Frame2,text='fare : '+str(ac),font='Arial 13 bold').grid(row=2,column=1,sticky='w')

        Label(Frame2,text='booked on '+str(info[0][4]),font='Arial 13 bold').grid(row=3,column=1,sticky='w')

        Label(Frame2,text='boarding point '+str(info[0][7]),font='Arial 13 bold').grid(row=4,column=1,sticky='w')

        #Label(Frame2,text='Phone : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

        Label(Frame2,text='* Total fare of '+str(info[0][9])+' /- to be paid at the time of boarding the bus',font='Arial 12 italic').grid(row=5,column=0,columnspan=10)
        def exitt():
            root.destroy()
        """def home():
            root.destroy()
            import Main_Menu"""
        Button(root,text='Exit',font='Times_new_roman 10',command=exitt).grid(row=7,column=1,columnspan=10)
        def home(pravin=0):
            con.close()
            root.destroy()
            self.w2()
        photu=PhotoImage(file="home.png")
        Button(root,image=photu,font='Times_new_roman 10',command=home).grid(row=7,column=0,columnspan=10)
        root.mainloop()
    





























 



        
t=Test()
t.w1()
