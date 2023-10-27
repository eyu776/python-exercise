from movies import Movies

movies = Movies('./movies.txt')

def search_names(name: str) -> None:
  for movie in movies._movies:
    if movie['name'].lower().find(name) >= 0:
      print(movie['name'])
      continue

def search_cast(name: str) -> None:
  casts = []
  for movie in movies._movies:
    matched = False
    for cast in movie['cast']:
      if cast.lower().find(name) >= 0:
        matched = True
        casts.append(cast)
    if matched:
      print(movie['name'])
      print(str(casts))

def list_movies() -> None:
  for movie in movies._movies:
      print(movie['name'])

def menu() -> None:
  print("q: quit\nsn: search movie names\nsc: search casts\nlist: print all movie names")
  x = input("").strip().lower()
  if x == "q": return None
  else:
    if x == "sn":
      name = input("  enter a word to search: ").lower()
      search_names(name)
    elif x == "sc":
      name = input("  enter a word to search: ").lower()
      search_cast(name)
    elif x == "list":
      list_movies()
    print()
    menu()

menu()