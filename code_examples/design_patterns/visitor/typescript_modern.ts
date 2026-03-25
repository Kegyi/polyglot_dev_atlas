// Modern TypeScript Visitor using discriminated unions + exhaustive switch
// No Visitor interface or accept/visit ceremony - shapes are plain data objects.

interface Circle    { readonly kind: "circle" }
interface Rectangle { readonly kind: "rectangle" }

type Shape = Circle | Rectangle;

// Operation is a plain function - no "visitor" class needed
function draw(shape: Shape): void {
    switch (shape.kind) {
        case "circle":    console.log("Drawing circle");    break;
        case "rectangle": console.log("Drawing rectangle"); break;
        default: {
            const _exhaustive: never = shape; // compile error if Shape grows
        }
    }
}

// Adding a second operation - no changes to Shape types required
function describe(shape: Shape): string {
    switch (shape.kind) {
        case "circle":    return "it's a circle";
        case "rectangle": return "it's a rectangle";
        default: {
            const _exhaustive: never = shape;
            return "";
        }
    }
}

const circle: Shape    = { kind: "circle" };
const rectangle: Shape = { kind: "rectangle" };

draw(circle);
draw(rectangle);
console.log(describe(circle));
console.log(describe(rectangle));
