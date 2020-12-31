cd=[5+i*0.5 for i in range(40)]
print cd
fd=[9/5*c+32 for c in cd]
print fd
zip(cd,fd)
for c,f in zip(cd,fd):
