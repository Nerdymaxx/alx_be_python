fruits= ["orange", "apple", "sour sop", "mango", "banana"]
print(fruits[1])

book = {
    "author" : "mark manson",
    "title" : "the subtle art of not giving a fuck",
    "id" : "4",
    "year of release" : "2006",
    "genre": "self help",
}
def get_genre():
    print(f"a {book["genre"]} book authored by {book["author"]}")
        
    
get_genre()