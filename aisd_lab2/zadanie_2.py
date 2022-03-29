with open('output.csv', 'w+') as output_file:
    with open('zadanie2.csv', newline='') as f:
        reader = f.read()
        reader = reader.split("\n")

        ascii_words = []
        helper_file = []

        for row in reader:
            row = row.split(",", 1)
            if row[0] != "":
                if row[1] != "\r":
                    if row[0] != 'id':
                        row[0] = int(row[0])
                        row[1] = row[1].lower()
                        helper_file.append(row)

                        p = row[1].split(" ")
                        for word in p:
                            if len(word) >= 2:
                                if abs(ord(word[0]) - ord(word[1])) == 1:
                                    ascii_words.append((row[0], word))
                                    helper_file[-1][1] = helper_file[-1][1].replace(word, "", 1)

        helper_file.sort(key=lambda helper: helper[0])
        i = 1
        while i < len(helper_file):
            if helper_file[i][0] == helper_file[i-1][0]:
                helper_file[i][0] = helper_file[i-1][0]+1
            i += 1
        for line in helper_file:
            line[0] = str(line[0])
            line = ",".join(line)
            output_file.write(line)
            output_file.write('\n')

        print(ascii_words)