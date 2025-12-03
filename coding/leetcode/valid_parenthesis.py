
# create dict of parenth' with opening as value and closing as key
# stack is checked from left , we start from right if  a z cl comes check the respective val from dict and
# check if it is in the stack to its left side

# if we get a x opening next item must be x closing,instead if next is y op
# then next be y cl then x cl if not false


class solut:
    def parvalid(self,s: str) -> bool:
        stack = []
        cl_to_op = {")": "(", "]":"[", "}": "{"}

        for c in s:
            if c in cl_to_op: # checks keys ie closing
                if stack and stack[-1] == cl_to_op[c]: # checks if empty and last ele is opening
                    stack.pop()
                else:
                    return  False
            else:
                stack.append(c) 

        return True if not stack else False





