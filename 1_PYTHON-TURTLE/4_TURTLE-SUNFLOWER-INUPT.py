"""
>>> PAZ_Academy = [["PAZ - Parametric Academy Zurich", "https://pazacademy.ch", "info@pazacademy.ch", "+41 44 243 62 16"],["PAZ Central" , "Niederdorfstrasse 77", "CH-8001 Zurich"]]

>>>  Y1 - Python AEC
        Python AEC is a full day Python course for Architects, Engineers and BIM professionals.
        Analyze, Optimize and Automatize with Python your normal day AEC workflows !
        

        
                     .::::::::::::::::::::::::::::::::::::::::::::::::::::::.                                                                                                                           
                  -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+.                                                                                                                       
                +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@#-                                                                                                                     
              .%@@@@*:                                                       -#@@@@+                                                                                                                    
              =@@@@-                                                           #@@@@.                                                                                                                   
              +@@@@.                                                           +@@@@.                                                                                                                   
              +@@@@.                                                           +@@@@.                                                                                                                   
              +@@@@.                                                           +@@@@.                                         .............               .......            ...................        
              +@@@@.                   :*+.             -*+                    +@@@@.                                         +@@@@@@@@@@@@@@%*-          @@@@@@@=           %@@@@@@@@@@@@@@@@@@.       
              +@@@@.                  =@@@%.           .@@@%.                  +@@@@.                                         +@@@@@@%%%%%@@@@@@#.       +@@@@@@@%.          #@@@@@@@@@@@@@@@@@=        
              +@@@@.                 :@@@@@-           =@@@@%.                 +@@@@.                                         +@@@@%.      =@@@@@@.     :@@@@@@@@@%                    =@@@@@#.         
              +@@@@.                .@@@@@@=           *@@@@@*                 +@@@@.                                         +@@@@%.       +@@@@@=    .@@@@+.%@@@@+                 .*@@@@@#           
           .-=%@@@@.                +@@@@@@-           +@@@@@@-                +@@@@*=:.                                      +@@@@%       :%@@@@@-    *@@@#  -@@@@@.               -%@@@@%=            
        .*@@@@@@@@@.                %@@@@@@:           -@@@@@@%                +@@@@@@@@%-                                    +@@@@@#****#%@@@@@@=    *@@@#    *@@@@#              #@@@@@#.             
       =@@@@@@@@@@@.               :@@@@@@%.           .@@@@@@@.               +@@@@@@@@@@%:                                  +@@@@@@@@@@@@@@@@*.    -@@@@:    .@@@@@+           .#@@@@@=               
      *@@@@@@@@@@@@.               =@@@@@@=             *@@@@@@:               +@@@@@@@@@@@@=                                 +@@@@@+======-:.       %@@@@%#%%%%@@@@@@-         -@@@@@@=                
     =@@@@@@@@@@@@@.               =@@@@@%              :@@@@@@-               +@@@@@@@@@@@@@-                                +@@@@%                =@@@@@@@@@@@@@@@@@%        +@@@@@%.                 
    .@@@@@@@@@@@@@@.               -@@@@@:               -@@@@@:               +@@@@@@@@@@@@@*                                +@@@@%.              :@@@@#--------=@@@@@#     .%@@@@@+.                  
    .@@@@@@@@@@@@@@.                #@@%.                 -@@@#                +@@@@@@@@@@@@@#                                +@@@@%.             :@@@@%          -@@@@@*   =@@@@@@@@@@@@@@@@@@%        
     #@@@@@@@@@@@@@.                .++                    :+=                 +@@@@@@@@@@@@@=                                +@@@@%              #@@@@-           *@@@@@. .@@@@@@@@@@@@@@@@@@@%        
     .%@@@@@@@@@@@@.            -+-.                           :++:            +@@@@@@@@@@@@%.                                 .....              ...:.             ....:   ....................        
      .%@@@@@@@@@@@.           -@@@@%*=:                  .-+#@@@@%            +@@@@@@@@@@@*                                                                                                            
        -#@@@@@@@@@.           .@@@@@@@@@@%%#***+++***#%@@@@@@@@@@#            +@@@@@@@@@*:                                                                                                             
           -+#@@@@@.            =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-            +@@@@%#+-                                                                                                                
              +@@@@.             *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+             +@@@@.                                                                                                                   
              +@@@@.              %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+              +@@@@.                                                                                                                   
              +@@@@.              .*@@@@@@@@@@@@@@@@@@@@@@@@@@@+               +@@@@.                                            .:       :-:       :     .:::.     .:::::.  :.     ::  :.    .:        
              +@@@@.                .+%@@@@@@@@@@@@@@@@@@@@@%=.                +@@@@.                                           .#*%.   *#-.:+#:   ##%.   =@=:-+#=  *%-:::. .@%-   =@@- :#*  -%-        
              +@@@@.                   -*%@@@@@@@@@@@@@@@%+.                   +@@@@.                                           *- *%. =@:        +* +%.  =@:   -@: *@---   :%+@: .#:@-   +%+*          
              +@@@@.                      .-+##%%%%%#*=-.                      +@@@@.                                          -@==+@+ -@:       -@+=+@+  =@:   -@: *%-::   :% *# *:.@-    +@           
              +@@@@.                                                           +@@@@:                                         :@=...=@. *%:  -%:.@=...-@- =@- .=@+  *%.     :%  #@# .@-    =%           
              +@@@@:                                                           *@@@@.                                         -=     --  :+++=. -=     -+ :++++-.   -+++++=  =  :+.  +:    :=           
              :@@@@%-                                                        .=@@@@#                                                                                                                    
                #@@@@@%#####################################################@@@@@@*                                                                                                                     
                 -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:                                                                                                                      
                   .=+*#####################################################*+-
                   

                   
>>>  1_PYTHON-TURTLE/4_TURTLE-SUNFLOWER-INPUT.py
        Turtle was a popular way to introduce programming to kids :D
        Part of the original Logo programming language dveloped by Wally Feurzig and Seymour Papert in 1966.
        Thanks to turtle we can introduce how to Generate Geometry & Design like a Developer with Python :D !
        Being the same logic as we will apply inside our BIM Software when we generate AEC Elements ;)
        So let's turtle.forward(101) <3 !!!
"""

