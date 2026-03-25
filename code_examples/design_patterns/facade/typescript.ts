class Compiler {
  run(): void {
    console.log('compile');
  }
}

class TestRunner {
  run(): void {
    console.log('test');
  }
}

class Packager {
  run(): void {
    console.log('package');
  }
}

class ReleaseFacade {
  private readonly compiler = new Compiler();
  private readonly tests = new TestRunner();
  private readonly packager = new Packager();

  deploy(): void {
    this.compiler.run();
    this.tests.run();
    this.packager.run();
  }
}

new ReleaseFacade().deploy();
