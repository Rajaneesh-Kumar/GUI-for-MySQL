### Computer Project###
###Session - 2021-2022###

#Project Name - GUI for MySQL

#Made by - Rajaneesh kumar

#Class - XII A1

#Roll no. - 23729103



import tkinter as tk
import mysql.connector as sql

root=tk.Tk()
root.title("Login Window")
root.geometry("900x500")
    


def connection():
    obj=sql.connect(host="localhost",user=e1.get(),passwd=e2.get(),database=e3.get())

    if obj.is_connected():
        l4=tk.Label(root,text="Successfully Connected")
        l4.grid(row=4,column=3)
        cursor=obj.cursor()


        ##Functions for showing the table contents
        def ctab1():

            #Function to insert row in a table
            def insert():
                def insert_row():
                    values=eval(evalue.get())
                    sql="INSERT INTO "+data[0][0]+" VALUES("
                    for i in values:
                        if str(type(i))== "<class 'str'>":
                            sql=sql+'"%s",'
                        else:
                            sql=sql+"%s,"
                    sql=sql[0:-1]
                    sql=sql+');'
                    cursor.execute(sql%(eval(evalue.get())))
                    obj.commit()
                    msg=tk.Label(winsert,text="Successfully Inserted",font=("Ubuntu Mono",15,"bold")).grid(row=3,column=2)
                    
                winsert=tk.Tk()
                winsert.focus_force()
                winsert.title("Insert row")
                lq=tk.Label(winsert,text="INSERT INTO "+data[0][0]+" VALUES (",font=("Ubuntu Mono",12)).grid(row=1,column=1)
                evalue=tk.Entry(winsert,width=30,font=("Ubuntu Mono",12))
                evalue.grid(row=1,column=2)
                lq1=tk.Label(winsert,text=" );",font=("Ubuntu Mono",12)).grid(row=1,column=3)
                insertb=tk.Button(winsert,text="Insert",font=("Ubuntu Mono",12),command=insert_row).grid(row=2,column=2)
                winsert.mainloop()

            def delete():
                delete_row=tk.Tk()
                delete_row.title("Delete row")
                delete_row.focus_force()
                lb1=tk.Label(delete_row,text="DELETE FROM "+data[0][0]+" \nWHERE ",font=("Ubuntu Mono",12)).grid(row=1,column=1)
                cln_name=tk.Entry(delete_row,font=("Ubuntu Mono",12))
                cln_name.grid(row=1,column=2)
                lb2=tk.Label(delete_row,text="=",font=("Ubuntu Mono",12)).grid(row=1,column=3)
                val1=tk.Entry(delete_row,font=("Ubuntu Mono",12))
                val1.grid(row=1,column=4)
                
                def delete_Button():
                    if str(type(eval(val1.get())))=="<class 'int'>":
                        
                        sql="delete from "+data[0][0]+" where "+cln_name.get()+" = %s;"
                        
                        cursor.execute(sql%(eval(val1.get()+",")))
                    else:
                        sql="delete from "+data[0][0]+" where "+cln_name.get()+" = '%s';"
                        cursor.execute(sql%(eval(val1.get()+",")))
                    
                    obj.commit()
                    msg=tk.Label(delete_row,text="Successfully Deleted",font=("Ubuntu Mono",15,"bold")).grid(row=3,column=1)

                bdel=tk.Button(delete_row,text="Delete",command=delete_Button).grid(row=2,column=2)
                
                delete_row.mainloop()

            def search():
                searchwin=tk.Tk()
                searchwin.focus_force()
                searchwin.title("Search row")
                lquery=tk.Label(searchwin,text="SELECT * FROM "+data[0][0],font=("Ubuntu Mono",12)).grid(row=1,column=1)
                lquery1=tk.Label(searchwin,text="WHERE",font=("Ubuntu Mono",12)).grid(row=2,column=1)
                cln=tk.Entry(searchwin,font=("Ubuntu Mono",12))
                cln.grid(row=2,column=2)
                lquery2=tk.Label(searchwin,text="=",font=("Ubuntu Mono",12)).grid(row=2,column=3)
                val=tk.Entry(searchwin,font=("Ubuntu Mono",12))
                val.grid(row=2,column=4)
                lquery3=tk.Label(searchwin,text=" ;",font=("Ubuntu Mono",12)).grid(row=2,column=5)
                def search_Button():
                    if str(type(eval(val.get())))=="<class 'int'>":
                        
                        sql="SELECT * FROM "+data[0][0]+" where "+cln.get()+" = %s;"
                        
                        cursor.execute(sql%(eval(val.get()+",")))
                    else:
                        sql="SELECT * FROM "+data[0][0]+" where "+cln.get()+" = '%s';"
                        cursor.execute(sql%(eval(val.get()+",")))

                    dat=""
                    for i in cursor.fetchall():
                        dat=dat+str(i)+"\n\n"
                    
                    head=tk.Label(searchwin,text=20*"="+"\nSearch Results",font=("Ubuntu Mono",15,"bold")).grid(row=4,column=1)
                    dat=tk.Label(searchwin,text=dat,font=("Ubuntu Mono",12)).grid(row=5,column=1)

                bs=tk.Button(searchwin,text="Search",font=("Ubuntu Mono",12),command=search_Button).grid(row=3,column=2)
                searchwin.mainloop()

            def update():
                updatewin=tk.Tk()
                updatewin.title("Update")
                updatewin.focus_force()
                queryl0=tk.Label(updatewin,text="UPDATE "+data[0][0],font=("Ubuntu Mono",12)).grid(row=1,column=1)
                queryl1=tk.Label(updatewin,text="SET ",font=("Ubuntu Mono",12)).grid(row=2,column=1)
                clnset=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                clnset.grid(row=2,column=2)
                queryl2=tk.Label(updatewin,text=" = ",font=("Ubuntu Mono",12)).grid(row=2,column=3)
                valset=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                valset.grid(row=2,column=4)
                queryl3=tk.Label(updatewin,text="WHERE ",font=("Ubuntu Mono",12)).grid(row=3,column=1)
                clnw=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                clnw.grid(row=3,column=2)
                queryl4=tk.Label(updatewin,text=" = ",font=("Ubuntu Mono",12)).grid(row=3,column=3)
                valw=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                valw.grid(row=3,column=4)
                queryl5=tk.Label(updatewin,text=" ;",font=("Ubuntu Mono",12)).grid(row=3,column=5)

                def update_button():
                    if str(type(eval(valset.get())))=="<class 'int'>":
                        
                        sql="UPDATE "+data[0][0]+" SET "+clnset.get()+" = %s "
                        
                    else:
                        sql="UPDATE "+data[0][0]+" SET "+clnset.get()+" = '%s' "



                    if str(type(eval(valw.get())))=="<class 'int'>":
                        
                        sql=sql+"where "+clnw.get()+" = %s;"
                        
                    else:
                        sql=sql+"where "+clnw.get()+" = '%s';"

                    cursor.execute(sql%(eval(valset.get()),eval(valw.get())))
                    obj.commit()
                    msg=tk.Label(updatewin,text="Successfully Updated",font=("Ubuntu Mono",12,"bold")).grid(row=5,column=1)

                update_button=tk.Button(updatewin,text="Update",font=("Ubuntu Mono",12),command=update_button).grid(row=4,column=2)

                updatewin.mainloop()

            dat=""
            cursor.execute("select * from "+data[0][0]+";")
            for i in cursor.fetchall():
                dat=dat+str(i)+"\n"+200*"-"+"\n"
            table=tk.Tk()
            table.focus_force()
            table.title("Contents of Table")
            binsert=tk.Button(table,text="Insert row",font=("Ubuntu Mono",12),command=insert).pack()
            bupdate=tk.Button(table,text="Update",font=("Ubuntu Mono",12),command=update).pack()
            bdelete=tk.Button(table,text="Delete row",font=("Ubuntu Mono",12),command=delete).pack()
            bsearch=tk.Button(table,text="Search",font=("Ubuntu Mono",12),command=search).pack()
            cln=tk.Label(table,text="\n"+str(cursor.column_names)+"\n"+30*"----+"+"\n",font=("HP Simplified",11))
            cln.pack()
            Labd=tk.Label(table,text=dat,font=("HP Simplified",11))
            Labd.pack()
            table.mainloop()

        def ctab2():
            #Function to insert row in a table
            def insert():
                def insert_row():
                    values=eval(evalue.get())
                    sql="INSERT INTO "+data[1][0]+" VALUES("
                    for i in values:
                        if str(type(i))== "<class 'str'>":
                            sql=sql+'"%s",'
                        else:
                            sql=sql+"%s,"
                    sql=sql[0:-1]
                    sql=sql+');'
                    cursor.execute(sql%(eval(evalue.get())))
                    obj.commit()
                    msg=tk.Label(winsert,text="Successfully Inserted",font=("Ubuntu Mono",15,"bold")).grid(row=3,column=2)
                    
                winsert=tk.Tk()
                winsert.focus_force()
                winsert.title("Insert row")
                lq=tk.Label(winsert,text="INSERT INTO "+data[1][0]+" VALUES (",font=("Ubuntu Mono",12)).grid(row=1,column=1)
                evalue=tk.Entry(winsert,width=30,font=("Ubuntu Mono",12))
                evalue.grid(row=1,column=2)
                lq1=tk.Label(winsert,text=" );",font=("Ubuntu Mono",12)).grid(row=1,column=3)
                insertb=tk.Button(winsert,text="Insert",font=("Ubuntu Mono",12),command=insert_row).grid(row=2,column=2)
                winsert.mainloop()

            def delete():
                delete_row=tk.Tk()
                delete_row.title("Delete row")
                delete_row.focus_force()
                lb1=tk.Label(delete_row,text="DELETE FROM "+data[1][0]+" \nWHERE ",font=("Ubuntu Mono",12)).grid(row=1,column=1)
                cln_name=tk.Entry(delete_row,font=("Ubuntu Mono",12))
                cln_name.grid(row=1,column=2)
                lb2=tk.Label(delete_row,text="=",font=("Ubuntu Mono",12)).grid(row=1,column=3)
                val1=tk.Entry(delete_row,font=("Ubuntu Mono",12))
                val1.grid(row=1,column=4)
                
                def delete_Button():
                    if str(type(eval(val1.get())))=="<class 'int'>":
                        
                        sql="delete from "+data[1][0]+" where "+cln_name.get()+" = %s;"
                        
                        cursor.execute(sql%(eval(val1.get()+",")))
                    else:
                        sql="delete from "+data[1][0]+" where "+cln_name.get()+" = '%s';"
                        cursor.execute(sql%(eval(val1.get()+",")))
                    
                    obj.commit()
                    msg=tk.Label(delete_row,text="Successfully Deleted",font=("Ubuntu Mono",15,"bold")).grid(row=3,column=1)

                bdel=tk.Button(delete_row,text="Delete",command=delete_Button).grid(row=2,column=2)
                
                delete_row.mainloop()

            def search():
                searchwin=tk.Tk()
                searchwin.focus_force()
                searchwin.title("Search row")
                lquery=tk.Label(searchwin,text="SELECT * FROM "+data[1][0],font=("Ubuntu Mono",12)).grid(row=1,column=1)
                lquery1=tk.Label(searchwin,text="WHERE",font=("Ubuntu Mono",12)).grid(row=2,column=1)
                cln=tk.Entry(searchwin,font=("Ubuntu Mono",12))
                cln.grid(row=2,column=2)
                lquery2=tk.Label(searchwin,text="=",font=("Ubuntu Mono",12)).grid(row=2,column=3)
                val=tk.Entry(searchwin,font=("Ubuntu Mono",12))
                val.grid(row=2,column=4)
                lquery3=tk.Label(searchwin,text=" ;",font=("Ubuntu Mono",12)).grid(row=2,column=5)
                def search_Button():
                    if str(type(eval(val.get())))=="<class 'int'>":
                        
                        sql="SELECT * FROM "+data[1][0]+" where "+cln.get()+" = %s;"
                        
                        cursor.execute(sql%(eval(val.get()+",")))
                    else:
                        sql="SELECT * FROM "+data[1][0]+" where "+cln.get()+" = '%s';"
                        cursor.execute(sql%(eval(val.get()+",")))

                    dat=""
                    for i in cursor.fetchall():
                        dat=dat+str(i)+"\n\n"
                    
                    head=tk.Label(searchwin,text=20*"="+"\nSearch Results",font=("Ubuntu Mono",15,"bold")).grid(row=4,column=1)
                    dat=tk.Label(searchwin,text=dat,font=("Ubuntu Mono",12)).grid(row=5,column=1)

                bs=tk.Button(searchwin,text="Search",font=("Ubuntu Mono",12),command=search_Button).grid(row=3,column=2)
                searchwin.mainloop()

            def update():
                updatewin=tk.Tk()
                updatewin.title("Update")
                updatewin.focus_force()
                queryl0=tk.Label(updatewin,text="UPDATE "+data[1][0],font=("Ubuntu Mono",12)).grid(row=1,column=1)
                queryl1=tk.Label(updatewin,text="SET ",font=("Ubuntu Mono",12)).grid(row=2,column=1)
                clnset=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                clnset.grid(row=2,column=2)
                queryl2=tk.Label(updatewin,text=" = ",font=("Ubuntu Mono",12)).grid(row=2,column=3)
                valset=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                valset.grid(row=2,column=4)
                queryl3=tk.Label(updatewin,text="WHERE ",font=("Ubuntu Mono",12)).grid(row=3,column=1)
                clnw=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                clnw.grid(row=3,column=2)
                queryl4=tk.Label(updatewin,text=" = ",font=("Ubuntu Mono",12)).grid(row=3,column=3)
                valw=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                valw.grid(row=3,column=4)
                queryl5=tk.Label(updatewin,text=" ;",font=("Ubuntu Mono",12)).grid(row=3,column=5)

                def update_button():
                    if str(type(eval(valset.get())))=="<class 'int'>":
                        
                        sql="UPDATE "+data[1][0]+" SET "+clnset.get()+" = %s "
                        
                    else:
                        sql="UPDATE "+data[1][0]+" SET "+clnset.get()+" = '%s' "



                    if str(type(eval(valw.get())))=="<class 'int'>":
                        
                        sql=sql+"where "+clnw.get()+" = %s;"
                        
                    else:
                        sql=sql+"where "+clnw.get()+" = '%s';"

                    cursor.execute(sql%(eval(valset.get()),eval(valw.get())))
                    obj.commit()
                    msg=tk.Label(updatewin,text="Successfully Updated",font=("Ubuntu Mono",12,"bold")).grid(row=5,column=1)

                update_button=tk.Button(updatewin,text="Update",font=("Ubuntu Mono",12),command=update_button).grid(row=4,column=2)

                updatewin.mainloop()

            dat=""
            cursor.execute("select * from "+data[1][0]+";")
            for i in cursor.fetchall():
                dat=dat+str(i)+"\n"+200*"-"+"\n"
            table=tk.Tk()
            table.focus_force()
            table.title("Contents of Table")
            binsert=tk.Button(table,text="Insert row",font=("Ubuntu Mono",12),command=insert).pack()
            bupdate=tk.Button(table,text="Update",font=("Ubuntu Mono",12),command=update).pack()
            bdelete=tk.Button(table,text="Delete row",font=("Ubuntu Mono",12),command=delete).pack()
            bsearch=tk.Button(table,text="Search",font=("Ubuntu Mono",12),command=search).pack()
            cln=tk.Label(table,text="\n"+str(cursor.column_names)+"\n"+30*"----+"+"\n",font=("HP Simplified",11))
            cln.pack()
            Labd=tk.Label(table,text=dat,font=("HP Simplified",11))
            Labd.pack()
            table.mainloop()


        def ctab3():
            #Function to insert row in a table
            def insert():
                def insert_row():
                    values=eval(evalue.get())
                    sql="INSERT INTO "+data[2][0]+" VALUES("
                    for i in values:
                        if str(type(i))== "<class 'str'>":
                            sql=sql+'"%s",'
                        else:
                            sql=sql+"%s,"
                    sql=sql[0:-1]
                    sql=sql+');'
                    cursor.execute(sql%(eval(evalue.get())))
                    obj.commit()
                    msg=tk.Label(winsert,text="Successfully Inserted",font=("Ubuntu Mono",15,"bold")).grid(row=3,column=2)
                    
                winsert=tk.Tk()
                winsert.focus_force()
                winsert.title("Insert row")
                lq=tk.Label(winsert,text="INSERT INTO "+data[2][0]+" VALUES (",font=("Ubuntu Mono",12)).grid(row=1,column=1)
                evalue=tk.Entry(winsert,width=30,font=("Ubuntu Mono",12))
                evalue.grid(row=1,column=2)
                lq1=tk.Label(winsert,text=" );",font=("Ubuntu Mono",12)).grid(row=1,column=3)
                insertb=tk.Button(winsert,text="Insert",font=("Ubuntu Mono",12),command=insert_row).grid(row=2,column=2)
                winsert.mainloop()

            def delete():
                delete_row=tk.Tk()
                delete_row.title("Delete row")
                delete_row.focus_force()
                lb1=tk.Label(delete_row,text="DELETE FROM "+data[2][0]+" \nWHERE ",font=("Ubuntu Mono",12)).grid(row=1,column=1)
                cln_name=tk.Entry(delete_row,font=("Ubuntu Mono",12))
                cln_name.grid(row=1,column=2)
                lb2=tk.Label(delete_row,text="=",font=("Ubuntu Mono",12)).grid(row=1,column=3)
                val1=tk.Entry(delete_row,font=("Ubuntu Mono",12))
                val1.grid(row=1,column=4)
                
                def delete_Button():
                    if str(type(eval(val1.get())))=="<class 'int'>":
                        
                        sql="delete from "+data[2][0]+" where "+cln_name.get()+" = %s;"
                        
                        cursor.execute(sql%(eval(val1.get()+",")))
                    else:
                        sql="delete from "+data[2][0]+" where "+cln_name.get()+" = '%s';"
                        cursor.execute(sql%(eval(val1.get()+",")))
                    
                    obj.commit()
                    msg=tk.Label(delete_row,text="Successfully Deleted",font=("Ubuntu Mono",15,"bold")).grid(row=3,column=1)

                bdel=tk.Button(delete_row,text="Delete",command=delete_Button).grid(row=2,column=2)
                
                delete_row.mainloop()

            def search():
                searchwin=tk.Tk()
                searchwin.focus_force()
                searchwin.title("Search row")
                lquery=tk.Label(searchwin,text="SELECT * FROM "+data[2][0],font=("Ubuntu Mono",12)).grid(row=1,column=1)
                lquery1=tk.Label(searchwin,text="WHERE",font=("Ubuntu Mono",12)).grid(row=2,column=1)
                cln=tk.Entry(searchwin,font=("Ubuntu Mono",12))
                cln.grid(row=2,column=2)
                lquery2=tk.Label(searchwin,text="=",font=("Ubuntu Mono",12)).grid(row=2,column=3)
                val=tk.Entry(searchwin,font=("Ubuntu Mono",12))
                val.grid(row=2,column=4)
                lquery3=tk.Label(searchwin,text=" ;",font=("Ubuntu Mono",12)).grid(row=2,column=5)
                def search_Button():
                    if str(type(eval(val.get())))=="<class 'int'>":
                        
                        sql="SELECT * FROM "+data[2][0]+" where "+cln.get()+" = %s;"
                        
                        cursor.execute(sql%(eval(val.get()+",")))
                    else:
                        sql="SELECT * FROM "+data[2][0]+" where "+cln.get()+" = '%s';"
                        cursor.execute(sql%(eval(val.get()+",")))

                    dat=""
                    for i in cursor.fetchall():
                        dat=dat+str(i)+"\n\n"
                    
                    head=tk.Label(searchwin,text=20*"="+"\nSearch Results",font=("Ubuntu Mono",15,"bold")).grid(row=4,column=1)
                    dat=tk.Label(searchwin,text=dat,font=("Ubuntu Mono",12)).grid(row=5,column=1)

                bs=tk.Button(searchwin,text="Search",font=("Ubuntu Mono",12),command=search_Button).grid(row=3,column=2)
                searchwin.mainloop()

            def update():
                updatewin=tk.Tk()
                updatewin.title("Update")
                updatewin.focus_force()
                queryl0=tk.Label(updatewin,text="UPDATE "+data[2][0],font=("Ubuntu Mono",12)).grid(row=1,column=1)
                queryl1=tk.Label(updatewin,text="SET ",font=("Ubuntu Mono",12)).grid(row=2,column=1)
                clnset=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                clnset.grid(row=2,column=2)
                queryl2=tk.Label(updatewin,text=" = ",font=("Ubuntu Mono",12)).grid(row=2,column=3)
                valset=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                valset.grid(row=2,column=4)
                queryl3=tk.Label(updatewin,text="WHERE ",font=("Ubuntu Mono",12)).grid(row=3,column=1)
                clnw=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                clnw.grid(row=3,column=2)
                queryl4=tk.Label(updatewin,text=" = ",font=("Ubuntu Mono",12)).grid(row=3,column=3)
                valw=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                valw.grid(row=3,column=4)
                queryl5=tk.Label(updatewin,text=" ;",font=("Ubuntu Mono",12)).grid(row=3,column=5)

                def update_button():
                    if str(type(eval(valset.get())))=="<class 'int'>":
                        
                        sql="UPDATE "+data[2][0]+" SET "+clnset.get()+" = %s "
                        
                    else:
                        sql="UPDATE "+data[2][0]+" SET "+clnset.get()+" = '%s' "



                    if str(type(eval(valw.get())))=="<class 'int'>":
                        
                        sql=sql+"where "+clnw.get()+" = %s;"
                        
                    else:
                        sql=sql+"where "+clnw.get()+" = '%s';"

                    cursor.execute(sql%(eval(valset.get()),eval(valw.get())))
                    obj.commit()
                    msg=tk.Label(updatewin,text="Successfully Updated",font=("Ubuntu Mono",12,"bold")).grid(row=5,column=1)

                update_button=tk.Button(updatewin,text="Update",font=("Ubuntu Mono",12),command=update_button).grid(row=4,column=2)

                updatewin.mainloop()

            dat=""
            cursor.execute("select * from "+data[2][0]+";")
            for i in cursor.fetchall():
                dat=dat+str(i)+"\n"+200*"-"+"\n"
            table=tk.Tk()
            table.focus_force()
            table.title("Contents of Table")
            binsert=tk.Button(table,text="Insert row",font=("Ubuntu Mono",12),command=insert).pack()
            bupdate=tk.Button(table,text="Update",font=("Ubuntu Mono",12),command=update).pack()
            bdelete=tk.Button(table,text="Delete row",font=("Ubuntu Mono",12),command=delete).pack()
            bsearch=tk.Button(table,text="Search",font=("Ubuntu Mono",12),command=search).pack()
            cln=tk.Label(table,text="\n"+str(cursor.column_names)+"\n"+30*"----+"+"\n",font=("HP Simplified",11))
            cln.pack()
            Labd=tk.Label(table,text=dat,font=("HP Simplified",11))
            Labd.pack()
            table.mainloop()


        def ctab4():
            #Function to insert row in a table
            def insert():
                def insert_row():
                    values=eval(evalue.get())
                    sql="INSERT INTO "+data[3][0]+" VALUES("
                    for i in values:
                        if str(type(i))== "<class 'str'>":
                            sql=sql+'"%s",'
                        else:
                            sql=sql+"%s,"
                    sql=sql[0:-1]
                    sql=sql+');'
                    cursor.execute(sql%(eval(evalue.get())))
                    obj.commit()
                    msg=tk.Label(winsert,text="Successfully Inserted",font=("Ubuntu Mono",15,"bold")).grid(row=3,column=2)
                    
                winsert=tk.Tk()
                winsert.focus_force()
                winsert.title("Insert row")
                lq=tk.Label(winsert,text="INSERT INTO "+data[3][0]+" VALUES (",font=("Ubuntu Mono",12)).grid(row=1,column=1)
                evalue=tk.Entry(winsert,width=30,font=("Ubuntu Mono",12))
                evalue.grid(row=1,column=2)
                lq1=tk.Label(winsert,text=" );",font=("Ubuntu Mono",12)).grid(row=1,column=3)
                insertb=tk.Button(winsert,text="Insert",font=("Ubuntu Mono",12),command=insert_row).grid(row=2,column=2)
                winsert.mainloop()

            def delete():
                delete_row=tk.Tk()
                delete_row.title("Delete row")
                delete_row.focus_force()
                lb1=tk.Label(delete_row,text="DELETE FROM "+data[3][0]+" \nWHERE ",font=("Ubuntu Mono",12)).grid(row=1,column=1)
                cln_name=tk.Entry(delete_row,font=("Ubuntu Mono",12))
                cln_name.grid(row=1,column=2)
                lb2=tk.Label(delete_row,text="=",font=("Ubuntu Mono",12)).grid(row=1,column=3)
                val1=tk.Entry(delete_row,font=("Ubuntu Mono",12))
                val1.grid(row=1,column=4)
                
                def delete_Button():
                    if str(type(eval(val1.get())))=="<class 'int'>":
                        
                        sql="delete from "+data[3][0]+" where "+cln_name.get()+" = %s;"
                        
                        cursor.execute(sql%(eval(val1.get()+",")))
                    else:
                        sql="delete from "+data[3][0]+" where "+cln_name.get()+" = '%s';"
                        cursor.execute(sql%(eval(val1.get()+",")))
                    
                    obj.commit()
                    msg=tk.Label(delete_row,text="Successfully Deleted",font=("Ubuntu Mono",15,"bold")).grid(row=3,column=1)

                bdel=tk.Button(delete_row,text="Delete",command=delete_Button).grid(row=2,column=2)
                
                delete_row.mainloop()

            def search():
                searchwin=tk.Tk()
                searchwin.focus_force()
                searchwin.title("Search row")
                lquery=tk.Label(searchwin,text="SELECT * FROM "+data[3][0],font=("Ubuntu Mono",12)).grid(row=1,column=1)
                lquery1=tk.Label(searchwin,text="WHERE",font=("Ubuntu Mono",12)).grid(row=2,column=1)
                cln=tk.Entry(searchwin,font=("Ubuntu Mono",12))
                cln.grid(row=2,column=2)
                lquery2=tk.Label(searchwin,text="=",font=("Ubuntu Mono",12)).grid(row=2,column=3)
                val=tk.Entry(searchwin,font=("Ubuntu Mono",12))
                val.grid(row=2,column=4)
                lquery3=tk.Label(searchwin,text=" ;",font=("Ubuntu Mono",12)).grid(row=2,column=5)
                def search_Button():
                    if str(type(eval(val.get())))=="<class 'int'>":
                        
                        sql="SELECT * FROM "+data[3][0]+" where "+cln.get()+" = %s;"
                        
                        cursor.execute(sql%(eval(val.get()+",")))
                    else:
                        sql="SELECT * FROM "+data[3][0]+" where "+cln.get()+" = '%s';"
                        cursor.execute(sql%(eval(val.get()+",")))

                    dat=""
                    for i in cursor.fetchall():
                        dat=dat+str(i)+"\n\n"
                    
                    head=tk.Label(searchwin,text=20*"="+"\nSearch Results",font=("Ubuntu Mono",15,"bold")).grid(row=4,column=1)
                    dat=tk.Label(searchwin,text=dat,font=("Ubuntu Mono",12)).grid(row=5,column=1)

                bs=tk.Button(searchwin,text="Search",font=("Ubuntu Mono",12),command=search_Button).grid(row=3,column=2)
                searchwin.mainloop()

            def update():
                updatewin=tk.Tk()
                updatewin.title("Update")
                updatewin.focus_force()
                queryl0=tk.Label(updatewin,text="UPDATE "+data[3][0],font=("Ubuntu Mono",12)).grid(row=1,column=1)
                queryl1=tk.Label(updatewin,text="SET ",font=("Ubuntu Mono",12)).grid(row=2,column=1)
                clnset=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                clnset.grid(row=2,column=2)
                queryl2=tk.Label(updatewin,text=" = ",font=("Ubuntu Mono",12)).grid(row=2,column=3)
                valset=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                valset.grid(row=2,column=4)
                queryl3=tk.Label(updatewin,text="WHERE ",font=("Ubuntu Mono",12)).grid(row=3,column=1)
                clnw=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                clnw.grid(row=3,column=2)
                queryl4=tk.Label(updatewin,text=" = ",font=("Ubuntu Mono",12)).grid(row=3,column=3)
                valw=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                valw.grid(row=3,column=4)
                queryl5=tk.Label(updatewin,text=" ;",font=("Ubuntu Mono",12)).grid(row=3,column=5)

                def update_button():
                    if str(type(eval(valset.get())))=="<class 'int'>":
                        
                        sql="UPDATE "+data[3][0]+" SET "+clnset.get()+" = %s "
                        
                    else:
                        sql="UPDATE "+data[3][0]+" SET "+clnset.get()+" = '%s' "



                    if str(type(eval(valw.get())))=="<class 'int'>":
                        
                        sql=sql+"where "+clnw.get()+" = %s;"
                        
                    else:
                        sql=sql+"where "+clnw.get()+" = '%s';"

                    cursor.execute(sql%(eval(valset.get()),eval(valw.get())))
                    obj.commit()
                    msg=tk.Label(updatewin,text="Successfully Updated",font=("Ubuntu Mono",12,"bold")).grid(row=5,column=1)

                update_button=tk.Button(updatewin,text="Update",font=("Ubuntu Mono",12),command=update_button).grid(row=4,column=2)

                updatewin.mainloop()

            dat=""
            cursor.execute("select * from "+data[3][0]+";")
            for i in cursor.fetchall():
                dat=dat+str(i)+"\n"+200*"-"+"\n"
            table=tk.Tk()
            table.focus_force()
            table.title("Contents of Table")
            binsert=tk.Button(table,text="Insert row",font=("Ubuntu Mono",12),command=insert).pack()
            bupdate=tk.Button(table,text="Update",font=("Ubuntu Mono",12),command=update).pack()
            bdelete=tk.Button(table,text="Delete row",font=("Ubuntu Mono",12),command=delete).pack()
            bsearch=tk.Button(table,text="Search",font=("Ubuntu Mono",12),command=search).pack()
            cln=tk.Label(table,text="\n"+str(cursor.column_names)+"\n"+30*"----+"+"\n",font=("HP Simplified",11))
            cln.pack()
            Labd=tk.Label(table,text=dat,font=("HP Simplified",11))
            Labd.pack()
            table.mainloop()

        def ctab5():
            #Function to insert row in a table
            def insert():
                def insert_row():
                    values=eval(evalue.get())
                    sql="INSERT INTO "+data[4][0]+" VALUES("
                    for i in values:
                        if str(type(i))== "<class 'str'>":
                            sql=sql+'"%s",'
                        else:
                            sql=sql+"%s,"
                    sql=sql[0:-1]
                    sql=sql+');'
                    cursor.execute(sql%(eval(evalue.get())))
                    obj.commit()
                    msg=tk.Label(winsert,text="Successfully Inserted",font=("Ubuntu Mono",15,"bold")).grid(row=3,column=2)
                    
                winsert=tk.Tk()
                winsert.focus_force()
                winsert.title("Insert row")
                lq=tk.Label(winsert,text="INSERT INTO "+data[4][0]+" VALUES (",font=("Ubuntu Mono",12)).grid(row=1,column=1)
                evalue=tk.Entry(winsert,width=30,font=("Ubuntu Mono",12))
                evalue.grid(row=1,column=2)
                lq1=tk.Label(winsert,text=" );",font=("Ubuntu Mono",12)).grid(row=1,column=3)
                insertb=tk.Button(winsert,text="Insert",font=("Ubuntu Mono",12),command=insert_row).grid(row=2,column=2)
                winsert.mainloop()

            def delete():
                delete_row=tk.Tk()
                delete_row.title("Delete row")
                delete_row.focus_force()
                lb1=tk.Label(delete_row,text="DELETE FROM "+data[4][0]+" \nWHERE ",font=("Ubuntu Mono",12)).grid(row=1,column=1)
                cln_name=tk.Entry(delete_row,font=("Ubuntu Mono",12))
                cln_name.grid(row=1,column=2)
                lb2=tk.Label(delete_row,text="=",font=("Ubuntu Mono",12)).grid(row=1,column=3)
                val1=tk.Entry(delete_row,font=("Ubuntu Mono",12))
                val1.grid(row=1,column=4)
                
                def delete_Button():
                    if str(type(eval(val1.get())))=="<class 'int'>":
                        
                        sql="delete from "+data[4][0]+" where "+cln_name.get()+" = %s;"
                        
                        cursor.execute(sql%(eval(val1.get()+",")))
                    else:
                        sql="delete from "+data[4][0]+" where "+cln_name.get()+" = '%s';"
                        cursor.execute(sql%(eval(val1.get()+",")))
                    
                    obj.commit()
                    msg=tk.Label(delete_row,text="Successfully Deleted",font=("Ubuntu Mono",15,"bold")).grid(row=3,column=1)

                bdel=tk.Button(delete_row,text="Delete",command=delete_Button).grid(row=2,column=2)
                
                delete_row.mainloop()

            def search():
                searchwin=tk.Tk()
                searchwin.focus_force()
                searchwin.title("Search row")
                lquery=tk.Label(searchwin,text="SELECT * FROM "+data[4][0],font=("Ubuntu Mono",12)).grid(row=1,column=1)
                lquery1=tk.Label(searchwin,text="WHERE",font=("Ubuntu Mono",12)).grid(row=2,column=1)
                cln=tk.Entry(searchwin,font=("Ubuntu Mono",12))
                cln.grid(row=2,column=2)
                lquery2=tk.Label(searchwin,text="=",font=("Ubuntu Mono",12)).grid(row=2,column=3)
                val=tk.Entry(searchwin,font=("Ubuntu Mono",12))
                val.grid(row=2,column=4)
                lquery3=tk.Label(searchwin,text=" ;",font=("Ubuntu Mono",12)).grid(row=2,column=5)
                def search_Button():
                    if str(type(eval(val.get())))=="<class 'int'>":
                        
                        sql="SELECT * FROM "+data[4][0]+" where "+cln.get()+" = %s;"
                        
                        cursor.execute(sql%(eval(val.get()+",")))
                    else:
                        sql="SELECT * FROM "+data[4][0]+" where "+cln.get()+" = '%s';"
                        cursor.execute(sql%(eval(val.get()+",")))

                    dat=""
                    for i in cursor.fetchall():
                        dat=dat+str(i)+"\n\n"
                    
                    head=tk.Label(searchwin,text=20*"="+"\nSearch Results",font=("Ubuntu Mono",15,"bold")).grid(row=4,column=1)
                    dat=tk.Label(searchwin,text=dat,font=("Ubuntu Mono",12)).grid(row=5,column=1)

                bs=tk.Button(searchwin,text="Search",font=("Ubuntu Mono",12),command=search_Button).grid(row=3,column=2)
                searchwin.mainloop()

            def update():
                updatewin=tk.Tk()
                updatewin.title("Update")
                updatewin.focus_force()
                queryl0=tk.Label(updatewin,text="UPDATE "+data[4][0],font=("Ubuntu Mono",12)).grid(row=1,column=1)
                queryl1=tk.Label(updatewin,text="SET ",font=("Ubuntu Mono",12)).grid(row=2,column=1)
                clnset=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                clnset.grid(row=2,column=2)
                queryl2=tk.Label(updatewin,text=" = ",font=("Ubuntu Mono",12)).grid(row=2,column=3)
                valset=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                valset.grid(row=2,column=4)
                queryl3=tk.Label(updatewin,text="WHERE ",font=("Ubuntu Mono",12)).grid(row=3,column=1)
                clnw=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                clnw.grid(row=3,column=2)
                queryl4=tk.Label(updatewin,text=" = ",font=("Ubuntu Mono",12)).grid(row=3,column=3)
                valw=tk.Entry(updatewin,font=("Ubuntu Mono",12))
                valw.grid(row=3,column=4)
                queryl5=tk.Label(updatewin,text=" ;",font=("Ubuntu Mono",12)).grid(row=3,column=5)

                def update_button():
                    if str(type(eval(valset.get())))=="<class 'int'>":
                        
                        sql="UPDATE "+data[4][0]+" SET "+clnset.get()+" = %s "
                        
                    else:
                        sql="UPDATE "+data[4][0]+" SET "+clnset.get()+" = '%s' "



                    if str(type(eval(valw.get())))=="<class 'int'>":
                        
                        sql=sql+"where "+clnw.get()+" = %s;"
                        
                    else:
                        sql=sql+"where "+clnw.get()+" = '%s';"

                    cursor.execute(sql%(eval(valset.get()),eval(valw.get())))
                    obj.commit()
                    msg=tk.Label(updatewin,text="Successfully Updated",font=("Ubuntu Mono",12,"bold")).grid(row=5,column=1)

                update_button=tk.Button(updatewin,text="Update",font=("Ubuntu Mono",12),command=update_button).grid(row=4,column=2)

                updatewin.mainloop()

            dat=""
            cursor.execute("select * from "+data[4][0]+";")
            for i in cursor.fetchall():
                dat=dat+str(i)+"\n"+200*"-"+"\n"
            table=tk.Tk()
            table.focus_force()
            table.title("Contents of Table")
            binsert=tk.Button(table,text="Insert row",font=("Ubuntu Mono",12),command=insert).pack()
            bupdate=tk.Button(table,text="Update",font=("Ubuntu Mono",12),command=update).pack()
            bdelete=tk.Button(table,text="Delete row",font=("Ubuntu Mono",12),command=delete).pack()
            bsearch=tk.Button(table,text="Search",font=("Ubuntu Mono",12),command=search).pack()
            cln=tk.Label(table,text="\n"+str(cursor.column_names)+"\n"+30*"----+"+"\n",font=("HP Simplified",11))
            cln.pack()
            Labd=tk.Label(table,text=dat,font=("HP Simplified",11))
            Labd.pack()
            table.mainloop()


        cursor.execute("Show tables;")
        data=cursor.fetchall()

        ## Window for showing the list of Tables
        boot=tk.Tk()
        boot.focus_force()
        boot.title("List of Tables")
        boot.geometry("500x400")
        lab1=tk.Label(boot,text="List of Tables : ",font=("HP Simplified",15))
        lab1.pack()
        gap0=tk.Label(boot,text="---------------------")
        gap0.pack()
        tab1=tk.Button(boot,text=data[0][0],command=ctab1,font=("HP Simplified",15))
        tab1.pack()
        gap1=tk.Label(boot,text="---------------------")
        gap1.pack()
        tab2=tk.Button(boot,text=data[1][0],command=ctab2,font=("HP Simplified",15))
        tab2.pack()
        gap2=tk.Label(boot,text="---------------------")
        gap2.pack()
        tab3=tk.Button(boot,text=data[2][0],command=ctab3,font=("HP Simplified",15))
        tab3.pack()
        gap3=tk.Label(boot,text="---------------------")
        gap3.pack()
        tab4=tk.Button(boot,text=data[3][0],command=ctab4,font=("HP Simplified",15))
        tab4.pack()
        gap4=tk.Label(boot,text="---------------------")
        gap4.pack()
        tab5=tk.Button(boot,text=data[4][0],command=ctab5,font=("HP Simplified",15))
        tab5.pack()

        boot.mainloop()
        obj.close()

    else:
       l4=tk.Label(root,text="Failed to Connect",font=("HP Simplified",15))
       l4.grid(row=3,column=3)

