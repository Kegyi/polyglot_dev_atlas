interface Sender {
  send(message: string): void;
}

class EmailSender implements Sender {
  send(message: string): void {
    console.log(`email: ${message}`);
  }
}

class SmsSender implements Sender {
  send(message: string): void {
    console.log(`sms: ${message}`);
  }
}

class AlertNotification {
  constructor(private readonly sender: Sender) {}

  notify(message: string): void {
    this.sender.send(`alert -> ${message}`);
  }
}

new AlertNotification(new EmailSender()).notify('CPU high');
new AlertNotification(new SmsSender()).notify('CPU high');
