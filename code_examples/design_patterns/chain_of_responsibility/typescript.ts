interface IHandler {
    setNext(next: IHandler): void;
    handle(request: Request): void;
}

class Request {
    constructor(public level: number, public message: string) {}
}

abstract class BaseHandler implements IHandler {
    protected next: IHandler | null = null;
    
    setNext(next: IHandler): void {
        this.next = next;
    }
    
    abstract handle(request: Request): void;
}

class LowHandler extends BaseHandler {
    handle(request: Request): void {
        if (request.level <= 1) {
            console.log(`LowHandler: ${request.message}`);
        } else if (this.next) {
            this.next.handle(request);
        }
    }
}

class MidHandler extends BaseHandler {
    handle(request: Request): void {
        if (request.level === 2) {
            console.log(`MidHandler: ${request.message}`);
        } else if (this.next) {
            this.next.handle(request);
        }
    }
}

class HighHandler extends BaseHandler {
    handle(request: Request): void {
        if (request.level >= 3) {
            console.log(`HighHandler: ${request.message}`);
        }
    }
}

const low = new LowHandler();
const mid = new MidHandler();
const high = new HighHandler();

low.setNext(mid);
mid.setNext(high);

low.handle(new Request(1, "Simple"));
low.handle(new Request(2, "Normal"));
low.handle(new Request(3, "Critical"));
