rows = 10
mod = 10

def pascal_triangle(n, mod=1):
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    for i in range(1, n):
        # Start each new row with a 1
        prev_row = triangle[-1]
        new_row = [1]
        
        # Calculate middle elements by summing adjacent values from prev_row
        for j in range(1, i):
            new_row.append((prev_row[j-1] + prev_row[j]) % mod)
            
        # End each new row with a 1
        new_row.append(1)
        triangle.append(new_row)
        
    return triangle

# print(pascal_triangle(6, 10))
# print("=====================")

print(f"Pascal's triangle in mod({str(mod)}) up to row {rows}")
print("To change, modify the variables at the top of the file.")

def print_triangle(triangle):
    for i in range(len(triangle)):
      print("| ", end="")
      spaces = ""
      for j in range(len(triangle) - (i + 1)):
        spaces += " "
      print(spaces, end="")
      print(
      str(triangle[i])
      [1:-1]
      .replace(",","") + spaces + " | " + str(i+1))

print_triangle(pascal_triangle(rows,mod))