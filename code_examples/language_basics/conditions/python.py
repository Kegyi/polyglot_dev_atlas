#!/usr/bin/env python3

def grade_to_label(grade: int) -> str:
    if grade >= 90:
        return "excellent"
    if grade >= 75:
        return "good"
    if grade >= 60:
        return "pass"
    return "fail"


def main() -> None:
    grade = 82
    code = 2

    print("if/elif/else:", grade_to_label(grade))

    match code:
        case 1:
            print("match: created")
        case 2:
            print("match: updated")
        case 3:
            print("match: deleted")
        case _:
            print("match: unknown")

    ready = grade >= 60
    print("conditional expression:", "can continue" if ready else "needs retry")


if __name__ == "__main__":
    main()
