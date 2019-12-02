# =============================================================================
# Q1
# =============================================================================
print('----Q1---')
import sympy as sym
x = sym.symbols('x')

expr=x**2+x**3+21*x**4+10*x+1

print (expr.subs(x, 7) )

y = sym.symbols('y')
print(sym.expand( (x + y) ** 2 ))


print( sym.simplify(4*x**3+21*x**2+10*x+12))

print(sym.limit(1/(x**2),x,sym.oo))

i = sym.symbols('i')
n = sym.symbols('n')
print(sym.summation(2*i+i-1,(i,5,n)))


print( sym.integrate(sym.sin(x)+sym.exp(x)*sym.cos(x)+sym.tan(x),x))

z = sym.symbols('z')
print( sym.factor(x**3 +12*x*y*z+3*y**2*z) )

print( sym.solveset(x-4,x))


m1 = sym.Matrix([[5, 12, 40], [30, 70, 2]])
m2 = sym.Matrix([2,1,0])
print(m1*m2)

from sympy.plotting import plot,plot3d
plot(x**3+3, (x, -10, 10))
print('---k:-')
plot3d(x**2*y**3, (x, -6, 6), (y, -6, 6))

# =============================================================================
# Q2
# =============================================================================
print('----Q2---')

import xlsxwriter
workbook = xlsxwriter.Workbook('solve10.xlsx')
worksheet=workbook.add_worksheet()
worksheet.autofilter('A1:A5')

data=["This is Example","My first export example",1,2,3]

format1=workbook.add_format({'bold':True, 'font_color':'red'})
format2=workbook.add_format({'font_color':'black'})


worksheet.set_column('A:A', 20)
worksheet.write('A1', data[0],format1)
worksheet.write('A2', data[1], format2)
for x in range(2):
    worksheet.write(x+2, 0, x+1)
worksheet.write('A5', data[4],format1)
workbook.close()

# =============================================================================
# Q3
# =============================================================================
print('----Q3---')
from xlrd import open_workbook

wb=open_workbook('dd.xlsx')

for s in wb.sheets():
    print('sheet:',s.name)
    for row in range(s.nrows):
        values=[]
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(''.join(values))