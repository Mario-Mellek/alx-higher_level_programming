#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	size_t *temp = NULL;
	size_t i, j, len;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	for (len = 0; current != NULL; current = current->next, len++)
		;
	temp = malloc(sizeof(size_t) * len);
	if (temp == NULL)
		return (0);

	current = *head;

	for (i = 0; current != NULL; current = current->next)
	{
		temp[i] = current->n;
		i++;
	}

	for (j = 0; j < i / 2; j++)
	{
		size_t firstElement = temp[j];
		size_t lastElement = temp[i - j - 1];

		if (firstElement != lastElement)
		{
			free(temp);
			return (0);
		}
	}
	free(temp);
	return (1);
}
