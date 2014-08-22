from __future__ import division

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total_p = 0


def pay(m):
    global total_p
    if m == 1:
        p = balance * monthlyPaymentRate
        total_p += p
        ub = (balance - p) * (1 + annualInterestRate / 12)
        print_results(m, p, ub)
        return ub
    else:
        last_ub = pay(m - 1)
        p = last_ub * monthlyPaymentRate
        total_p += p
        ub = (last_ub - p) * (1 + annualInterestRate / 12)
        print_results(m, p, ub)
        return ub
        

def print_results(m, p, ub):
    print('Month: %s' % m)
    print('Minimum monthly payment: %.2f' % p)
    print('Remaining balance: %.2f' % ub)

ub = pay(12)
print('Total paid: %.2f' % total_p)
print('Remaining balance: %.2f' % ub)
