#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the first node in the linked list
 * @number: integer
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *nnode = malloc(sizeof(listint_t));

	if (nnode == NULL)
	{
		return (NULL);
	}
	nnode->n = number;
	if (!node)
	{
		nnode->next = NULL;
		*head = nnode;
		return (nnode);
	}
	if ((*head)->n > number)
	{
		nnode->next = *head;
		*head = nnode;
		return (nnode);
	}

	while (node->next != NULL && node->next->n < number)
	{
		node = node->next;
	}
	nnode->next = node->next;
	node->next = nnode;
	return (nnode);
}
