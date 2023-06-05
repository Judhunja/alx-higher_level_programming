#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * check_cyle - checks if a linked list is a cycle
 * @list: element in the singly linked list
 * Return: 1 if a loop exists, 0 if there is no loop
 */

int check_cycle(listint_t *list)
{
    listint_t *current = list;
    listint_t *temp = list;

    while (current->next != NULL && temp->next->next != NULL)
    {
        current = current->next;
        temp = temp->next->next;

        if (current == temp)
        {
            return (1);
        }
    }
    return(0);
}
