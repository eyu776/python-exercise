from movies import Movies

movies = Movies('./movies.txt')

def search_names(name: str) -> None:
  for movie in movies._movies:
    if movie['name'].lower().find(name) >= 0:
      print(movie['name'])

def menu() -> None:
  print("q: quit\nsn: search movie names\nsc: search casts\nlist: print all movie names")
  x = input("").strip().lower()
  if x == "q": return None
  else:
    if x == "sn":
      name = input("  enter a word to search for: ").lower()
      search_names(name)
    elif x == "sc":
      print("call search casts function")
    elif x == "list":
      print("call list function")
    print()
    menu()

menu()