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
                   

                   
>>>  1_PYTHON-TURTLE/2_TURTLE-SQUARE-LOOP.py
        Turtle was a popular way to introduce programming to kids :D
        Part of the original Logo programming language dveloped by Wally Feurzig and Seymour Papert in 1966.
        Thanks to turtle we can introduce how to Generate Geometry & Design like a Developer with Python :D !
        Being the same logic as we will apply inside our BIM Software when we generate AEC Elements ;)
        So let's turtle.forward(101) <3 !!!
"""

import turtle #Let's call to our turtle module pre-installed in our Python IDLE ;D !

turtle.fillcolor("red") #This time we wanna be RED ;D !
turtle.begin_fill() #From this point we wanna start to Fill with RED our Future Geometry ;D !
for i in range(4): #We think to repeat 4 times the comans was bit hard ! So let's use a loop for 4 times ;)
    turtle.forward(50) #Now we will draw an smaller square :D !
    turtle.left(90) #Remember to Rotate to the left ! Positive side due to the Right Hand Rule ;D !
turtle.end_fill() #And here we will stop with the fill ;)
