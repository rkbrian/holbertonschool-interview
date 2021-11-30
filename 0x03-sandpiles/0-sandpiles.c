#include "sandpiles.h"

/**
 * sandpiles_sum - that computes the sum of two sandpiles
 * @grid1: Left 3x3 grid
 * @grid2: Right 3x3 grid
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i, j, flag = 1;
	int hypocrite[3][3] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}; /* heap grid */

	sumall(grid1, grid2);
	while (flag)
	{
		flag = 0;
		for (i = 0; i < 3; i++) /* adder and free buffer */
		{
			for (j = 0; j < 3; j++)
			{
				grid1[i][j] += hypocrite[i][j], hypocrite[i][j] = 0;
				if (grid1[i][j] > 3)
					flag++;
			}
		}
		if (flag)
			printf("=\n"), myprint_grid(grid1);
		else
			break;
		for (i = 0; i < 3; i++) /* subtractor and buffer */
		{
			for (j = 0; j < 3; j++)
			{
				if (grid1[i][j] > 3)
				{
					grid1[i][j] -= 4;
					if (i > 0)
						hypocrite[i - 1][j]++;
					if (i < 2)
						hypocrite[i + 1][j]++;
					if (j > 0)
						hypocrite[i][j - 1]++;
					if (j < 2)
						hypocrite[i][j + 1]++;
				}
			}
		}
	}
}

/**
 * sumall - sum of 2 grids
 * @grid1: Left 3x3 grid
 * @grid2: Right 3x3 grid
 */
void sumall(int grid1[3][3], int grid2[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
			grid1[i][j] += grid2[i][j];
	}
}

/**
 * myprint_grid - Print 3x3 grid
 * @grid: 3x3 grid
 */
void myprint_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}
