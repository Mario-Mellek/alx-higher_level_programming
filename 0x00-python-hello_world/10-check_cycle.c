#include "lists.h"

/**
 * check_cycle - A function that checks if a
 * singly linked list has a cycle in it.
 *
 * @list: pointer to the list to check for cycles
 *
 * Return: returns 1 if it finds a cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle;
	listint_t *rabbit;

	if (list == NULL)
	{
		return (0);
	}

	turtle = list;
	rabbit = turtle;

	for (; turtle != NULL && rabbit != NULL && rabbit->next != NULL;
			turtle = turtle->next)
	{
		rabbit = rabbit->next->next;
		if (turtle == rabbit)
			return (1);
	}
	return (0);
}
