import tkinter as tk
import tkinter.messagebox


def oblicz():
    global entry_cena, entry_spalanie, entry_dystans, lbl_wynik
    try:
        cena = float(entry_cena.get())
        spalanie = float(entry_spalanie.get()) / 100
        dystans = float(entry_dystans.get())
        koszt = cena * spalanie * dystans
        lbl_wynik.configure(text=f'koszt przejazdu: \n{koszt:2f} PLN')
    except Exception as e:
        tkinter.messagebox.showerror('Uwaga', 'wprowadź prawidłowe dane')


FONT_LBL = ('Arial', 14, 'normal')
FONT_TXT = ('Consolas', 16, 'bold')
FONT_BTN = ('Arial', 16, 'bold')
FONT_RES = ('Arial', 20, 'bold')


def main():
    global entry_cena, entry_spalanie, entry_dystans, lbl_wynik

    root = tk.Tk()
    root.geometry('400x600')

    lbl_cena = tk.Label(master=root, text='cena PLN: ', font=FONT_LBL)
    lbl_cena.pack()
    entry_cena = tk.Entry(master=root, font=FONT_TXT)
    entry_cena.pack()

    lbl_spalanie = tk.Label(master=root, text='spalanie l/km: ', font=FONT_LBL)
    lbl_spalanie.pack()
    entry_spalanie = tk.Entry(master=root, font=FONT_TXT)
    entry_spalanie.insert(tk.END, '6.5')
    entry_spalanie.pack()

    lbl_dystans = tk.Label(master=root, text='dystans w km: ', font=FONT_LBL)
    lbl_dystans.pack()
    entry_dystans = tk.Entry(master=root, font=FONT_TXT)
    entry_dystans.pack()

    button = tk.Button(master=root, text='oblicz', font=FONT_BTN, command=oblicz)
    button.pack()

    lbl_odstep = tk.Label(master=root, font=FONT_RES)
    lbl_odstep.pack()

    lbl_wynik = tk.Label(master=root, font=FONT_RES)
    lbl_wynik.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
