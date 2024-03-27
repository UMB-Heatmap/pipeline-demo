#include <stdio.h>
#include <math.h>
#include <gsl/gsl_rng.h>

#define N 1000000

int main (void) {
	gsl_rng * r = gsl_rng_alloc(gsl_rng_taus);

	double x;

	for (int i = 0; i < N; i++) {
		x = gsl_rng_uniform(r);
		printf("%f\n", x);
	}


	gsl_rng_free(r);
	return 0;
}
