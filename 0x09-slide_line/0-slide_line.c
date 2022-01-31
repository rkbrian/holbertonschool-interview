#include "slide_line.h"

/**
 * slide_line - function to reproduce the 2048 game mechanics
 *  on a single horizontal line.
 *  Notes: I wonder if there's less time complexity solution, I'm ok w/ mine
 * @line: array of integers
 * @size: element count of the array
 * @direction: 0 for left, 1 for right
 * Return: 1 upon success, or 0 upon failure
 */
int slide_line(int *line, size_t size, int direction)
{
	int start = direction * (size - 1), end = size - direction * (size + 1);
	int k = 1 - direction * 2, i, curr_i, flag = 0;

	if (!line || !size || (direction != SLIDE_LEFT && direction != SLIDE_RIGHT))
		return (0);
	for (i = start; i != end; i += k) /*merge*/
	{
		curr_i = i, i += k;
		while (i != end && line[i] == 0) /*merge aross 0s*/
		{
			i += k;
			if (i == end)
				flag = 1;
		}
		if (flag)
			break;
		if (i != end && line[curr_i] == line[i])
			line[curr_i] *= 2, line[i] = 0;
		else
			i -= k;
	}
	for (i = start; i != end; i += k) /*align*/
	{
		curr_i = i;
		while (i != end && line[i] == 0)
		{
			i += k;
			if (i == end)
				return (1);
		}
		if (curr_i != i)
			line[curr_i] = line[i], line[i] = 0, i = curr_i;
	}
	return (1);
}