import turtle #import module "turtle" in Python, we can find inside "C:\Program Files\Python311\Lib\turtle.py"

#Function input to "ask to the users what they want?" getting their inputs back ;)
polygon = int(input("Polygon sides(3): ")) #polygon will save the Polygon sides, point, line, triangle ...
side = int(input("Side Lenght(100) : ")) #Side will give us the Lenght of our Polygons having the final Size ;)
loops = int(input("How many loops(10) : ")) #Remember, remember more loops more time but more Turtle Art too ;D !
color = input("Favorite Color(red) : ") #Color like input write the correct name ;D !
working = print("Thanks for your inputs now I will work hard for your Turtle ART <3 !") #Turtle is a hard workers, like you :D !


turtle.fillcolor(color) #Now I will fill with my varible "color" string coming from the inputs ;D !
turtle.begin_fill() #When we wanna start to fill our Geometry ;)
for i in range(int(loops)): #The main Father Loop saying the number of total loops ;)
    for i in range(polygon): #Here our polygon definiton coming from inputs integer ;)
        turtle.forward(side) #Also the Units Steps are coming from Inputs ;)
        turtle.left(360/polygon)  #Now our rotation will depend on our Polygon ;D 
    turtle.left(360/loops) #And the Rotation on the number of Loops to get our Desired 360º loop
turtle.end_fill() #Fill all this previous Turtle Art <3 !

adios = '''
        @ @ @                   ___
       []___               ,,  // \\
      /    /\____         (_,\/ \_/ \_
(~)  /_/\_//____/\         \ \_/_\_/>
 |   | || |||__|||........./_/  /_/.............<3                                                  
 _______  ___    ___ ________  _______   ________     
|\   __  \|\  \  /  /|\   __  \|\  ___ \ |\   ____\    
\ \  \|\  \ \  \/  / | \  \|\  \ \   __/|\ \  \___|    
 \ \   ____\ \    / / \ \   __  \ \  \_|/_\ \  \       
  \ \  \___|\/  /  /__ \ \  \ \  \ \  \_|\ \ \  \____  
   \ \__\ __/  / /|\__\ \ \__\ \__\ \_______\ \_______\.
    \|__||\___/ / \|__|  \|__|\|__|\|_______|\|_______|.
         \|___|/                                       
                                                       
'''

adios_amigos = print(adios + "Let's continue with PAZ_Y1-Python-AEC, now Grasshopper & Python Love <3 !!!!" ) #Big big final for all our Python AEC Friends ;)
