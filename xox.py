def name() :
        print("-------------------------------------------------")
        print("|[0]             |[1]            |[2]           |")
        print("         ",b[0],"    |       ",b[1],"    |       ",b[2],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        print("|[3]             |[4]            |[5]           |")
        print("|        ",b[3],"    |       ",b[4],"    |       ",b[5],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        print("|[6]             |[7]            |[8]           |")
        print("|        ",b[6],"    |       ",b[7],"   |       ",b[8],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        print("==================================================== :-) GAME OVER :-) ==================================================== ")


        
print("                                        ================                                                        ")
print("               \\\        //            ||              ||            \\\        //                             ")
print("                \\\      //             ||    ======    ||             \\\      //                              ")
print("                 \\\    //              ||   ||    ||   ||              \\\    //                               ")
print("                  \\\  //               ||   ||    ||   ||               \\\  //                                ")
print("                   \\\//                ||   ||    ||   ||                \\\//                                 ")
print("                   //\\\                ||   ||    ||   ||                //\\\                                 ")
print("                  //  \\\               ||   ||    ||   ||               //  \\\                               ")
print("                 //    \\\              ||   ||    ||   ||              //    \\\                              ")
print("                //      \\\             ||    ======    ||             //      \\\                             ")
print("               //        \\\            ||              ||            //        \\\                            ")
print("                                        ================                                                        ")

print("==================================================== ^^HIII WELCOME TO GAME^^ ==================================================== ")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <<THIS IS "XOX">> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
r = input("ENTER PLAYER_1 NAME : ")
shri = input("ENTER PLAYER_2 NAME : ")
print('*************************************************:: THE GAME START "ALL THE BEST" ::**********************************************')           
print(r," IS GIVEN AS 'X'")
print(shri," IS GIVEN AS 'o'")
b = [ '__','__','__','__','__','__','__','__','__' ]
K = 9

while True :
        
        print("-------------------------------------------------")
        print("|[0]             |[1]            |[2]           |")
        print("|        ",b[0],"    |       ",b[1],"    |       ",b[2],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        print("|[3]             |[4]            |[5]           |")
        print("|        ",b[3],"    |       ",b[4],"    |       ",b[5],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        print("|[6]             |[7]            |[8]           |")
        print("|        ",b[6],"    |       ",b[7],"    |       ",b[8],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        
        print(r," YOU CAN SELECT THE POSTION " )
        C = eval(input())
        if C >= 9 :
                print("ivalid input")
                print("enter valid input")
                C = eval(input())
                
        K = K - 1
        if b[C] == 'X ':
            print(" allready value exits ")
            print("enter new value ")
            C = eval(input())
        if b[C] == 'O ' :
            print(s," has already enterd that postion\nenter new postion")
            C = eval(input())
            
            
        b[C] = 'X '

        
             
        if b[0] == b[1] == b[2]== 'X ':
                print(r," is the Winner")
                name()
                exit()
        elif b[1] == b[4] == b[7]== 'X ':
                print(r," is the Winner")
                name()
                exit()
        elif b[2] == b[5] == b[8]== 'X ':
                print(r," is the Winner")
                name()
                exit()
        elif b[0] == b[4] == b[8]== 'X ':
                print(r," is the Winner")
                name()
                exit()
        elif b[2] == b[4] == b[6]== 'X ':
                print(r," is the Winner")
                name()
                exit()
        elif b[3] == b[4] == b[5]== 'X ':
                print(r," is the Winner ")
                name()
                exit()
        elif b[6] == b[7] == b[8]== 'X ':
                print(r," is the Winner")
                name()
                exit()
        elif b[0] == b[3] == b[6]== 'X ':
                print(r," is the Winner")
                name()
                exit()
        else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
        if(K == 0) :
            print("match draw")
            s = eval(input(" if u want  try again press 1 " ))  
            if s == 1 :
                     b = [ '__','__','__','__','__','__','__','__','__' ]
                     K = 9
                     continue
            else  :
                    print("game over ")
                    name()
                    exit()
        print("-------------------------------------------------")
        print("|[0]             |[1]            |[2]           |")
        print("|       ",b[0],"     |       ",b[1],"    |       ",b[2],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        print("|[3]             |[4]            |[5]           |")
        print("|       ",b[3],"     |       ",b[4],"    |       ",b[5],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        print("|[6]             |[7]            |[8]           |")
        print("|       ",b[6],"     |       ",b[7],"    |       ",b[8],"   |")
        print("|                |               |              |")
        print("-------------------------------------------------")
        
        print(shri," U SELECT THE POSTION " )
        D = eval(input())
        if D >= 9 :
                print("ivalid input")
                print("enter valid input")
                D = eval(input())
        
        if b[D] == 'O ':
            print(" allready value exits ")
            print(shri,"  ENTER THE NEW POSTION ")
            D = eval(input())
        if b[D] == 'X ' :
            print(" allready value exits ")
            print(r," HAS ALREADY ENTERD THE POSTION" )
            print(shri," ENTER THE NEW POSTION")
            D = eval(input())
            b[D] = 'O '
            
                
        b[D] = 'O '
        K = K - 1
        
        
        
        if b[0] == b[1] == b[2]== 'O ':
            print(shri," is the Winner")
            name()
            exit()
        elif b[1] == b[4] == b[7]== 'O ':
            print(shri," is the Winner")
            name()
            exit()       
        elif b[2] == b[5] == b[8]== 'O ':
            print(shri," is the Winner")
            name()
            exit()  
        elif b[0] == b[4] == b[8]== 'O ':
            print(shri," is the Winner")
            name()
            exit() 
        elif b[2] == b[4] == b[6]== 'O ':
            print(shri," is the Winner")
            name()
            exit()
        elif b[3] == b[4] == b[5]== 'O ':
            print(shri," is the Winner")
            name()
            exit()     
        elif b[6] == b[7] == b[8]== 'O ':
            print(shri," is the Winner")
            name()
            exit()  
        elif b[0] == b[3] == b[6]== 'O ':
            print(shri," is the Winner")
            name()
            exit()
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                         
            
            
