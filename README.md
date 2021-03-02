JSON API Exercise 1
Write a Python script that:

Sends a GET request to https://jsonapiplayground.reyesoft.com/v2/authors?
page[size]=
Parses the JSON response
Prints a list of dictionaries containing:
o Each author’s name in a “name” key
o The number of books they have written in a “book_count” key
JSON API Exercise 2
Write a Python script that:

Pages through the endpoint below
Extends an author_list variable with each page of author data
Stops paging when either :
o There are no more authors
o 15 pages have been processed
Te l l s t h e u s e r w h i c h c o n d i t i o n a b o v e s t o p p e d t h e l o o p
Prints the author_list variable
Starting endpoint: https://jsonapiplayground.reyesoft.com/v2/authors?
page[size]=10&page[number]=
JSON API Exercise 3
Write a Python function that:

Accepts an author_id parameter
Sends a GET request to https://jsonapiplayground.reyesoft.com/v2/authors/{au-
thor_id}
Parses the JSON response
Returns a single dictionary containing:
o The author name in a “name” key
o The number of books they have written in a “book_count” key
Raises a meaningful exception if the author_id is not found
For bonus points, write a unit test to prove that your function raises the expected exception
if author_id is not found. You will need to mock the API response to achieve this.