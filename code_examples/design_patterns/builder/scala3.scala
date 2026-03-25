// Builder
case class House(
    walls: String = "",
    roof: String = "",
    windows: Int = 0,
    doors: Int = 0
)

class HouseBuilder:
    private var walls: String = ""
    private var roof: String = ""
    private var windows: Int = 0
    private var doors: Int = 0

    def withWalls(w: String): HouseBuilder =
        walls = w
        this

    def withRoof(r: String): HouseBuilder =
        roof = r
        this

    def withWindows(w: Int): HouseBuilder =
        windows = w
        this

    def withDoors(d: Int): HouseBuilder =
        doors = d
        this

    def build(): House = House(walls, roof, windows, doors)

@main def main(): Unit =
    val house = new HouseBuilder()
        .withWalls("Wood")
        .withRoof("Shingles")
        .withWindows(8)
        .withDoors(2)
        .build()

    println(house)
