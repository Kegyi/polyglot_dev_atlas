interface Button {
  render(): string;
}

interface Dialog {
  render(): string;
}

interface WidgetFactory {
  createButton(): Button;
  createDialog(): Dialog;
}

class LightButton implements Button {
  render(): string {
    return 'light button';
  }
}

class LightDialog implements Dialog {
  render(): string {
    return 'light dialog';
  }
}

class DarkButton implements Button {
  render(): string {
    return 'dark button';
  }
}

class DarkDialog implements Dialog {
  render(): string {
    return 'dark dialog';
  }
}

class LightFactory implements WidgetFactory {
  createButton(): Button {
    return new LightButton();
  }

  createDialog(): Dialog {
    return new LightDialog();
  }
}

class DarkFactory implements WidgetFactory {
  createButton(): Button {
    return new DarkButton();
  }

  createDialog(): Dialog {
    return new DarkDialog();
  }
}

function showScreen(factory: WidgetFactory): void {
  console.log(`${factory.createButton().render()} + ${factory.createDialog().render()}`);
}

showScreen(new LightFactory());
showScreen(new DarkFactory());