#include "lists.h"

/**
 * lower_rev - reverse the lower half of the linked list
 * @head: head node of the linked list lower half
 * Return: the reversed head node
 */
listint_t *lower_rev(listint_t **head)
{
	listint_t *current = NULL, *prev = NULL, *next = NULL;

	current = *head;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *  Note: I have to make the change (reverse the lower half linkage) of
 *  the list to decrease the time complexity. Size up to ULONG_MAX
 * @head: head node of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	unsigned long int len = 0, i = 0;
	int pa_flag = 1;
	listint_t *current = NULL, *mid_node = NULL, *rev_cur = NULL;

	if (*head == NULL)
		return (1);
	current = *head, mid_node = *head;
	while (current)
	{
		if (len % 2 == 0)
			mid_node = mid_node->next; /*actually, it's behind middle node*/
		current = current->next, len++;
	}
	current = *head, rev_cur = lower_rev(&mid_node), mid_node = rev_cur;
	for (; i < len / 2; i++, current = current->next, rev_cur = rev_cur->next)
	{
		if (current->n != rev_cur->n)
		{
			pa_flag = 0;
			break;
		}
	}
	lower_rev(&mid_node);
	return (pa_flag);
}
