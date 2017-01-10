# -*- coding: utf-8 -*-

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    For P3, *you do not need to modify this method.*
    """
    return next((variable for variable in csp.variables if not variable.is_assigned()))


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    For P3, *you do not need to modify this method.*
    """
    return [value for value in variable.domain]


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P3, *you do not need to modify this method.*
    """
    return True


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P3, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.

    Refer to discussion 5 for more details on the algorithm
    """

    # TODO implement this
    # print type(csp.variables)
    # for item in csp.assignment.values():
        # print item  
    if is_complete(csp):
        # print "Done"
        return True
    
    var = select_unassigned_variable(csp)
    # print
    # print var
    index = find_var_index(csp,var)
    # print "index: ", index
    # print
    
    for value in order_domain_values(csp, var):
        # print "Var:",var
        # print "Value:", value
        
        if is_consistent(csp,var, value):
            csp.variables.begin_transaction()
            # for variable in csp.variables: print variable
            csp.assignment[var]= value

            csp.variables[index].assign(value)
            # print
            # for variable in csp.variables: print variable
            result =  backtrack(csp)
            if result: 
                return result
            csp.variables.rollback()

    # print "False"
    
    return False


def find_var_index(csp,var):
    for i in xrange(len(csp.variables)):
        if var.name == csp.variables[i].name:
            return i


def is_consistent(csp, variable, value):
    """Returns True when the variable assignment to value is consistent, i.e. it does not violate any of the constraints
    associated with the given variable for the variables that have values assigned.

    For example, if the current variable is X and its neighbors are Y and Z (there are constraints (X,Y) and (X,Z)
    in csp.constraints), and the current assignment as Y=y, we want to check if the value x we want to assign to X
    violates the constraint c(x,y).  This method does not check c(x,Z), because Z is not yet assigned."""

    for constraint in csp.constraints[variable]:
        if constraint.var2.is_assigned() and not constraint.is_satisfied(value,constraint.var2.value):
            return False
    return True

def is_complete(csp):
    """Returns True when the CSP assignment is complete, i.e. all of the variables in the CSP have values assigned."""

    # Hint: The list of all variables for the CSP can be obtained by csp.variables.
    # Also, if the variable is assigned, variable.is assigned() will be True.
    # (Note that this can happen either by explicit assignment using variable.assign(value),
    # or when the domain of the variable has been reduced to a single value.)

    # TODO implement this
    for  variable in csp.variables:
        if not variable.is_assigned():
            return False
    return True

