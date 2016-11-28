# App - Project Kinopoisk Rating film for actor

import urllib.request
from bs4 import BeautifulSoup
import codecs
from tkinter import *


def output(event):
    Filmography.delete(1.0, END)
    #clear text filmography
    NameActor.delete(1.0, END)
    #clear text name actor
    html_d = ent.get()
    # link actor page
    pag = urllib.request.urlopen(html_d)
    # parse html page
    soup = BeautifulSoup(pag, 'lxml')

    name_actor = soup.title.string
    # Name actor
    print("Name Actor = ", name_actor)

    filmography = soup.findAll('div', {"class": "filmo-category-section"})
    # Search all film
    f = codecs.open('text.txt', 'w', 'utf-8')
    # open fail for save information actor
    f.write("Name Actor = " + name_actor + "\n\n" + "Filmography:\n\n")
    # write actor name
    NameActor.insert(END, name_actor)

    for search in filmography:
        div = search.findAll('div')
        # search film
        for info in div:
            year_film = info.findAll('span', {"class": "year_column"})
            # search year film
            name_film = info.findAll('b')
            # search name film
            for name in name_film:
                line = name.text
                # save name film in the string
                print(name.text)
            for year in year_film:
                line += year.text.replace('\n', '')
                # delete "\n" and save year film in the string
                print(year.text)
                f.write(line + '\n')
                Filmography.insert(END, line + '\n')
                # write the name and the year film in fail

    f.close()


# close fail

root = Tk()

Start = Button(root, text="Start", width=5, height=1, bg="white", fg="blue")
Save = Button(root, text="Save", width=5, height=1, bg="white", fg="blue")
lab = Label(root, text="Вставте ссылку на профиль актера \n в поле ввода внизу.", font="Arial 14")
FilmographyLabel = Label(root, text="Фильмы выбранного актера", font="Arial 12")
NameLabel = Label(root, text="Имя актера", font="Arial 12")
ent = Entry(root, width=60, bd=3)
Filmography = Text(root, width=50, height=30, font="10", wrap=WORD)
NameActor = Text(root, width=50, height=1, font="10", wrap=WORD)

Start.bind("<Button-1>", output)
Save.bind("<Button-2>", output)
lab.pack()
ent.pack()
Start.pack()
Save.pack()
NameLabel.pack()
NameActor.pack()
FilmographyLabel.pack()
Filmography.pack()


root.mainloop()


