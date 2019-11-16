import tkinter as tk
from tkinter import messagebox
import prims ,kurskal ,dijkstra,FloydWarshall,bellmanford,parser_1,plotting
from functools import partial
result = 0
node_x_y = 0
from_to_cost = 0
no_of_nodes = 0
source = 0
    


def readFileName():
    try :
        f = open("benchmark\\"+str(e1.get())+".txt", "r")
        f.close()
        button2.grid(row=2)
        button3.grid(row=3)
        button4.grid(row=4)
        button5.grid(row=5)
        button6.grid(row=6)
        button7.grid(row=7)
        global result 
        global node_x_y 
        global from_to_cost 
        global no_of_nodes 
        global source 

        result = parser_1.PARSER(e1.get())
        result = result + (0.0,) + ('Simple Graph',)
        node_x_y = result[0]
        from_to_cost = result [1]
        no_of_nodes = result[2]
        source = result[3]
    except(FileNotFoundError):
        print('Not Found')
        button2.grid_forget()
        button3.grid_forget()
        button4.grid_forget()
        button5.grid_forget()
        button6.grid_forget()
        button7.grid_forget()
        messagebox.showerror("File Error", "File Not Found")
    
    
def buttonpress(function, *args):
    result = (node_x_y,)
    result = result + function(*args)
    result = result[ : 2 ] + (no_of_nodes ,) + (source,)+ result[2 : ]
    print(result)
    plotting.PLOTTING(result)

def PLOTTING():
    plotting.PLOTTING(result)


root = tk.Tk()
root.title("Shortest Path Algorithm")
tk.Label(root, text="Enter file name").grid(row=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
button1 = tk.Button(root, text='Submit' ,width=25, command=readFileName)
button1.grid(row=1)
button2 = tk.Button(root, text='PLOT' ,width=25, command=PLOTTING)
button3 = tk.Button(root, text='PRIMS' ,width=25, command=lambda: buttonpress( prims.PRIMS,from_to_cost,no_of_nodes ))
button4 = tk.Button(root, text='KURSKAL', width=25, command=lambda: buttonpress(kurskal.KURSKAL,from_to_cost,no_of_nodes))
button5 = tk.Button(root, text='DIJKSTRA', width=25, command=lambda: buttonpress(dijkstra.DIJKSTRA,from_to_cost,no_of_nodes,source))
button6 = tk.Button(root, text='FLOYD WARSHALL', width=25, command=lambda: buttonpress(FloydWarshall.FLOYDWARSHALL,from_to_cost,no_of_nodes,source,node_x_y))
button7 = tk.Button(root, text='BELLMAN FORD', width=25, command=lambda: buttonpress(bellmanford.BELLMANFORD,from_to_cost,no_of_nodes,source))


root.mainloop()