// Singleton
object Config {
    private var env: String = "dev"

    def getEnv(): String = env
    
    def setEnv(e: String): Unit = {
        env = e
    }
}

object Main extends App {
    println(Config.getEnv())
    Config.setEnv("prod")
    println(Config.getEnv())
}
