#include "lists.h"

/**
 * insert_node - A function that inserts a number into a
 * sorted singly linked list.
 * @head: pointer to list
 * @number: number to insert
 * Return: return a pointer to the newNode or NULL if fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = malloc(sizeof(listint_t));
	listint_t *currect = NULL;

	if (*head == NULL)
		return (NULL);
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (head == NULL || *head == NULL || (*head)->n >= newNode->n)
	{
		newNode->next = *head;
		*head = newNode;
	}

	for (current = *head; current->next != NULL && current->next->n < newNode->n;
			current = current->next)
		;

	newNode->next = current->next;
	current->next = newNode;

	return (newNode);
}
