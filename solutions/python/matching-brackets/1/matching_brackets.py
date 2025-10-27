def is_paired(input_string):
    stack = []
    for i in input_string :
        if i in "{([" :
            stack.append(i) # add the open to the stack 
        elif i in "}])" :
            if not stack : # if the stack is null => False
                return False
            last = stack.pop() # if no jump in the if not stack => we take the last element as last and remove from stack
            # compare the close we take from elif with the last element we take
            if i == ")" and last != "(" : 
                return False
            if i == "}" and last != "{" :
                return False
            if i == "]" and last != "[" :
                return False 
        
        else : 
            continue

    return len(stack) == 0

# Exemple : 
# input_string = "{[])"
# For 1 : i = { => stack = ["{"]
# For 2 : i = [ => stack = ["{["]
# For 3 : i = ] => last = "[" ; stack = ["{"] => no jump in the condition => continue
# For 4 : i = ) => last = "{" ; stack = [] => jump in the first condition after stack.pop => return False
            
