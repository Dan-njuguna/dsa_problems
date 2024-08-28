#include <stdio.h>
#include <stdlib.h>
float *averageMarks(int **grades, int len0, int len1);
/**
 * main - Entry Point
 * Return: Always 0 on success
 */
int main(void)
{
    /*grades[2][5]*/
    int **grades;
    int len[2], i, j;
    float *answer;

    printf("Enter the number of subjects and number of student marks: ");
    scanf("%d %d", &len[0], &len[1]);

    /* Allocate memory for an array of int pointers (one for each subject) */
    grades = (int **)malloc(len[0] * sizeof(int *));
    if (grades == NULL)
    {
        exit(EXIT_FAILURE);
    }

    /* Allocate memory for each subject's marks */
    for (i = 0; i < len[0]; i++)
    {
        grades[i] = (int *)malloc(len[1] * sizeof(int));
        if (grades[i] == NULL)
        {
            for (j = 0; j < i; j++)
            {
                free(grades[j]);
            }
            free(grades);
            exit(EXIT_FAILURE);
        }
    }

    /* Input the marks for each subject */
    for (i = 0; i < len[0]; i++)
    {
        printf("Enter marks for subject %d: ", i + 1);
        for (j = 0; j < len[1]; j++)
        {
            scanf("%d", &grades[i][j]);
        }
    }

    /* Calculate the average marks for each subject */
    answer = averageMarks(grades, len[0], len[1]);
    if (answer == NULL)
    {
        for (i = 0; i < len[0]; i++)
        {
            free(grades[i]);
        }
        free(grades);
        exit(EXIT_FAILURE);
    }

    /* Print the average marks */
    printf("SUBJECT_ID\tAVERAGE\n-----------------------\n");
    for (i = 0; i < len[0]; i++)
    {
        printf("%d\t\t%.1f\n", i + 1, answer[i]);
    }

    /* Free the allocated memory */
    for (i = 0; i < len[0]; i++)
    {
        free(grades[i]);
    }
    free(grades);
    free(answer);

    return (0);
}
 
/**
 * averageMarks - Function to calculate the average marks for students given
 *      their marks for each subject
 * @grades: 2D array for {subject_id, student_marks}.
 * @len0: Number of subjects
 * @len1: Number of student marks
 * Return: Average marks 1D array for their subjects  
 */
float *averageMarks(int **grades, int len0, int len1)
{
    int i, j;
    float *avg, sum;

    /* Allocate memory for the average array */
    avg = (float *)malloc(len0 * sizeof(float));
    if (avg == NULL)
    {
        exit(EXIT_FAILURE);
    }

    /* Calculate the average marks for each subject */
    for (i = 0; i < len0; i++)
    {
        sum = 0;
        for (j = 0; j < len1; j++)
        {
            sum += grades[i][j];
        }
        avg[i] = sum / len1;
    }

    return (avg);
}