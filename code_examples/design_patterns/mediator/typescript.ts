interface IMediator {
    notify(sender: User, event: string): void;
}

class User {
    constructor(protected mediator: IMediator, public name: string) {}
    
    send(msg: string): void {
        console.log(`${this.name} sends: ${msg}`);
        this.mediator.notify(this, msg);
    }
    
    receive(msg: string): void {
        console.log(`${this.name} receives: ${msg}`);
    }
}

class ChatRoom implements IMediator {
    private user1: User;
    private user2: User;
    
    addUsers(u1: User, u2: User): void {
        this.user1 = u1;
        this.user2 = u2;
    }
    
    notify(sender: User, event: string): void {
        if (sender === this.user1) {
            this.user2.receive(event);
        } else {
            this.user1.receive(event);
        }
    }
}

const room = new ChatRoom();
const u1 = new User(room, "Alice");
const u2 = new User(room, "Bob");

room.addUsers(u1, u2);

u1.send("Hello!");
u2.send("Hi there!");
