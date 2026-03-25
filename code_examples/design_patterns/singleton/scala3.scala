// Singleton
object Config:
    private var env: String = "dev"

    def getEnv(): String = env
    
    def setEnv(e: String): Unit =
        env = e

@main def main(): Unit =
    println(Config.getEnv())
    Config.setEnv("prod")
    println(Config.getEnv())
