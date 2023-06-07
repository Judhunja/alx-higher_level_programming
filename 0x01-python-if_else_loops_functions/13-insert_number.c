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
	listint_t *ptr = *head;

	while (ptr->next != NULL && *head != NULL)
	{
		ptr = ptr->next;
	}
	ptr->n = number;
	return (0);
}
