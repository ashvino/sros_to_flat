#!/usr/bin/env python3
#####################################################################
#
# Purpose:  Script to generate flat config for NOKIA SROS from an
#			existing SROS indented config file.
#			SROS config file hierarchies are indented by 4 spaces.
#
#####################################################################

import re
import math
import sys

def pop(stack):
    """ Pop last item from stack, when exit are encountered in hierarchical config"""
    try:
        stack.pop()
    except Exception as err:
        print("ERROR: Unable to flush stack - %s" %err)

def output(stack):
    """ Out flat config lines """
    output = " ".join(stack)
    print(output)

def main():
    exit_detected = False
    conf_file = open(filename, 'r')
    data = conf_file.read()
    indent = 0

    for line in data.lstrip().splitlines():
        l = len(line) - len(line.lstrip())
        nxt_indent = math.ceil(float(l/4))

        if line.startswith(("#", "echo")) or line.strip() == "":
            pass
        elif line.strip() == "exit all":
            output(stack)
        else:
            if nxt_indent == 0 and line.strip() == "configure":
                new_line = str("/")+str(line.strip())
                stack.append(new_line)

            elif nxt_indent > indent:
                if line.strip() != "configure" and len(stack) == 0:
                    stack.insert(0, "/configure")
                stack.append(line.lstrip())

            elif nxt_indent == indent:
                if line.strip() != "exit":
                    if exit_detected:
                        stack.append(line.strip())
                    else:
                        if len(stack) != 0:
                            output(stack)
                            pop(stack)
                            stack.append(line.strip())
                        else:
                            stack.insert(0, "/configure")
                            stack.append(line.strip())
                    exit_detected = False

            else:
                if line.strip() == "exit":
                    if not exit_detected:
                        output(stack)
                        del stack[-2:]
                    else:
                        pop(stack)
                    exit_detected = True

                else:
                    output(stack)
                    exit_detected = False
                    pop(stack)
            indent = nxt_indent
    conf_file.close()


if __name__ == "__main__":
    filename = sys.argv[1]

    stack = []
    main()
