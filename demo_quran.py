from urllib.request import urlopen
import json
import tkinter as tk


def getJsonFromUrl(url):
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json


quran_url = "https://raw.githubusercontent.com/risan/quran-json/main/data/quran.json"
chapters_url = (
    "https://raw.githubusercontent.com/risan/quran-json/main/data/chapters/en.json"
)

quran = getJsonFromUrl(quran_url)
chapters = getJsonFromUrl(chapters_url)

app = tk.Tk()
app.title("Quran")


app.geometry('395x350+265+75')


bg = tk.Frame(width=395, height=350, bg='#0b2f3a')
bg.place(x=0, y=0)

# Global Variable [sura Number, aya Number]
selection = {"chapter": 1, "verse": 1}

ayaLabel = tk.Label(
    app, text=quran[str(selection["chapter"])
                    ][selection["verse"] - 1]["text"], bg='#dba901'
)
ayaLabel.grid(column=1, row=0, padx=100, pady=100)

suraLabel = tk.Label(
    app, text=chapters[selection["chapter"] - 1]["name"], bg='#dba901')
suraLabel.grid(column=1, row=5, padx=5, pady=5)
numLabel = tk.Label(
    app, text=quran[str(selection["chapter"])
                    ][selection["verse"] - 1]["verse"], bg='#dba901'
)
numLabel.grid(column=1, row=2, padx=5, pady=20)


def displaySelection():
    ayaLabel["text"] = quran[str(selection["chapter"])
                             ][selection["verse"] - 1]["text"]
    suraLabel["text"] = chapters[selection["chapter"] - 1]["name"]
    numLabel["text"] = quran[str(selection["chapter"])
                             ][selection["verse"] - 1]["verse"]


def displayNextAya():
    ayaNum = selection["verse"]
    if ayaNum < chapters[selection["chapter"] - 1]["total_verses"]:
        ayaNum += 1
        selection["verse"] = ayaNum
        displaySelection()


def displayPrevAya():
    ayaNum = selection["verse"]
    if ayaNum > 1:
        ayaNum -= 1
        selection["verse"] = ayaNum
        displaySelection()


def displayNextsura():
    suraNum = selection["chapter"]
    if suraNum < chapters[selection["chapter"] - 1]["total_verses"]:
        suraNum += 1
        selection["chapter"] = suraNum
        displaySelection()


def displayPrevsura():
    suraNum = selection["chapter"]
    if suraNum > 1:
        suraNum -= 1
        selection["chapter"] = suraNum
        displaySelection()


ayaPrevBtn = tk.Button(app, text="<<", bg='#dba901', command=displayPrevAya)
ayaPrevBtn.grid(column=0, row=2, padx=5, pady=10)

ayaNextBtn = tk.Button(app, text=">>", bg='#dba901', command=displayNextAya)
ayaNextBtn.grid(column=2, row=2, padx=5, pady=10)


suraPrevBtn = tk.Button(app, text="<<", bg='#dba901', command=displayPrevsura)
suraPrevBtn.grid(column=0, row=5, padx=5, pady=10)

suraNextBtn = tk.Button(app, text=">>", bg='#dba901', command=displayNextsura)
suraNextBtn.grid(column=2, row=5, padx=5, pady=10)

app.mainloop()
