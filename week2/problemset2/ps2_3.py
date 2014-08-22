from __future__ import division

balance = 9999999
annualInterestRate = 0.18

lopay = balance / 12
hipay = balance * (1 + annualInterestRate / 12) ** 12 / 12


def pay(m, min_pay):
    if m == 1:
        ub = (balance - min_pay) * (1 + annualInterestRate / 12)
        return ub
    else:
        last_ub = pay(m - 1, min_pay)
        ub = (last_ub - min_pay) * (1 + annualInterestRate / 12)
        return ub
        
min_pay = (lopay + hipay) / 2
ub = pay(12, min_pay)
while abs(ub) > 0.01:
    ub = pay(12, min_pay)
    if ub > 0:
        lopay= min_pay
    else:
        hipay = min_pay
    min_pay = (lopay + hipay) / 2

print('Lowest Payment: %.2f' % min_pay)
