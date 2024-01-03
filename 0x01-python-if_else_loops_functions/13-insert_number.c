#include "lists.h"

/**
 * insert_node- inserts a number into a sorted singly linked list
 *
 * @head: a pointer to the first node address
 * @number: the number to be stored in the new node
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	int i = 0;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	else
	{
		for (i = 0; i < 5; i++)
		{
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}
	
	return (new);
}
