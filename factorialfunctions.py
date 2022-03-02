def fact():
  n=int(input())
  r=int(input())
  n_fact=fact(n)
  r_fact=fact(r)
  n_r_fact=fact(n-r)
  a=n_fact//(r_fact*n_r_fact)
  print(a)
fact()