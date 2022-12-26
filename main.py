from tkinter import *
from data_manip import WordGenerator



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
    word_gen = WordGenerator() 
    word_gen.generate_words()

    timer = None
    def run()-> None:
        nonlocal timer
        timer = root.after(3000, flip_card)
        root.mainloop()

    def correct_click() ->None:
        word_gen.remove_words_and_write_to_learnt_file()
        change_word()
    
    def wrong_click() ->None:
        change_word()

    def change_word() ->None:
        word_gen.generate_words()
        canvas.itemconfig(img_container , image = card_front_img)
        canvas.itemconfig(lang_lab,text ="French", fill = "Black")
        canvas.itemconfig(word_lab, text=word_gen.word_pair["French"], fill = "Black")
        root.after_cancel(timer)
        run()

    def flip_card():
        canvas.itemconfig(img_container , image = card_back_img)
        canvas.itemconfig(lang_lab,text ="English", fill = "White",)
        canvas.itemconfig(word_lab,text = word_gen.word_pair["English"], fill = "White")

    #creating the labels
    # language_label = Label(text="Japanese", font=("Arial", 20, "italic"), bg="White", highlightthickness=0)
    #word_label = Label(text="test", font=("Arial", 50, "bold"), bg="White", highlightthickness=0)


    #create button
    right_button = Button( image=right_image, background="Light green", command= correct_click)
    wrong_button= Button( image=wrong_image, background="Light green", command= wrong_click)

    # gridding all widgets and putting labels into canvas
    canvas.grid(column=0, row=0 ,columnspan=2)
    right_button.grid(column=0, row=1)
    wrong_button.grid(column=1, row=1)
    lang_lab = canvas.create_text(400,50, text="French", font=("Arial", 20, "italic"))
    word_lab = canvas.create_text(400, 263,text= word_gen.word_pair["French"], font=("Arial", 50, "bold"))
    
    
    run()

main()


