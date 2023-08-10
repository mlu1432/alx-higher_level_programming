#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Checks if there is a cycle in a linked list
 * @list: linked list to check
 *
 * Return: If the list has a cycle, 1; otherwise, 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
