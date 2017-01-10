# -*- coding: utf-8 -*-
# from collections import OrderedDict
from Queue import PriorityQueue
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
    minDomainSize = 999999999
    returnVar = None

    # for var in csp.variables:
    #     domainSize = len(var.domain)

    #     # if domainSize == 0:
    #     #     return None
    #     if not var.is_assigned():
    #         # print "Domain: ",domainSize
    #         # print "constraints var: ", len(csp.constraints[var])
    #         # print "constraints return: ", len(csp.constraints[returnVar])
    #         if domainSize < minDomainSize:
    #             minDomainSize = domainSize
    #             # print "Variable: ", var
    #             # print "Min domain: ", minDomainSize
    #             returnVar = var
    #         elif domainSize == minDomainSize and len(csp.constraints[var]) > len(csp.constraints[returnVar]):
    #             returnVar = var 

    unassigned_variables = [var for var in csp.variables if not var.is_assigned()]

    minimum_domain_size = len(min(unassigned_variables, key = lambda var: len(var.domain)).domain)
    minimum_domain_variables = [ var for var in unassigned_variables if len(var.domain) == minimum_domain_size]


    l = []
    for var1 in minimum_domain_variables:
        count = 0
        for var2 in unassigned_variables:
            count += len(csp.constraints[var1,var2])
        l.append((var1, count))
    returnVar = max(l, key = lambda (var,count): count)[0]
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
