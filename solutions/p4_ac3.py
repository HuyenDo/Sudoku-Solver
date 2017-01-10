# -*- coding: utf-8 -*-

from collections import deque


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise.

    Refer to discussion 5 for more details on the algorithm"""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

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
    while len(queue_arcs) != 0:
        (xi, xj) = queue_arcs.pop()
        if revise(csp, xi, xj):
            for constraint in csp.constraints[xi]:
                xk = constraint.var2
                arc = (xk,xi)
                queue_arcs.append(arc)
        if len(xi.domain) == 0:
            # print "acr not consistent"
            # print csp.variables
            return False
    # print csp.variables 
    return True



def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    removed = False
    constraint = csp.constraints[xi,xj][0]
    # print constraint
    for x in xi.domain:
        # print "X:" ,x
        satisfied = False
        for y in xj.domain:
            # print "Y: ",y
            if constraint.is_satisfied(x,y):
                # print "satisfied"
                satisfied = True
                break
        if not satisfied:
            # print "Remove: x = ", x
            xi.domain.remove(x)
            removed = True
            # print xi

    # print csp.variables
    return removed
    