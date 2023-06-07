#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to first node of the singly linked list
 * @number: number to be added to the linked list
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *ptr = *head;

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}

	while (ptr->next != NULL && ptr->next->n < number)
	{
		ptr = ptr->next;
	}
	new->next = ptr->next;
	ptr->next = new;

	return (0);
}
