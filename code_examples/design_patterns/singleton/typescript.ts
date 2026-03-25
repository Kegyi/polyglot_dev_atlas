class Config {
  private static shared: Config | null = null;

  private constructor(public env: string) {}

  static instance(): Config {
    if (!Config.shared) {
      Config.shared = new Config('dev');
    }
    return Config.shared;
  }
}

Config.instance().env = 'prod';
console.log(Config.instance().env);