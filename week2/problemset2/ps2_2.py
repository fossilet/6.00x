from __future__ import division

balance = 9999999
annualInterestRate = 0.18
min_pay = 10


def pay(m, min_pay):
    if m == 1:
        ub = (balance - min_pay) * (1 + annualInterestRate / 12)
        return ub
    else:
        last_ub = pay(m - 1, min_pay)
        ub = (last_ub - min_pay) * (1 + annualInterestRate / 12)
        return ub
        
ub = pay(12, min_pay)
while ub > 0:
    min_pay += 10
    ub = pay(12, min_pay)

print('Lowest Payment: %d' % min_pay)
