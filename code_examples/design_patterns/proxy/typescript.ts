class RealImage {
  constructor() {
    console.log('load image');
  }

  display(): void {
    console.log('display image');
  }
}

class ImageProxy {
  private real: RealImage | null = null;

  display(): void {
    if (!this.real) {
      this.real = new RealImage();
    }
    this.real.display();
  }
}

const proxy = new ImageProxy();
proxy.display();
proxy.display();
