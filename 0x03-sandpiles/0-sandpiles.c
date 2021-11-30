#include "sandpiles.h"

/**
 * sandpiles_sum - that computes the sum of two sandpiles
 * @grid1: Left 3x3 grid
 * @grid2: Right 3x3 grid
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i, j, flag = 1;
	int hypocrite[3][3] = {
		{0, 0, 0},
		{0, 0, 0},
		{0, 0, 0}
	}; /* heap grid */

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
			grid1[i][j] += grid2[i][j];
	}
	while (flag)
	{
		printf("=\n"), flag = 0;
		for (i = 0; i < 3; i++) /* adder and printer */
		{
			for (j = 0; j < 3; j++)
			{
				grid1[i][j] += hypocrite[i][j];
				if (j)
					printf(" ");
				printf("%d", grid1[i][j]);
				hypocrite[i][j] = 0;
			}
			printf("\n");
		}
		for (i = 0; i < 3; i++) /* subtractor and buffer */
		{
			for (j = 0; j < 3; j++)
			{
				if (grid1[i][j] > 3)
				{
					flag++, grid1[i][j] -= 4;
					if (i > 0)
						hypocrite[i - 1][j] += 1;
					if (i < 2)
						hypocrite[i + 1][j] += 1;
					if (j > 0)
						hypocrite[i][j - 1] += 1;
					if (j < 2)
						hypocrite[i][j + 1] += 1;
				}
			}
		}
	}
}
