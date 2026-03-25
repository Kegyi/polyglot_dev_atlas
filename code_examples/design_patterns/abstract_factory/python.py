from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...


class Dialog(ABC):
    @abstractmethod
    def render(self) -> str: ...


class WidgetFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...

    @abstractmethod
    def create_dialog(self) -> Dialog: ...


class LightButton(Button):
    def render(self) -> str:
        return "light button"


class LightDialog(Dialog):
    def render(self) -> str:
        return "light dialog"


class DarkButton(Button):
    def render(self) -> str:
        return "dark button"


class DarkDialog(Dialog):
    def render(self) -> str:
        return "dark dialog"


class LightFactory(WidgetFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_dialog(self) -> Dialog:
        return LightDialog()


class DarkFactory(WidgetFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_dialog(self) -> Dialog:
        return DarkDialog()


def show_screen(factory: WidgetFactory) -> None:
    print(f"{factory.create_button().render()} + {factory.create_dialog().render()}")


show_screen(LightFactory())
show_screen(DarkFactory())