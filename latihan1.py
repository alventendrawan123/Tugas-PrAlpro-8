def banding_file(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        while True:
            line1 = f1.readline()
            line2 = f2.readline()
            if not line1 and not line2:
                break
            if line1!= line2:
                print(f"Difference at line {f1.tell()}:")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}")

banding_file('l.txt', 'n.txt')