print('k')
def first(s):
 if len(s)<2:
    return "empty"
 else:
    return s[:2]+s[-2:]
def main():
  n=input("enter a string ")
  print(first(n))

if __name__=="__main__":
    main()