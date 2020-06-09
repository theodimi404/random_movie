from tkinter import *
from tkinter.ttk import *
import bs4
import requests
import random
import webbrowser

window = Tk()
window.title("IMDB Random Generator Movie")
window.geometry("600x460")
window.resizable(0, 0)

chosen_movie = ''


def find_movie():
    genre = comboGenre.get()
    rating_low = comboRatingL.get()
    rating_high = comboRatingH.get()
    date_low = comboDateL.get()
    date_high = comboDateH.get()
    votes_low = comboNumVotesL.get()
    votes_high = comboNumVotesH.get()
    url = f'https://www.imdb.com/search/title/?title_type=feature&release_date={date_low}-01-01,{date_high}-12-31&user_rating={rating_low},{rating_high}&num_votes={votes_low},{votes_high}&genres={genre}'
    try:
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        data = []
        for ana in soup.findAll('a'):
            if ana.parent.name == 'h3':
                data.append('https://www.imdb.com' + ana["href"])

        txt.delete("1.0", END)
        response1 = ''
        if data:
            global chosen_movie
            chosen_movie = random.choice(data)
            res1 = requests.get(chosen_movie)
            soup1 = bs4.BeautifulSoup(res1.text, 'html.parser')

            movie_data = soup1.find("div", {"class": "title_wrapper"})

            response1 = ''
            title = movie_data.find("h1", {"class": "long"})
            if title:
                title_data = list(title.stripped_strings)
                response1 = response1 + 'Title : ' + ''.join(title_data) + '\n'

            title1 = movie_data.find("h1", {"class": ""})
            if title1:
                title1_data = list(title1.stripped_strings)
                response1 = response1 + 'Title : ' + ''.join(title1_data) + '\n'

            original_title = movie_data.find("div", {"class": "originalTitle"})
            if original_title:
                original_title_data = list(original_title.stripped_strings)
                response1 = response1 + ''.join(original_title_data) + '\n'

            runtime = movie_data.find("time")
            if runtime:
                runtime_data = list(runtime.stripped_strings)
                response1 = response1 + 'Runtime: ' + ''.join(runtime_data)

            stoixeia = []
            for i in movie_data('a'):
                stoixeia.append(i.get_text())

            response2 = f"""
Genres: {stoixeia[1]}, {stoixeia[2]}, {stoixeia[3]}
Release Date: {stoixeia[4]}
    
    
Sorted by current popularity in IMDB"""

            response1 = response1 + response2
        txt.insert("1.0", response1)
    except:
        txt.insert("1.0", "404")


def open_imdb():
    global chosen_movie
    webbrowser.open(chosen_movie)


frm_Search = Frame(window)
frm_Search.grid(row=0, column=0)

lblGenre = Label(frm_Search, text="Choose a genre")
lblGenre.grid(row=0, column=0, padx=5, pady=5)

comboGenre = Combobox(frm_Search, values=[
    "Action",
    "Comedy",
    "Family",
    "History",
    "Mystery",
    "Sci-Fi",
    "War",
    "Adventure",
    "Crime",
    "Fantasy",
    "Horror",
    "News",
    "Sport",
    "Western",
    "Animation",
    "Documentary",
    "Film-Noir",
    "Music",
    "Reality-TV",
    "Talk-Show",
    "Biography",
    "Drama",
    "Game-Show",
    "Musical",
    "Romance",
    "Thriller"])
comboGenre.current(0)
comboGenre.grid(row=1, column=0, padx=5, pady=5)

lblRatingL = Label(frm_Search, text="Choose a minumum rating")
lblRatingL.grid(row=2, column=0, padx=5, pady=5)

comboRatingL = Combobox(frm_Search, values=[
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"])
comboRatingL.current(0)
comboRatingL.grid(row=3, column=0, padx=5, pady=5)

lblRatingH = Label(frm_Search, text="Choose a maximum rating")
lblRatingH.grid(row=4, column=0, padx=5, pady=5)

comboRatingH = Combobox(frm_Search, values=[
    "10",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"])
comboRatingH.current(9)
comboRatingH.grid(row=5, column=0, padx=5, pady=5)

lblNumVotesL = Label(frm_Search, text="Choose a minimum Number of Votes")
lblNumVotesL.grid(row=6, column=0, padx=5, pady=5)

comboNumVotesL = Combobox(frm_Search, values=[
    "5000",
    "20000",
    "50000",
    "100000",
    "150000",
    "200000",
    "500000",
    "750000",
    "1000000",
    "1500000",
    "2000000",
    "3000000"])
comboNumVotesL.current(0)
comboNumVotesL.grid(row=7, column=0, padx=5, pady=5)

lblNumVotesH = Label(frm_Search, text="Choose a maximum Number of Votes")
lblNumVotesH.grid(row=8, column=0, padx=5, pady=5)

comboNumVotesH = Combobox(frm_Search, values=[
    "5000",
    "20000",
    "50000",
    "100000",
    "150000",
    "200000",
    "500000",
    "750000",
    "1000000",
    "1500000",
    "2000000",
    "3000000"])
comboNumVotesH.current(11)
comboNumVotesH.grid(row=9, column=0, padx=5, pady=5)

lblDateL = Label(frm_Search, text="Choose a Release Date (min)")
lblDateL.grid(row=10, column=0, padx=5, pady=5)

comboDateL = Combobox(frm_Search, values=[
    "1900",
    "1910",
    "1920",
    "1930",
    "1940",
    "1950",
    "1960",
    "1970",
    "1980",
    "1990",
    "2000",
    "2010",
    "2020"])
comboDateL.current(0)
comboDateL.grid(row=11, column=0, padx=5, pady=5)

lblDateH = Label(frm_Search, text="Choose a Release Date (max)")
lblDateH.grid(row=12, column=0, padx=5, pady=5)

comboDateH = Combobox(frm_Search, values=[
    "1900",
    "1910",
    "1920",
    "1930",
    "1940",
    "1950",
    "1960",
    "1970",
    "1980",
    "1990",
    "2000",
    "2010",
    "2020"])
comboDateH.current(12)
comboDateH.grid(row=13, column=0, padx=5, pady=5)

frm_Buttons = Frame(window)
frm_Buttons.grid(row=1, column=1)

txt = Text(window, width=45, height=25)
txt.grid(column=1, row=0)

btnSearch = Button(frm_Buttons, text="Search", width=10, command=find_movie)
btnSearch.grid(column=0, row=0, padx=15, pady=5)

btnSearch = Button(frm_Buttons, text="Open in IMDB", width=14, command=open_imdb)
btnSearch.grid(column=1, row=0, padx=15, pady=5)

window.mainloop()
