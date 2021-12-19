# 0x04. Linked list palindrome

**Technical interview preparation:**
 - You are not allowed to google anything
 - Whiteboard first

Write a function in C that checks if a singly linked list is a palindrome.
 - Prototype: *int is_palindrome(listint_t \*\*head);*
 - Return: 0 if it is not a palindrome, 1 if it is a palindrome
 - An empty list is considered a palindrome

### Compile Command:
gcc -Wall -Werror -Wextra -pedantic 0-main.c linked_lists.c 0-is_palindrome.c -o palindrome

### Execution Command:
./palindrome

### Notes
 - I came up with my own method
 - No malloc(), no buffer, no array of pointers
 - I tried my best (-ish) to optimize the run time
