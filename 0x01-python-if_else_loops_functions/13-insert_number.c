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
	listint_t *temp = *head;
	unsigned int pos = 0;
	unsigned int index = 0;

	temp = malloc(sizeof(listint_t));

	while (pos < index - 1 && temp->next != NULL)
	{
		temp = temp->next;
	}
	temp->n = number;

	return (temp);
}
