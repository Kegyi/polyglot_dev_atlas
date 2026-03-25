class Compiler:
    def run(self) -> None:
        print("compile")


class TestRunner:
    def run(self) -> None:
        print("test")


class Packager:
    def run(self) -> None:
        print("package")


class ReleaseFacade:
    def __init__(self) -> None:
        self.compiler = Compiler()
        self.tests = TestRunner()
        self.packager = Packager()

    def deploy(self) -> None:
        self.compiler.run()
        self.tests.run()
        self.packager.run()


ReleaseFacade().deploy()
