import os
Databases = {}
os.chdir("Bababoi")
if 1>0:

    with open('sheet_names.txt', 'r') as sheet_file:

        for line in sheet_file:
            # noinspection PyBroadException
            try:
                print(line)
                with open(line.strip(), 'r') as sheet_cache:
                    print("yes")
                    hehe = []

                    for l in sheet_cache:
                        print(l)
                        b = []
                        a = l.strip().split(",")
                        print("ez", a)
                        for j in a:
                            print(j)
                            try:
                                j = float(j)

                            except:
                                j = str(j)
                                  
                            b.append(j)

                        hehe.append(b)
                Databases[line.split(".")[0]] = hehe
            except:
                pass

print(Databases)