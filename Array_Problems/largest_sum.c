#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/**
 * @brief Entry point of the program.
 *
 * This function reads the number of elements, allocates memory for the array,
 * reads the elements of the array, calculates the sum1, and then calculates
 * the minimum value x such that the sum of the new array is strictly greater than sum1.
 * It also prints the new element value and the new sum.
 *
 * @return Always 0
 */
int main(void)
{
    int N, i, sum1 = 0, sum2, n;
    int *A;

    /*Read the number of elements*/
    scanf("%d", &N);

    /*Allocate memory for the array*/
    A = (int *)malloc(N * sizeof(int));
    if (A == NULL)
    {
        perror("Failed to allocate memory.\n");
        exit(EXIT_FAILURE);
    }

    /*Read the elements of the array and calculate the sum1*/
    for (i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
        sum1 += A[i];
    }

    /*Calculate the minimum value x such that the sum of the new array is strictly greater than sum1*/
    /* sum2 = N * n > sum1 implies n > sum1 / N*/
    n = (int)ceil((double)sum1 / N);

    /*If n is not strictly greater than sum1 / N, increment n*/
    if (n * N <= sum1)
    {
        n++;
    }

    /*Calculate the sum of the new array*/
    sum2 = N * n;

    /*Print the new element value and the new sum*/
    printf("New element value: %d\n", n);
    printf("Sum of the new array: %d\n", sum2);

    /*Free the allocated memory*/
    free(A);

    return (0);
}