i=0
with open("the_scoring_file.txt","w") as f :
    for i in range(10):
        i=i+1
        if (i==10) :
            f.write(str(i))
        else: 
            f.write(str(i)+"\n")
        



for i in range(1,10) :
    with open("the_scoring_file.txt","r") as f :
        b=True
        with open(f"multiplication{i}.txt","w") as g :
            while b:
                chunk = f.readline()
                if chunk == '':
                    b=False
                    g.close()
                    f.close()
                else:
                    c=int(chunk)    
                    g.write(f"{i}X{c}={i*c}"+"\n")