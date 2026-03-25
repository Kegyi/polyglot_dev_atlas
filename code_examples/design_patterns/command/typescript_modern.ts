// Modern TypeScript Command using () => void closures
// No Command interface or class hierarchy - commands are plain callable closures.

class Device {
    turnOn():  void { console.log("Device is ON"); }
    turnOff(): void { console.log("Device is OFF"); }
}

const device = new Device();

const commands: Array<() => void> = [
    () => device.turnOn(),
    () => device.turnOff(),
];

commands.forEach(cmd => cmd());
