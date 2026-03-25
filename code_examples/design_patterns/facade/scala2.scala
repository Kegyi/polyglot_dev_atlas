// Facade
class Compiler {
    def compile(): Unit = println("Compiling code...")
}

class Tester {
    def test(): Unit = println("Running tests...")
}

class Deployer {
    def deploy(): Unit = println("Deploying package...")
}

class BuildFacade {
    private val compiler = new Compiler()
    private val tester = new Tester()
    private val deployer = new Deployer()
    
    def build(): Unit = {
        compiler.compile()
        tester.test()
        deployer.deploy()
    }
}

object Main extends App {
    val facade = new BuildFacade()
    facade.build()
}
