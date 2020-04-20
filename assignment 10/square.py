
 ///
 def print_line1(n, m) :
    # Print the starting colum of the box as a '+' for n smaller boxes
    for i in range(1, n+1) :
        print('+', end='')

        # Print the inner column as a '-' and a width of m
        for j in range(1, m+1) :
            print('-', end='')

     # Finish the row by closing it with a '+'
     print('+')


 # print_line2 - prints an empty box row with n smaller boxes of width m
 ///
 def print_line2(n, m) :
 # Print the starting column of the box as a '|' for n smaller boxes
  for i in range(1, n+1) :
      print('|', end='')

      # Printthe inner columns as a ' ' and a width of m
      for j in range(1, m+1) :
          print(' ', end='')

   # Finish the row by closing it with a '|'
   print('|')


   # print_box - prints a box with n smaller boxes width m
 ///
 def print_box(n, m) :
    # Print the starting row of the box as line 1, for n small boxes
    for i in range(1, n+1) :
        print_line2(n, m)

        #Finish the large box with line 1
        print_line1(n, m)

    #Finish the large box with line 1
    print_line1(n, m)


    ///
    print_box(2,4)
