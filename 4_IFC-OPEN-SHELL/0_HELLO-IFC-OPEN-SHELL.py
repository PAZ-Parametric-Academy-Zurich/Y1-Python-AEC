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
                   

                   
>>>  0_HELLO-IFC-OPEN-SHELL.py
        Let's start with Python IFC Open Shell ;D > https://ifcopenshell.org/
        Installation > https://blenderbim.org/docs-python/ifcopenshell-python/installation.html 
        Donwload your version and paste the folder "ifcopenshell" in > C:\Program Files\Python311\Lib\site-packages
        Or install with pip > pip install ifcopenshell
        Now let's enjoy with our Hello IFC Open Shell ;D !
"""
#First steps in our IFC Open Shell > https://blenderbim.org/docs-python/ifcopenshell-python/hello_world.html
import ifcopenshell #Let's import our IFC module ;)
import os #os module to find our folder directory ;)

__location__ = os.path.realpath( #Here we will get our 0_HELLO-IFC-OPEN-SHELL.py file directory ;)
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

model = ifcopenshell.open(os.path.join(__location__, 'AC20-FZK-Haus.ifc')) #To open our donwloaded IFC inside the Project Folder ;)

print (model.schema) #Let's start printing IFC Schema information ;D !
print (model.by_id(1)) #Let's bring our 1 Data part by ID ;)
print (model.by_id(79107)) #Let's bring our Last Data Line by ID ;)


walls = model.by_type('IfcWall') #Filter by type of IFC Element > Wall
print(len(walls)) #Print the Nº of Walls ;)

wall = model.by_type('IfcWall')[0]
print(wall.is_a()) # Returns 'IfcWall'

print(walls) #Print All the Walls ;D!
#See you soon in our next Python AEC Workshop in PAZ Central ;D !
