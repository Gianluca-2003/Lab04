import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.btnSpellChech = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self._language = None
        self._dd1 = None
        self.txtOut = None
        self.txtIn = None
        self._dd2 = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        self.txtOut = ft.ListView()

        self._dd1 = ft.Dropdown(label="Select language",
                         width= self.page.width,
                         options=[ft.dropdown.Option("english"),
                                  ft.dropdown.Option("italian"),
                                  ft.dropdown.Option("spanish")],
                         on_change = self.__controller.check_language)

        self.page.add(self._dd1)

        self._dd2 = ft.Dropdown(
            width=self.page.width*0.20,
            label="Search modality",
            options=[
            ft.dropdown.Option("Linear"),
            ft.dropdown.Option("Dichotomic"),
            ft.dropdown.Option("Default"),
            ],
            on_change = self.__controller.check_modality)

        self.txtIn = ft.TextField(value="", label="Add your sentence here",width= self.page.width*0.6)

        self.btnSpellChech = ft.ElevatedButton(text="Spell Check",
                                               color="blue",
                                               on_click=self.__controller.handleSpellCheck,
                                               width= self.page.width*0.15)

        row3 = ft.Row(
            controls=[self._dd2, self.txtIn, self.btnSpellChech],
            #alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        self.page.add(row3)

        self.page.add(self.txtOut)


        # Add your stuff here



        self.page.update()

    def update(self):
        self.page.update()


    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
