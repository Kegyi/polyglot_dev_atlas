interface Notifier {
  send(message: string): void;
}

class EmailNotifier implements Notifier {
  send(message: string): void {
    console.log(`email: ${message}`);
  }
}

class SmsDecorator implements Notifier {
  constructor(private readonly inner: Notifier) {}

  send(message: string): void {
    this.inner.send(message);
    console.log(`sms: ${message}`);
  }
}

new SmsDecorator(new EmailNotifier()).send('deployment done');
