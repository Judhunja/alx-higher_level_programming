#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the singly linked list
 * Return: 0 if there is no cycle, 1 if a cycle is in it
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;
	listint_t *fastptr = list;

	list = malloc(sizeof(listint_t));

	if (list == NULL)
	{
		return (0);
	}

	while (ptr->next != NULL && fastptr->next->next != NULL)
	{
		ptr = ptr->next;
		fastptr = fastptr->next->next;

		if (ptr == fastptr)
		{
			return (1);
		}
		else
		{
			return (0);
		}
	}
	return (0);
}
