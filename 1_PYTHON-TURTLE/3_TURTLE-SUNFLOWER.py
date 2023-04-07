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
                   

                   
>>>  1_PYTHON-TURTLE/3_TURTLE-SUNFLOWER.py
        Turtle was a popular way to introduce programming to kids :D
        Part of the original Logo programming language dveloped by Wally Feurzig and Seymour Papert in 1966.
        Thanks to turtle we can introduce how to Generate Geometry & Design like a Developer with Python :D !
        Being the same logic as we will apply inside our BIM Software when we generate AEC Elements ;)
        So let's turtle.forward(101) <3 !!!
"""

import turtle #Let's call to our turtle module pre-installed in our Python IDLE ;D !

turtle.fillcolor("yellow") #For our Sunflower we will select the color "yellow" ;)
turtle.begin_fill() #From this point I wanna fill my geometry with my "yellow" color ;)
for i in range(36): #For each element in range > 36 "i" iterate once and do ;)
    for i in range(4): #Identation is important to know we are inside a nested loop ;)
        turtle.forward(100) #This operation will be reapeated 4 x 36 = 144 times ;)
        turtle.left(90) #Remember to Rotate to continue our Loop for ;D !  
    turtle.left(10) #After each Square let's rotate 10º x 36 = 360º
turtle.end_fill() #And here the end of our Color Fill, outside the Nested Loop For ;D !
