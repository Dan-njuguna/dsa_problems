#include <stdio.h>
#include <stdlib.h>
#define HASH_SIZE 10000
/**
 * twoSum - return the position of values that attain sum of target value.
 * @nums: The array of numbers.
 * @numsSize: The Size of array.
 * @target: The target Value.
 * @returnSize: Size of the returned value.
 * Return: Array of positions
*/
int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    int i, complement, index;
    int *res;
    int *hashTable;
    
    res = (int *)malloc(2 * sizeof(int));
    if (!res)
    {
        *returnSize = 0;
        fprintf(stderr, "Error allocating memory.\n");
        exit(EXIT_FAILURE);
    }

    /*Allocate hashTable and initialize to -1*/
    hashTable = (int *)malloc(HASH_SIZE * sizeof(int));
    if (!hashTable)
    {
        free(res);
        *returnSize = 0;
        exit(EXIT_FAILURE);
    }
    for (i = 0; i < HASH_SIZE; i++)
    {
        hashTable[i] = -1;
    }

    for (i = 0; i < numsSize; i++)
    {
        complement = target - nums[i];
        index = (complement + 1000) % HASH_SIZE; /*Adjust to handle negative indices*/
        
        if (hashTable[index] != -1)
        {
            res[0] = hashTable[index];
            res[1] = i;
            *returnSize = 2;
            free(hashTable);
            return res;
        }
        
        index = (nums[i] + 1000) % HASH_SIZE;
        hashTable[index] = i;
    }

    free(hashTable);
    *returnSize = 0;
    return NULL;
}

/*Main Test Function*/
int main(void)
{
    int nums[5] = {3, 2, 95, 4, -3};
    int target = 92;
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;
    int* result = twoSum(nums, numsSize, target, &returnSize);

    if (result)
    {
        printf("Indices: [%d, %d]\n", result[0], result[1]);
        free(result);
    }
    else
    {
        printf("No two sum solution found.\n");
    }

    return (0);
}