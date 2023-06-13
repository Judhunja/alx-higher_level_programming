#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * reverse - pointer to funtion that reverses a singly linked list
 * @head: pointer to first node of the singly linked list
 * Return: address of the first node of the reversed linked list
 */
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
 * is_palindrome - checks if the elements of a linked list
 * form the same pattern when reversed and when forward
 * @head: pointer to pointer to the first node of the singly linked list
 * Return: 0 if the linked list is not palindrome, else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow_prev = *head, *slow = *head, *half_list = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow_prev = slow;
		slow = slow->next;
	}
	if (fast->next != NULL)
	{
		slow = slow->next;
	}
	half_list = reverse(slow);

	while (half_list != NULL)
	{
		if ((*head)->n != half_list->n)
		{
			return (0);
		}
		*head = (*head)->next;
		half_list = half_list->next;
	}
	slow = reverse(slow_prev->next);
	slow_prev->next = slow;

	return (1);
}
