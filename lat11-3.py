def distribusi_jam():

    n = input("Enter file name: ")
    d = {}

    with open(n, "r") as file:
        file = file.readlines()
        # print(file)
        for kalimat in file:
            if "From" in kalimat and not "From:" in kalimat:
                kalimat = kalimat.split()
                jam = kalimat[5].split(":")[0]
                # print(jam)

                if jam not in d:
                    d[jam] = 1
                else:
                    d[jam] += 1
        
        
        for key, value in d.items():
            print(key, value)



distribusi_jam()