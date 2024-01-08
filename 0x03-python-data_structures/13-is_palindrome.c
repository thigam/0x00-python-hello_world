#include "lists.h"

/**
 * is_palindrome- Checks if a singly linked list is a palindrome
 * @head: Pointer to the first list element
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *previous;
	listint_t *subsequent;
	listint_t *rev_head;

	if (*head == NULL)
		return (1);

	previous  = NULL;
	current = *head;

	while (current != NULL)
	{
		subsequent = current->next;
		current->next = previous;
		previous = current;
		current = subsequent;
	}
	rev_head = previous;
	current = *head;

	while (current != NULL)
	{
		if (current->n != rev_head->n)
		{
			return  (0);
		}
		current = current->next;
		rev_head = rev_head->next;
	}
	return (1);
}

