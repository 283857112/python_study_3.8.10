from stack_ import SStack

strtext = "([dwf{1232}dwd[3232]ffdff)Lore]m ip]sum dolor sit amet, consectetur adipisicing elit.Porro tenetur accusamus sit, autem officia quae, (ex) fugiat {voluptatibus} aliquam {[reiciendis saepe re(cusandae) ipsum reprehenderit pla]}ceat. Quos quod enim, officiis vero."
s = SStack()

parents = "(){}[]"
wrong = []

for i in range(len(strtext)):
    c = strtext[i] 
    if c in ("(", "[", "{"):
        tuple01 = (i, strtext[i])
        s.push(tuple01)
    elif c in (")", "}", "]") and (not s.is_empty()):
        if c == ")" and s.top()[1] == "(":
            s.pop() 
        elif c == "]" and s.top()[1] == "[":
            s.pop()
        elif c == "}" and s.top()[1] == "{":
            s.pop()
        else:
            wrong.append((i,c))
    elif c in (")", "}", "]") and s.is_empty():
        wrong.append((i,c))


for item in wrong:
    print(item)    
    
