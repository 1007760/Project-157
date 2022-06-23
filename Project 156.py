from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("500x500")
root.title("Pokemon")
root.configure(background = "pink")
power_pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))
player1 = Label(root, text = "Player 1", bg = "red", fg = "blue")
player2 = Label(root, text = "Player 2", bg = "yellow", fg = "purple")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)
player1score = Label(root, bg = "red", fg = "yellow")
player2score = Label(root, bg = "blue", fg = "green")
player1score.place(relx = 0.1, rely = 0.4, anchor = CENTER)
player2score.place(relx = 0.9, rely = 0.4, anchor = CENTER)
card = Label(root, bg = "orange", fg = "green")
card.place(relx = 0.5, rely = 0.5, anchor = CENTER)
list1 = ["Abra", "Bulbasour", "Charmender", "Iyvasour", "Jigglepuff", "Kadabra", "Meowth", "Nidoking", "Paras", "Persion", "Power Pikachu", "Ratata", "Squirtle"]
list2 = [30, 60, 50, 100, 70, 70, 60, 90, 40, 70, 200, 40, 50]
player1_score = 0

def player1() :
    global player1_score
    random_no = random.randint(0,12)
    random_pokemon = list1[random_no]
    card["image"] = random_pokemon
    random_power_list = list2[random_no]
    player1_score = player1score + random_power_list
    player1score["text"] = str(player1_score)

player1_btn = Button(root, image = img, command = player1)
player1_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)
player2_score = 0

def player2() :
    global player2_score
    random_no2 = random.randint(0,12)
    random_pokemon2 = list1[random_no2]
    card["image"] = random_pokemon2
    random_power_list2 = list2[random_no2]
    player2_score = player2_score + random_power_list2
    player2score["text"] = str(player2_score)

player2_btn = Button(root, image = img, command = player2)
player2_btn.place(relx = 0.9, rely = 0.6, anchor = CENTER)
root.mainloop()