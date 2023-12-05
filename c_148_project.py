from tkinter import*
import random

root = Tk()
root.geometry("600x200")
root.title("In_MY_Bag")
root.configure(background = "snow")

list_item = ["phone","choclates","headphone","laptop","books","tiffin"]
label_items = Label(root,bg="snow",fg = "black")
label_items["text"] = "names of the object:"+str(list_item)
label_items.place(rely = 0.4,relx = 0.5,anchor= CENTER)
label_show  = Label(root,bg="snow",fg = "black")
def value_show():
    random_list = random.randint(0,5)
    index_list = list_item[random_list]
    label_show["text"]="keep object No."+str(random_list)+" "+str(index_list)+" in the bag"

btn  = Button(root,text="see the lugage",bg ="yellow",fg = "black",command= value_show)
label_show.place(rely = 0.8,relx = 0.5,anchor= CENTER)
btn.place(rely = 0.6,relx = 0.5,anchor= CENTER)
root.mainloop()