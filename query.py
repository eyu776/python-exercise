from movies import Movies

movies = Movies('./movies.txt')

def menu() -> None:
  print("q: quit\nsn: search movie names\nsc: search casts\nlist: print all movie names")
  x = input("").strip().lower()
  if x == "q": return None
  else:
    if x == "sn":
      print("call search names function")
    elif x == "sc":
      print("call search casts function")
    elif x == "list":
      print("call list function")
    print()
    menu()

menu()