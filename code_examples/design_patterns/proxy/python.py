class RealImage:
    def __init__(self) -> None:
        print("load image")

    def display(self) -> None:
        print("display image")


class ImageProxy:
    def __init__(self) -> None:
        self._real: RealImage | None = None

    def display(self) -> None:
        if self._real is None:
            self._real = RealImage()
        self._real.display()


proxy = ImageProxy()
proxy.display()
proxy.display()
