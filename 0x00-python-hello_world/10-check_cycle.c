#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (fast != NULL)
	{
		fast = fast->next;
		if (fast == NULL)
		{
			return (0);
		}
		fast = fast->next;

		slow = slow->next;

		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
