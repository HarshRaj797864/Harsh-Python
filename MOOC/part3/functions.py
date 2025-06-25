def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1

def squared(str, size):
    i = 0
    row = str*(size*size)
    while i < size:
        
        print(row[i*size:(i + 1)*size ])
        print()
        i += 1
        
squared("aybabtu",5)
        













chessboard(6)
