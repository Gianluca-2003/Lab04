import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view
        self._myLanguage = None
        self._mytxtIn = None
        self._myModality = None


    def check_language(self, e):
        self._myLanguage = self._view._dd1.value
        if self._myLanguage == "":
            print("Lingua non inserita")
            return
        else:
            self._view.txtOut.controls.append(ft.Text(f"Lingua inserita: {self._myLanguage}"))
            self._view.update()
            print("Lingua inserita")


    def check_modality(self, e):
        self._myModality = self._view._dd2.value
        if self._myModality == "":
            print("Modalita non inserita")
            return
        else:
            self._view.txtOut.controls.append(ft.Text(f"Modalità inserita: {self._myModality}"))
            self._view.update()
            print("Modalita inserita")




    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())
        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                self._view.txtOut.controls.append(ft.Text(f"Parole errate: {paroleErrate} e tempo: {t2 - t1} ", color="green"))
                self._view.update()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                self._view.txtOut.controls.append(ft.Text(f"Parole errate: {paroleErrate} \nTempo: {t2 - t1} ", color="green"))
                self._view.update()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                self._view.txtOut.controls.append(ft.Text(f"Parole errate: {paroleErrate} e tempo: {t2 - t1} ", color="green"))
                self._view.update()
                return paroleErrate, t2 - t1
            case _:
                return None

    def handleSpellCheck(self, e):
        if self._myLanguage is None:
            self._view.txtOut.controls.append(ft.Text(f"Devi scegliere una lingua", color="red"))
            self._view.update()
            return
        if self._myModality is None:
            self._view.txtOut.controls.append(ft.Text(f"Devi scegliere una modalità", color="red"))
            self._view.update()
            return
        self._mytxtIn = self._view.txtIn.value
        if self._mytxtIn == "":
            self._view.txtOut.controls.append(ft.Text(f"Devi inserire una frase", color="red"))
            self._view.update()
            return
        self._view.txtOut.controls.append(ft.Text(f"Frase Inserita: {self._mytxtIn}"))
        self._view.update()
        print("Frase Inserita")
        self.handleSentence(self._mytxtIn, self._myLanguage, self._myModality)






    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text