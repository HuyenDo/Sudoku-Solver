# -*- coding: utf-8 -*-



def is_consistent(csp, variable, value):
    """Returns True when the variable assignment to value is consistent, i.e. it does not violate any of the constraints
    associated with the given variable for the variables that have values assigned.

    For example, if the current variable is X and its neighbors are Y and Z (there are constraints (X,Y) and (X,Z)
    in csp.constraints), and the current assignment as Y=y, we want to check if the value x we want to assign to X
    violates the constraint c(x,y).  This method does not check c(x,Z), because Z is not yet assigned."""

    # TODO implement this
    # first_pos_constraints   = []   #(X,Y)
    # second_pos_constraints = []	  #(Y,X)
    # for constraint in csp.constraints:
    # 	#(X,Y)
    # 	if variable.name == constraint.var1.name and constraint.var2.is_assigned():
    # 		first_pos_constraints.append(constraint)
    # 	#(Y,X)
    # 	elif variable.name == constraint.var2.name and constraint.var1.is_assigned():
    # 		second_pos_constraints.append(constraint)

    # for constraint in first_pos_constraints :
    # 	if not constraint.is_satisfied(value, constraint.var2.value):
    # 		return False

    # for constraint in second_pos_constraints :
    # 	if not constraint.is_satisfied(constraint.var1.value, value):
    # 		return False

    # return True


    for constraint in csp.constraints[variable]:
    	if constraint.var2.is_assigned() and not constraint.is_satisfied(value,constraint.var2.value):
            return False
    return True

    

