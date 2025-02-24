# Fix order of books with their given widths and heights to be placed on shelves with fixed width.
# Goal is to minimize the total height of the book shelf, i.e. the sum of heights of the tallest book on each shelf is minimized.

def optimize_lib_space(book_heights, book_widths, shelf_width_max):
    assert len(book_heights) == len(book_widths), "Number of books and their widths should be equal"

    n_books = len(book_heights)
    c = [0] * (n_books + 1) # c[i] will store the minimum height of the whole library for the books bi to bn
    c[n_books-1] = book_heights[n_books-1] # if we have only the last book, then the height of the library is the height of the last book
    last = [n_books-1] * n_books # last[i] will store the index of the last book on the shelf where the ith book is placed

    for i in range(n_books-2, -1, -1): # iterate from the second last book to the first book
        shelf_width = book_widths[i] 
        shelf_height = book_heights[i]
        last[i] = i # if the current shelf has only the ith book then the last book on the shelf is the ith book
        c[i] = shelf_height + c[i+1] # current shelf has only the ith book (bi) and the next books are placed on the next shelves
        for k in range(i+1, n_books): # current shelf has the books from bi to bk - check for all possbile k.
            shelf_width += book_widths[k] # total book width on the current shelf
            if shelf_height < book_heights[k]: # if the newly considered k-th book is taller than the current shelf height
                shelf_height = book_heights[k] # then the shelf height is the height of the k-th book
            if shelf_width <= shelf_width_max and shelf_height + c[k+1] < c[i]: # if shelf width constraint is respected and current k split is better than the previous best split
                c[i] = shelf_height + c[k+1]
                last[i] = k # we found out that having the books from bi to bk on the current shelf is better than the previous best split, so last book on the shelf is k now
    
    ####### PRINT RESULTS #######
    print("Library Height:", c[0])
    
    # Print results
    prev = last[0]
    shelf = 1
    books = []
    for i, last_idx in enumerate(last):
        if last_idx == prev:
            books.append(i+1)
        else:
            print(f"Shelf {shelf}: Books {books}")
            books = []
            books.append(i+1)
            shelf += 1
            prev = last_idx
    print(f"Shelf {shelf}: Books {books}")

    return c[0], last

if __name__ == "__main__":
    import random 

    book_heights = [random.randint(1, 7) for _ in range(5)] 
    book_widths = #[random.randint(1, 7) for _ in range(5)]
    shelf_width = 10
    print("Book Heights: ", book_heights)
    print("Book Widths: ", book_widths)
    print("Shelf Width: ", shelf_width)
    
    optimize_lib_space(book_heights, book_widths, shelf_width)

