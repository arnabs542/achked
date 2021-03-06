#!/usr/bin/env python3

STARTING_PAREN = '('


def find_max_length_of_matching_parentheses(brackets):

    if len(brackets) == 0:
        return 0

    stack = []
    start, prev_start, max_len = 0, 0, 0

    for i, bracket in enumerate(brackets):

        print("i:", i, ", c:", bracket, ", start:", start, ", prev:",
                prev_start, "max_len:", max_len)
        if bracket == STARTING_PAREN:

            stack.append(i)

        else:

            # bracket is closing
            if not stack:

                # stack is empty, found a closing paren but no open paren, advance to next char
                prev_start = i + 1

            else:

                # matching paren found, compute the length of the matching paren
                # if stack is empty - compute length from previous position,
		    # otherwise length of
                # matching substring is however far i has gotten from top of stack

                stack.pop()

                start = prev_start - 1 if not stack else stack[-1]
                
                size = i - start

                max_len = max(size, max_len)

    return max_len


#string = '(()()())'
string = '(()())(())'
# string = '()'

print(find_max_length_of_matching_parentheses(string))

