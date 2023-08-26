stk: stk.c
	gcc stk.c -o stk -g

.PHONY: clean

clean:
	rm stk