def execute():
    dat=""
    obj=sql.connect(host="localhost",user="root",passwd="HP 245G5",database=e3.get())
    cursor=obj.cursor()
    values=(eval(val.get()))
    cursor.execute(cmd.get()%(eval(val.get())))
    for i in cursor.fetchall():
        dat=dat+str(i)+"\n\n"
    table=tk.Tk()
    table.focus_force()
    table.title("Command Output")
    cln=tk.Label(table,text=str(cursor.column_names)+"\n",font=("HP Simplified",15))
    cln.pack()
    Labd=tk.Label(table,text=dat,font=("HP Simplified",15))
    Labd.pack()
    msg=tk.Label(table,text="Successfully Executed",font=("HP Simplified",15))
    msg.pack()
    table.mainloop()
    obj.close()

def commitexe():
    dat=""
    obj=sql.connect(host="localhost",user="root",passwd="HP 245G5",database=e3.get())
    cursor=obj.cursor()
    values=(eval(val.get()))
    cursor.execute(cmd.get()%(eval(val.get())))
    obj.commit()
    for i in cursor.fetchall():
        dat=dat+str(i)+"\n\n"
    table=tk.Tk()
    table.focus_force()
    table.title("Command Output")
    cln=tk.Label(table,text=str(cursor.column_names)+"\n",font=("HP Simplified",15))
    cln.pack()
    Labd=tk.Label(table,text=dat,font=("HP Simplified",15))
    Labd.pack()
    msg=tk.Label(table,text="Successfully Executed",font=("HP Simplified",15))
    msg.pack()
    table.mainloop()
    obj.close()
    

