#include "palindrome.h"

/**
 * is_palindrome - checks if an unsigned long integer is a palindrome.
 *  Notes: my method uses a big divisor (in power of 10) to find & behead
 *  the 1st digit, uses modulo to find the last digit, time complexity O(n).
 * @n: unsigned long integer to be checked
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome 
 */
int is_palindrome(unsigned long n)
{
	int ret_num = 1, pow = 0;
	unsigned long pow_of_ten = 1;

	if (n < 10)
		return (ret_num);
	while (pow_of_ten <= n)
		pow_of_ten *= 10, pow++;
	pow /= 2, pow_of_ten /= 10; /*the middle index & the max divisor*/
	while (pow > 0)
	{
		if (n / pow_of_ten != n % 10)
			return (0);
		n = n % pow_of_ten;
		n /= 10;
		pow--, pow_of_ten /= 100;
	}
	return (ret_num);
}
