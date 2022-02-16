#include "menger.h"

/**
 * menger - function that slides and merges an array of integers.
 * @level: the level of the Menger Sponge to draw
 */
void menger(int level)
{
	int i, j, pow;

	if (level < 0)
		return;
	pow = powerranger(level);
	for (i = 0; i < pow; i++)
	{
		for (j = 0; j < pow; j++)
		{
			if (hollow_gram(i, j, pow))
				putchar(' ');
			else
				putchar('#');
		}
		putchar('\n');
	}
}

/**
 * powerranger - function to implement 3^a with given index a
 * @a: ath power of 3
 * Return: 3^a
 */
int powerranger(int a)
{
	int i = 0, ret = 1;

	while (i < a)
		ret *= 3, i++;
	return (ret);
}

/**
 * hollow_gram - function to define if a pair of coordinates in a matrix of
 *  certain size should be hollow
 * @i: vertical coordinate
 * @j: horizontal coordinate
 * @size: size of the square matrix
 * Return: 0 for solid area, 1 for hollow area
 */
int hollow_gram(int i, int j, int size)
{
	int regional_i = i * 3 / size, regional_j = j * 3 / size;

	if (j < 1)
		return (0);
	if (regional_i == 1 && regional_j == 1)
		return (1);
	i -= regional_i * size / 3, j -= regional_j * size / 3;
	return (hollow_gram(i, j, size / 3));
}
