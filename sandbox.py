with open("input.txt", 'r', encoding='utf-8') as inp:
    with open("answers.txt", 'r', encoding='utf-8') as f_answers:
        for line in inp:
            print (line.strip('\n') + f_answers.readline().strip('\n'))
