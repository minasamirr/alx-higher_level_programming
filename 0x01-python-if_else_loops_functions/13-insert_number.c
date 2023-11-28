#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current;
    if (!new_node) {
        return (NULL);
    }

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL) {
        *head = new_node;
        return (new_node);
    }

    for (current = *head; current; current = current->next) {
        if (current->n >= number) {
            break;
        }
    }

    if (current == *head) {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    if (current) {
        listint_t *prev = *head;
        while (prev->next != current) {
            prev = prev->next;
        }
        prev->next = new_node;
        new_node->next = current;
    } else {
        (*head)->next = new_node;
    }

    return (new_node);
}
