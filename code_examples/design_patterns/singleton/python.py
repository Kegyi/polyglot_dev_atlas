class Config:
    _instance: "Config | None" = None

    def __new__(cls) -> "Config":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.env = "dev"
        return cls._instance


Config().env = "prod"
print(Config().env)