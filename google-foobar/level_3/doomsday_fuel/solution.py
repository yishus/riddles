from fractions import Fraction, gcd

def solution(m):
    if len(m) == 1:
        return [1, 1]
    
    absorbing = []
    non_absorbing = []
    for k in range(len(m)):
        if sum(m[k]) == 0:
            absorbing.append(k)
        else:
            non_absorbing.append(k)

    r = []
    q = []
    for na in non_absorbing:
        row_r = []
        row_q = []
        row_sum = sum(m[na])
        for i in range(len(m[0])):
            if i in absorbing:
                row_r.append(Fraction(m[na][i], row_sum))
            else:
                row_q.append(Fraction(m[na][i], row_sum))
        r.append(row_r)
        q.append(row_q)
    
    
    i = identity(len(q))
    
    i_minus_q = matrix_sub(i, q)
    f = getMatrixInverse(i_minus_q)
    fr = matrix_mul(f, r)
    denominator = lcmm(map(lambda x: x.denominator, fr[0]))
    res = list(map(lambda x: x.numerator * denominator / x.denominator, fr[0]))
    res.append(denominator)
    
    return res
    
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def lcmm(l):
	return reduce(lambda x, y: lcm(x, y), l)

def identity(size):
    i = []
    for n in range(size):
        row = [0] * size
        row[n] = 1
        i.append(row)
    
    return i


def matrix_sub(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            r = a[i][j] - b[i][j]
            row.append(r)
        res.append(row)

    return res


def matrix_mul(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            v = 0
            for k in range(len(a[0])):
                v += a[i][k] * b[k][j]
            row.append(v)
        res.append(row)

    return res


def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeterminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeterminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeterminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeterminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors