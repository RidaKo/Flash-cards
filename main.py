from tkinter import *
from data_manip import word_generator





def main() ->None:

    def change_word() ->None:
        word_label.config(text=word_generator())

    def flip_card():
        canvas.itemconfig(card_front_img, image = card_back_img)
        root.after_cancel()

    root = Tk()
    root.config(padx=50, pady=50, bg="Light green")

    #create canvas
    canvas = Canvas(width=800, height=530, background="Light green", highlightthickness=0)

    #creating the imgaes
    right_image = PhotoImage(file= Image(imgtype = "photo",name = "img/right.png"))
    wrong_image = PhotoImage(file= Image(imgtype="photo", name="img/wrong.png"))
    card_front_img = PhotoImage(file=Image(imgtype="photo",name="img/card_front.png"))
    card_back_img = PhotoImage(file=Image(imgtype="photo",name="img/card_back.png"))\
    
    #put the image in canvas
    canvas.create_image(400,265,image = card_front_img)

    #creating the labels
    language_label = Label(text="Japanese", font=("Arial", 20, "italic"), bg="White", highlightthickness=0)
    word_label = Label(text="test", font=("Arial", 50, "bold"), bg="White", highlightthickness=0)


    #create button
    right_button = Button( image=right_image, background="Light green", command= change_word)
    wrong_button= Button( image=wrong_image, background="Light green", command= change_word)

    # gridding all widgets and putting labels into canvas
    canvas.grid(column=0, row=0 ,columnspan=2)
    right_button.grid(column=0, row=1)
    wrong_button.grid(column=1, row=1)
    canvas.create_window(400,50, window= language_label)
    canvas.create_window(400, 263,window= word_label)


    root.after(3000, flip_card)


    root.mainloop()


main()