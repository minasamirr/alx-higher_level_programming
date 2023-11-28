#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    if (!new_node) {
        return (NULL);
    }

    new_node->n = number;
    new_node->next = NULL;

    if (!(*head)) {
        *head = new_node;
        return (new_node);
    }

    listint_t *current = *head;
    listint_t *prev = NULL;

    while (current && current->n < number) {
        prev = current;
        current = current->next;
    }

    if (prev) {
        prev->next = new_node;
    } else {
        *head = new_node;
    }

    new_node->next = current;

    return (new_node);
}

