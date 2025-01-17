'''
Created on 2024. 12. 3.

@author: user
'''
num1 = 123;

print("%d" % 123);
print("%5d" % 123);
print("%05d" % num1);
print(" ", num1);

print("%f" % 123.45);
print("%.2f" % 123.45);

print("%c" % "안");
print("%s" % "안녕");

print("{0:d} {1:d} {2:d}".format(100, 200, 300));
print("{2:d} {1:d} {0:d}".format(100, 200, 300));