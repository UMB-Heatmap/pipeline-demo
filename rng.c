#include <stdio.h>
#include <getopt.h>
#include <math.h>
#include <gsl/gsl_rng.h>

int main (int argc, char **argv) {
    int opt;
    int n = 0;

    while ((opt = getopt(argc, argv, "n:")) != -1) {
        switch (opt) {
            case 'n':
                n = atoi(optarg);
                break;
        }
    }

    if (n == 0) return 1;

    /*    rng     */
    gsl_rng * r = gsl_rng_alloc(gsl_rng_taus);

    double x;

    for (int i = 0; i < n; i++) {
        x = gsl_rng_uniform(r);
        printf("%f\n", x);
    }


    gsl_rng_free(r);
    return 0;
}
