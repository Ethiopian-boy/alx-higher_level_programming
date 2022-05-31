#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * nsert_node - inserts new node to linked list
 * @head: head of singly linked list
 * @number: input value
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp1, *tmp;

	tmp1 = *head;
	new_node = malloc(sizeof(listint_t));
	new_node->n = number;

	if (!new_node)
		return (NULL);
	if (!head)
	{
		*head = new_node;
		return (new_node);
	}
	if (tmp1->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (!tmp1 || tmp1->n <= number)
	{
		tmp = tmp1;
		tmp1 = tmp1->next;
	}
	if (tmp1->next == NULL)
	{
		tmp1->next = new_node;
		return (new_node);
	}
	new_node->next = tmp1;
	tmp->next = new_node;
	return (new_node);
}

