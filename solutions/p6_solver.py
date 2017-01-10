# -*- coding: utf-8 -*-

from collections import deque

def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    # TODO copy from p3
    # print "Hello"
    if is_complete(csp):
        # print "Done"
        return True
    
    var = select_unassigned_variable(csp)
    # print
    # print "Var: ", var
    # index = find_var_index(csp,var)
    # print "index: ", index
    # print
    
    for value in order_domain_values(csp, var):
        # print "Var:",var
        # print "Value:", value
        
        if is_consistent(csp,var, value):
            csp.variables.begin_transaction()
            # for variable in csp.variables: print variable 
            # print
            var.assign(value)
            csp.assignment[var]= value
            if inference(csp, var):
                # print
                # for variable in csp.variables: print variable
                result =  backtrack(csp)
                if result: 
                    return result
            # print "rollback"
            csp.variables.rollback()
    # print csp.assignment
    return False


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise.  Note that this method does not
    return any additional variable assignments (for simplicity)."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    # TODO copy from p4
    # queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    # TODO implement this
    # print len(queue_arcs)
    # print type(queue_arcs.pop()[0]) 
    # print len(queue_arcs)
    # (v1,v2) = queue_arcs.pop()
    # for constraint in csp.constraints:
    #     print constraint
    # print
    # print csp.constraints[v2,v1][0]
    # print queue_arcs
    # print csp.variables
    while queue_arcs:
        (xi, xj) = queue_arcs.pop()
        if revise(csp, xi, xj):
            if len(xi.domain) == 0:
                # print "acr not consistent"
                # print csp.variables
                return False
            for constraint in csp.constraints[xi]:
                xk = constraint.var2
                arc = (xk,xi)
                # if not arc in queue_arcs:
                queue_arcs.append(arc)
        
    # print csp.variables 
    return True

def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    if not xj.is_assigned():
        return False
    # removed = False

    # print constraint
    if xj.domain[0] in xi.domain:
        xi.domain.remove(xj.domain[0])
        return True
    # print csp.variables
    return False

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """

    # TODO implement this
    # print csp.constraints   
    returnVar = None

    unassigned_variables = [var for var in csp.variables if not var.is_assigned()]

    minimum_domain_size = len(min(unassigned_variables, key = lambda var: len(var.domain)).domain)
    minimum_domain_variables = [ var for var in unassigned_variables if len(var.domain) == minimum_domain_size]


    l = []
    for var1 in minimum_domain_variables:
        count = 0
        for var2 in unassigned_variables:
            count += len(csp.constraints[var1,var2])
        l.append((var1, count))
    returnVar = min(l, key = lambda (var,count): count)[0]
    # print l
    return returnVar


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """

    # # TODO implement this
   
    l = []
    # print var.domain
    for value in variable.domain:
        # print value
        count = 0
        for cons in csp.constraints[variable]:                               
            if value in cons.var2.domain:
                count += len(cons.var2.domain) -1
            else: count += len(cons.var2.domain)
        # print counter, value
        l.append((value, count))                                         

    # ordered_domain =[value for value,_ in sorted(l, key=lambda x: x[1])]
    ordered_domain =[value for value,_ in sorted(l, key=lambda x: x[1])][::-1]
    # print ordered_domain
    return ordered_domain

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

    

