/*
** EPITECH PROJECT, 2019
** my_swap
** File description:
** function swap variable
*/

int my_swap(int *a, int *b)
{
    int c;

    c = *a;
    *a = *b;
    *b = c;
    return (0);
}
