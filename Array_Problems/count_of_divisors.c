#include <stdio.h>
#include <stdlib.h>
/**
 * @brief Function to compute the greatest common divisor (GCD) of two integers
 *
 * @param a The first integer
 * @param b The second integer
 * @return int The GCD of a and b
 */
int gcd(int a, int b)
{
    while (b != 0)
    {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

/**
 * @brief Main function to find the number of common divisors for two integers
 *
 * This function takes two integers as input and calculates the number of common divisors
 * that divide both integers without a remainder.
 *
 * @param void No parameters are required for this function.
 *
 * @return int Always returns 0.
 */
int main(void)
{
    int a, b;
    int i, common_divisors_count = 0;

    /*Read the two integers from input*/
    scanf("%d %d", &a, &b);

    /*Calculate the GCD of the two numbers*/
    int gcd_ab = gcd(a, b);

    /*Iterate through all possible divisors up to the square root of gcd_ab*/
    for (i = 1; i * i <= gcd_ab; i++)
    {
        if (gcd_ab % i == 0)
        {
            common_divisors_count++;
            if (i != gcd_ab / i)
            {
                common_divisors_count++;
            }
        }
    }
    /*Print the count of common divisors*/
    printf("%d\n", common_divisors_count);

    return (0);
}