#Login Window_-_-_-
heading=tk.Label(root,text="GUI",font=("Shrikhand",60)).grid(row=1,column=1)
heading1=tk.Label(root,text="for",font=("Shrikhand",60)).place(x=320,y=3)
heading2=tk.Label(root,text="MySQL",font=("Shrikhand",60)).place(x=500,y=3)

l1=tk.Label(root,text="Enter Username: ",font=("HP Simplified",15))
l1.grid(row=2,column=1)
e1=tk.Entry(root,font=("HP Simplified",15))
e1.grid(row=2,column=2)
l2=tk.Label(root,text="Enter Password: ",font=("HP Simplified",15))
l2.grid(row=3,column=1)
e2=tk.Entry(root,font=("HP Simplified",15))
e2.grid(row=3,column=2)
l3=tk.Label(root,text="Enter Database: ",font=("HP Simplified",15))
l3.grid(row=4,column=1)
e3=tk.Entry(root,font=("HP Simplified",15))
e3.grid(row=4,column=2)
b1=tk.Button(root,text="Connect and show tables",command=connection,font=("HP Simplified",15))
b1.grid(row=3,column=3)

border=tk.Label(root,text="\n\n===============================\n\n",font=("HP Simplified",15)).grid(row=5,column=1)

lcmd=tk.Label(root,text="Enter your command here :",font=("Ubuntu Mono",12))
lcmd.grid(row=6,column=1)
cmd=tk.Entry(root,font=("Ubuntu Mono",12),width=40)
cmd.grid(row=7,column=1)
lval=tk.Label(root,text="Enter your values here :",font=("Ubuntu Mono",12))
lval.grid(row=8,column=1)
val=tk.Entry(root,font=("Ubuntu Mono",12),width=40)
val.grid(row=9,column=1)
exe=tk.Button(root,text="Execute",command=execute,font=("Ubuntu Mono",12))
exe.grid(row=7,column=2)
execommit=tk.Button(root,text="Execute with commit function",command=commitexe,font=("Ubuntu Mono",12))
execommit.grid(row=9,column=2)

credit=tk.Label(root,text="Project by :-\nRajaneesh Kumar",font=("Times New Roman",11)).place(x=760,y=430)

root.mainloop()
