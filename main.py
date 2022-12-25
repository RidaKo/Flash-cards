from tkinter import *
from data_manip import word_generator



root = Tk()
root.config(padx=50, pady=50, bg="Light green")

#create canvas
canvas = Canvas(width=800, height=530, background="Light green", highlightthickness=0)

#creating the imgaes
right_image = PhotoImage(file= Image(imgtype = "photo",name = "img/right.png"))
wrong_image = PhotoImage(file= Image(imgtype="photo", name="img/wrong.png"))
card_front_img = PhotoImage(file=Image(imgtype="photo",name="img/card_front.png"))
card_back_img = PhotoImage(file=Image(imgtype="photo",name="img/card_back.png"))\

#put the image in canvas and get the container of the image canvas
img_container = canvas.create_image(400,265,image = card_front_img)



def main() -> None:
    word_pair = word_generator()

    def run()-> None:
        root.after(3000, flip_card)
        root.mainloop()

    def change_word() ->None:
        nonlocal word_pair
        word_pair = word_generator()
        canvas.itemconfig(img_container , image = card_front_img)
        canvas.itemconfig(lang_lab,text ="French", fill = "Black")
        canvas.itemconfig(word_lab, text=word_pair["French"], fill = "Black")
        run()

    def flip_card():
        print(word_pair)
        canvas.itemconfig(img_container , image = card_back_img)
        canvas.itemconfig(lang_lab,text ="English", fill = "White",)
        canvas.itemconfig(word_lab,text = word_pair["English"], fill = "White")

    #creating the labels
    # language_label = Label(text="Japanese", font=("Arial", 20, "italic"), bg="White", highlightthickness=0)
    #word_label = Label(text="test", font=("Arial", 50, "bold"), bg="White", highlightthickness=0)


    #create button
    right_button = Button( image=right_image, background="Light green", command= change_word)
    wrong_button= Button( image=wrong_image, background="Light green", command= change_word)

    # gridding all widgets and putting labels into canvas
    canvas.grid(column=0, row=0 ,columnspan=2)
    right_button.grid(column=0, row=1)
    wrong_button.grid(column=1, row=1)
    lang_lab = canvas.create_text(400,50, text="French", font=("Arial", 20, "italic"))
    word_lab = canvas.create_text(400, 263,text=word_pair["French"], font=("Arial", 50, "bold"))
    
    
    run()

main()


