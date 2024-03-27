%: %.c
	gcc -Wall -I/usr/local/include -c $< -o $@.o
	gcc -L/usr/local/lib $@.o -lgsl -lgslcblas -lm -o $@

clean:
	rm *.o *.out
