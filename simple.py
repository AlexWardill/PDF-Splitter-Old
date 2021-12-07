def write_n_lines(n):
    my_file = open("n-lines.txt", "w+")
    for i in range(n):
        my_file.write(f"Line {n}")
    my_file.close()