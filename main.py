from tkinter import *
from PIL import Image, ImageTk
from Instagram_Class import InstagramBot

LB_FONT = ("Helvetica", 14, "bold")
SM_FONT = ("Helvetica", 12, "bold")


class InstagramBotApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Instagram Bot")
        self.window.geometry("393x480")
        # my variables:
        self.chosen_name = StringVar()

        self.header = Label(self.window, text="Automate - Following Function", font=LB_FONT, bd=1,
                            highlightthickness=1, relief=RIDGE, fg="green")
        self.header.place(x=5, y=5, width=382, height=40)

        used_image = Image.open("IMG/instagram.jpg")
        used_photo = ImageTk.PhotoImage(used_image)
        self.image_label = Label(self.window, image=used_photo, bd=1, highlightthickness=1, relief=RIDGE)
        self.image_label.image = used_photo
        self.image_label.place(x=5, y=50, width=382, height=237)

        self.central = Frame(self.window, bd=1, highlightthickness=1, relief=RIDGE, bg="light cyan")
        self.central.place(x=5, y=293, width=382, height=162)

        self.name = Label(self.central, text="Enter UserName", font=SM_FONT, justify="center", bd=1,
                          highlightthickness=1, relief=RIDGE)
        self.name.place(x=5, y=5, width=180, height=30)

        self.name_entry = Entry(self.central, font=SM_FONT, justify="center", bd=1, bg="wheat", fg="dark red",
                                highlightthickness=1, relief=RIDGE, textvariable=self.chosen_name)
        self.name_entry.place(x=190, y=4, width=184, height=32)

        follow_image = Image.open("IMG/follow.png")
        follow_photo = ImageTk.PhotoImage(follow_image)
        self.follow = Button(self.central, font=SM_FONT, image=follow_photo, bd=0, bg="light cyan",
                             command=self.follow_method)
        self.follow.image = follow_photo
        self.follow.place(x=210, y=40, width=149, height=47)

        close_image = Image.open("IMG/close.png")
        close_photo = ImageTk.PhotoImage(close_image)
        self.close = Button(self.central, font=SM_FONT, image=close_photo, bd=0, bg="light cyan",
                            command=self.close_method)
        self.close.image = close_photo
        self.close.place(x=50, y=40, width=94, height=47)

        self.answer = Label(self.central, text="", font=SM_FONT, justify="center", bd=1, wraplength=300,
                            highlightthickness=1, relief=RIDGE, bg="alice blue")
        self.answer.place(x=5, y=91, width=368, height=60)

    # ================================= FUNCTIONALITY =============================== #
    def close_method(self):
        self.window.destroy()

    def follow_method(self):
        bot_tool = InstagramBot()
        bot_tool.login_instagram()
        bot_tool.search_page(user_name=self.chosen_name.get())
        quantity = bot_tool.find_followers()
        self.answer.config(text=f"Number of Users - You are following increased by {quantity}", bg="pale green")


def launch_app():
    app = Tk()
    InstagramBotApp(app)
    app.mainloop()


if __name__ == "__main__":
    launch_app()
