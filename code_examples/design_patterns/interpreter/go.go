package main

import (
	"fmt"
	"strings"
)

type Expression interface {
	Interpret(string) bool
}

type TerminalExpression struct {
	literal string
}

func (t *TerminalExpression) Interpret(ctx string) bool {
	return strings.Contains(ctx, t.literal)
}

type OrExpression struct {
	expr1, expr2 Expression
}

func (o *OrExpression) Interpret(ctx string) bool {
	return o.expr1.Interpret(ctx) || o.expr2.Interpret(ctx)
}

type AndExpression struct {
	expr1, expr2 Expression
}

func (a *AndExpression) Interpret(ctx string) bool {
	return a.expr1.Interpret(ctx) && a.expr2.Interpret(ctx)
}

func main() {
	c1 := &TerminalExpression{"cat"}
	c2 := &TerminalExpression{"dog"}
	expr := &OrExpression{c1, c2}

	fmt.Println(expr.Interpret("cat"))
	fmt.Println(expr.Interpret("bird"))
}
