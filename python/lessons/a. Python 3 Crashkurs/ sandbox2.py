def lists_01():
    # Removing elements of a list using the remove()-method:

    motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki']
    too_expensive = 'ducati'

    motorcycles.remove(too_expensive)

    print(motorcycles)
    print(f"\nA {too_expensive.title()} is too expensive for me.")

    pass


print(lists_01())
