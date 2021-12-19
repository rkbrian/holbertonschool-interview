#include "lists.h"

/**
 * nth_node - find the nth node of the linked list
 * @head: head node of the linked list
 * @n: index / position of the target node
 * Return: the nth node
 */
listint_t *nth_node(listint_t **head, int n)
{
	listint_t *current = NULL;
	int i = 0;

	current = *head;
	while (i < n)
		current = current->next, i++;
	return (current);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *  Note: mid_node optimizes runtime, workable for list size of ULONG_MAX.
 *  But this method's time complexity is still O(n^2) ¯\(O_o)/¯
 *  I came up with this method by myself so I'm ok with it.
 * @head: head node of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	unsigned long int len = 0, i;
        int pa_flag = 1;
	listint_t *current = NULL, *mid_node = NULL;

	if (*head == NULL)
		return (1);
	current = *head, mid_node = *head;
	while (current)
	{
		if (len % 2 == 0)
			mid_node = mid_node->next; /*actually, it's behind middle node*/
		current = current->next, len++;
	}
        current = *head;
	for (i = 0; i < len / 2; i++, current = current->next)
	{
		if (current->n != (nth_node(&mid_node, len / 2 - 1 - i))->n)
		{
			pa_flag = 0;
			break;
		}
	}
	return (pa_flag);
}
