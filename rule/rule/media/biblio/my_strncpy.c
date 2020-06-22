/*
** EPITECH PROJECT, 2019
** my_strncpy
** File description:
** one string into an other
*/

#include <unistd.h>

char *my_strncpy(char *dest, char const *src, int n)
{
    int i = 0;
    int count = 0;
    int n_base = n;

    for (i = 0; src[i] != '\0'; i++) {
        count++;
    }
    i = 0;
    for (i = 0; n != 0; i++) {
        dest[i] = src[i];
        n--;
    }
    if (n_base > count) {
        dest[i] = '\0';
    }
    return (dest);
}
