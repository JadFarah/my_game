class Game:
    def __init__(self,name):
        self.name= name  # Initializes the player's name
        self.location= "Lobby"  # Starting location of the player
        self.inventory= []  # Player's inventory to hold collected items
        self.maps= {"Bulgaria": ["Bulgaria's Airport", "Bulgaria's library", "father's lab", "Railway station"], 
            "Turkey": ["Railway station in Turkey", "home", "kitchen", "father's room", "backyard", "mountain", "large rock"] }
        self.file = open("c:/Users/hunte/Desktop/testing_file.txt", "a", encoding="utf-8")  # Opens the log file in append mode
        self.file.write("\n=== New Game Session ==\n")  # Adds a session header
        
    def move(self,new_location):
        self.location= new_location  # Updates the player's current location
        print(f"\n You moved in {new_location}.")  # Informs the player about the new location
        self.file.write(f"Moved to: {new_location}\n")  # Logs the move
        
    def pick(self,item):
        if len(self.inventory)<4:  # Checks if inventory has less than 4 items
            self.inventory.append(item)  # Adds the item to the inventory
            print(f"\n {item} added to your inventory.")
            self.file.write(f"Picked: {item}\n")  # Logs the picked item
        else:
            print("\n Sorry...your inventory is full.")  # Restricts adding more items when inventory is full
            self.file.write("Attempted to pick item but inventory is full\n")  # Logs inventory full
    
    def drop(self,item):
           self.inventory.remove(item)  # Removes the specified item from the inventory
           print(f"\n {item} dropped from your inventory.")
           self.file.write(f"Dropped: {item}\n")  # Logs the dropped item
         
    def check(self):
        if self.inventory:  # Checks if inventory is not empty
            print(f"\n Your inventory contains {self.inventory}.")  # Display the items in the inventory
            self.file.write(f"Checked inventory: {self.inventory}\n")  # Logs inventory check
        else:
            print("\n Your inventory is empty.")  # Indicates that the inventory is empty
            self.file.write("Checked inventory: empty\n")  # Logs empty inventory
            
    def check_map(self,country):
        if country in self.maps:  # Checks if the map for the specified country is available
            print(f"\n Map of {country}: {', '.join(self.maps[country])}")  # Display the map for the country
            self.file.write(f"Viewed map of {country}\n")  # Logs map view
        else:
            print("\n Map not available for the selected country.")  # Indicates unavailable map
            self.file.write(f" Attempted to view map of {country}: not available\n")  # Logs unavailable map
            
         
        
    def play(self):
        # Indroduces the game and provides the player with initial instructions
        print(f"\n Welcome {self.name} to my game, Through this game, you will do your best to get the treasure, to get to the treasure, you must solve some puzzles that vary between medium and hard to get through the different stages, through the game, you will discover 10 different places, and you can pick up a maximum of 4 varied items to overcome obstacles. You can interact with the game by offering text options such as capturing items, solving puzzles or navigating sites. Win once you solve all the puzzles and get the treasure.")
        self.file.write(f"Player Name: {self.name}\n")  # Logs player name


        while True:  # Main game loop
            
            if self.location=="Lobby":  # Handles the logic for the Lobby location
                select=input("\n Now Assaf has to be at the airport in Bulgaria, do you want to continue or leave??: ").strip().lower()
                self.file.write(f"Location: Lobby, Input: {select}\n")  # Logs input
                if select=="continue":  # Moves the player to the Bulgaria Airport
                    self.move("Bulgaria Airport")
                elif select=="leave":  # Ends the game
                    print("Thank you for playing!")
                    self.file.write("Game ended by player\n")  # Logs game end
                    break
                else:
                    print("\n Invalid choice. please try again")  # Handles invalid logic
                    self.file.write("Invalid choice in Lobby\n")  # Logs invalid input
                    
            elif self.location=="Bulgaria Airport":
                while True:
                   select=input("\n Help Assaf find an old suitcase at the airport, there are three rooms to search... Room1 or Room2 or Room3: ").strip().lower()
                   self.file.write(f"Location: Bulgaria Airport, Input: {select}\n")
                   if select=="room1":  # Room 1 does not have the suitcase
                       print("Not here!!")
                   elif select=="room2":  # Room 2 does not have the suitcase
                       print("Try again:)")
                   elif select=="room3":  # Room 3 has the suitcase
                       while True:
                          choice=input("\n ***The old suitcase is here***... it has a map of Bulgaria, a secret key, and message. Pick them up by typing 'Claim': ").strip().lower()
                          self.file.write(f"Player selection: Room 3, Input: {choice}\n")
                          if choice=="claim":  # Player claims the items in the suitcase
                             self.pick("map of Bulgaria")
                             self.pick("secret key")
                             self.pick("message")
                             print("\n The message you picked up says: everything starts from my roots, search for the numbers in the City of Knowledge!!")
                             while True:
                                 country=input("\n Enter the country name to view its map: ").strip().capitalize()
                                 self.file.write(f"Player selection: Claim, Input: {country}\n")
                                 if country=="Bulgaria":  # Display the map of Bulgaria
                                    self.check_map(country)
                                    while True:
                                       library=input("\n Assaf should go to the City of Knowledge, what does it mean, Bulgaria's library or school??: ").strip().lower()
                                       self.file.write(f"Player selection: Bulgaria, Input: {library}\n")
                                       if library=="bulgaria's library":  # Moves the player to the library
                                          self.move("Bulgaria's library")
                                          break
                                       elif library=="school":  # Incorrect choice for the City of Knowledge
                                          print("wrong choice")
                                          self.file.write("Wrong choice in Bulgaria Airport\n")
                                       else:
                                          print("\n Invalid choice. please try again")  # Handles invalid inputs
                                          self.file.write("Invalid choice. please try again\n")
                                    break
                                 else:
                                    print("\n Invalid choice. please try again")  # Handles invalid inputs
                                    self.file.write("Invalid choice in country\n")
                             break
                          else:
                             print("\n Invalid choice. please try again")  # Handles invalid inputs
                             self.file.write("Invalid choice. please try again\n")
                       break
                   else:
                      print("\n Invalid choice. please try again")  # Handles invalid inputs
                      self.file.write("Invalid choice. please try again\n")

                      
            elif self.location=="Bulgaria's library":
                while True:
                   select=input("\n There are four shelves, look for a wooden box... Shelve1 and Shelve2 and Shelve3 and Shelve4: ").strip().lower()
                   self.file.write(f"Location: Bulgaria's library, Input: {select}\n")
                   if select=="shelve1":
                       print("Not here")
                   elif select=="shelve2":
                       print("Not here")
                   elif select== "shelve3":
                        print("Not here")
                   elif select=="shelve4":
                       while True:
                          choice=input("\n ***The wooden box is here***... but It's locked, open it with the secret key by typing 'Open': ").strip().lower()
                          self.file.write(f"Player selection: Shelve4, Input: {choice}\n")
                          if choice=="open":
                             self.drop("secret key")
                             while True:
                                box= input("it has a physics textbook and on its cover a note of 1967.. starting year, and UV lamp, collect the UV lamp by typing its name: ").strip().lower()
                                self.file.write(f"Player selection: open, Input: {box}\n")
                                if box=="uv lamp":
                                   self.pick("UV lamp")
                                   while True:
                                      lab= input("Since Assaf's father is a physicits, where can we go to continue?? Father's lab or Hospital: ").strip().lower()
                                      self.file.write(f"Player selection: UV lamp, Input: {lab}\n")
                                      if lab=="father's lab":
                                         self.move("father's lab")
                                         break
                                      elif lab=="hospital":
                                         print("\n Wrong choice")
                                         self.file.write("Wrong choice in Bulgaria's library\n")
                                      else:
                                         print("\n Invalid choice. please try again")
                                         self.file.write("Invalid choice. please try again\n")
                                   break
                                else:
                                   print("\n Invalid choice. please try again")
                                   self.file.write("Invalid choice. please try again\n")
                             break
                          else:
                              print("\n Invalid choice. please try again")
                              self.file.write("Invalid choice. please try again\n")
                       break
                   
                   else:
                      print("\n Invalid choice. please try again")
                      self.file.write("Invalid choice. please try again\n")
                      
                      
            elif self.location=="father's lab":
                has_pistol=False
                has_uv_lamp=False
                
                while True:
                   select=input("\n In the lab, there is a pistol on the table, pick it up, and next to it, a piece of paper with the symbol Φ written on it. But this code is incomplete, what item should you use to show the full code??? you can check your inventory by typing 'Show inventory': ").strip().lower()
                   self.file.write(f"Location: father's lab, Input: {select}\n")
                   if select=="show inventory":
                       self.check()
                   elif select=="pistol":
                       if has_pistol:
                           print("\n You have already picked up the pistol.")
                           self.file.write("Attempted to pick pistol but already has it\n")
                       else:
                          self.pick("pistol")
                          has_pistol=True
                          print("The pistol you picked it up has four numbers engraved on it: 2-4-3-3. These numbers will be usefull in the railway station in Turkey and in the end.")
                          self.file.write("Picked pistol with engraved numbers 2-4-3-3{select}\n")
                   elif select=="uv lamp":
                       if not has_pistol:
                           print("\n You must pick up the pistol first before UV lamp.")
                           self.file.write("Attempted to pick UV lamp without picking pistol\n")
                       elif has_uv_lamp:
                           print("\n You have already picked up UV lamp.")
                           self.file.write("Attempted to pick UV lamp but already has it\n")
                       else:
                          self.drop("UV lamp")
                          has_uv_lamp=True
                          print("\n Your full code is Φ34")
                          print("You can now continue the mission.")
                          self.file.write("Picked UV lamp and reveald full code Φ34\n")
                   else:
                       print("\n Invalid choice. please try again. ")
                       self.file.write("Invalid choice in father's lab\n")
                       
                       
                   if has_pistol and has_uv_lamp:    
                       while True:
                          station= input("\n After completing his mission in Bulgaria, Assaf must return to Turkey to complete the rest of the mission. Where should he go?? 'Railway station' or 'looking for a taxi': ").strip().lower()
                          self.file.write(f"Input at father's lab exit: {select}\n")
                          if station== "railway station":
                              while True:
                                 bag= input("\n *****You are on your way to the railway station, but a secret group is chasing you to capture you and collect all the information you've gathered. Search for an item in your inventory to get rid of them*****...: ")
                                 self.file.write(f"Chased secret group, Input: {bag}\n")
                                 if bag=="pistol":
                                    print("\n Well done, you got rid of them. You are now at the railway station.")
                                    self.move("Railway station")
                                    self.file.write("Succesfully escaped and moved to Railway station\n")
                                    break
                                 elif bag=="map of Bulgaria":
                                    print("****Game over... all the information was taken from you and you were eliminated****")
                                    self.move("lobby")
                                    self.file.write("Game over: player failed during chase\n")
                                    exit()
                                 elif bag=="message":
                                    print("****Game over... all the information was taken from you and you were eliminated****")
                                    self.move("lobby")
                                    self.file.write("Game over: player failed during chase\n")
                                    exit()
                                 else:
                                    print("\n Invalid choice. please try again.")
                                    self.file.write("Invalid choice during chase\n")
                              break
                          elif station=="looking for a taxi":
                             print("\n Wrong choice.")
                             self.file.write("Wrong choice: looked for taxi instead of railway station\n")
                          else:
                             print("\n Invalid choice. please try again.")
                             self.file.write("Invalid choice at father's lab exit\n")
                       break
                   
                    
            elif self.location=="Railway station":
                while True:
                   puz=input("\n You are now about to travel to Turkey, but there's a small puzzle you need to solve first: arrange the tickets that have these symbols E-D-V: ")
                   self.file.write(f"Location: Railway station, Input: {puz}\n")
                   if puz=="V-E-D":
                       while True:
                          print("\n You need to leave all your items at the railway station to proceed.")
                          self.drop("map of Bulgaria")
                          self.drop("message")
                          self.drop("pistol")
                          self.move("Railway station in Turkey")
                          break
                       break
                   else:
                      print("\n Invalid choice. please try again")
                      self.file.write("Invalid choice. please try again\n")
                      
                      
            elif self.location=="Railway station in Turkey":
                while True:
                   code=input("\n Remember the code engraved on the pistol, enter it to pass the guard and obtain the map of Turkey: ")
                   self.file.write(f"Location: Railway station in Turkey, Input: {code}\n")
                   if code=="2-4-3-3":
                      self.pick("map of Turkey")
                      while True:
                          country=input("\n Enter the country name to view its map: ").strip().capitalize()
                          self.file.write(f"Player selection: 2-4-3-3, Input: {country}\n")
                          if country=="Turkey":
                             self.check_map(country)
                             while True:
                                home=input("\n You did a good job in Bulgaria; you should go home to get some rest. Type 'home': ")
                                self.file.write(f"Player selection: Turkey, Input: {home}\n")
                                if home== "home":
                                  self.move("home")
                                  print("\n Enjoy time with your family and get some rest.")
                                  break
                                else:
                                   print("\n Invalid choice, please try again")
                                   self.file.write("Invalid choice. please try again\n")
                             break
                          else:
                            print("\n Invalid choice. please try again.")
                            self.file.write("Invalid country choice. please try again\n")
                      break      
                   else:
                      print("\n Invalid choice. please try again.")
                      self.file.write("Invalid code choice. please try again\n")
                      
            elif self.location=="home":
                while True:
                   kit=input("\n Now you must be ready to complete your father's mission. When you're hungry, where do you go??: ")
                   self.file.write(f"Location: Home, Input: {kit}\n")
                   if kit=="kitchen":
                      self.move("kitchen")
                      break
                   else:
                      print("\n Invalid choice. please try again.")
                      self.file.write("Invalid place choice. please try again\n")
                      
            elif self.location=="kitchen":
                while True:
                   salt=input("\n Alright, now you need to look for a clue in the kitchen. There are two cabinets. Which one do you want to open first? 'Cabinet 1' or 'Cabinet 2': ").strip().lower()
                   self.file.write(f"Location: Kitchen, Input: {salt}\n")
                   if salt=="cabinet 1":
                       while True:
                          nothing=input("\n In Cabinet 1, there is sugar, vinegar, and coffee. Is there any clue or hint?? 'Yes' or 'No': ").strip().lower()
                          self.file.write(f"Player selection: cabinet 1, Input: {nothing}\n")
                          if nothing=="yes":
                             print("\n Wrong choice, there is no clue or hint.")
                             self.file.write("Wrong choice\n")
                          elif nothing=="no":
                             print("\n Alright, you need to search in Cabinet 2.")
                             break
                          else:
                             print("\n Invalid choice. please try again.")
                   elif salt=="cabinet 2":
                       while True:
                          s=input("\n In Cabinet 2, there is pepsi, milk, and salT. Is there any clue or hint?? 'Yes' or 'No': ").strip().lower()
                          self.file.write(f"Player selection: cabinet 2, Input: {s}\n")
                          if s=="yes":
                              while True:
                                 t=input("\n What is the clue or hint that you saw??: ")
                                 self.file.write(f"Player selection: yes, Input: {t}\n")
                                 if t=="T":
                                    print("\n Well done, remember it well, you will need it.")
                                    while True:
                                       f_room=input("\n I know you miss your father. To see his memories, where do you go?? 'father's room' or 'your room': ")
                                       self.file.write(f"Player selection: T, Input: {f_room}\n")
                                       if f_room== "father's room":
                                          self.move("father's room")
                                          print("\n Well done.")
                                          break
                                       elif f_room== "your room":
                                          print("\n Wrong choice.")
                                          self.file.write("wrong room. please try again\n")
                                    break     
                                 else:
                                    print("\n Invalid choice. please try again.")
                                    self.file.write("wrong character. please try again\n")
                              break
                          elif s=="no":
                             print("\n Try again, focus carefully.")
                             self.file.write("wrong choice. please try again\n")
                       break      
                   else:
                      print("\n Invalid choice. please try again.")
                      self.file.write("Invalid choice. please try again\n")
                      
            elif self.location=="father's room": 
                while True:
                   table=input("\n In your father's room, there is a table with a phrase on it: 'The key to Tu{R}key is here'. Is there any hint or clue in this sentence??  'Yes' or 'No': ").strip().lower()
                   self.file.write(f"Location: father's room, Input: {table}\n")
                   if table== "yes":
                       while True:
                          r=input("\n What is the clue or hint that you saw??: ")
                          self.file.write(f"Player selection: yes, Input: {r}\n")
                          if r=="R":
                              while True:
                                 print("\n Well done, remember it well, you will need it.")
                                 tree=input("\n Now you will go to the backyard of the House. Type 'OK' to continue: ").strip().lower()
                                 self.file.write(f"Player selection: R, Input: {tree}\n")
                                 if tree== "ok":
                                    self.move("backyard")
                                    print("\n Well done.")
                                    break
                              break
                          else:
                            print("\n Invalid choice. please try again.")
                            self.file.write("wrong character. please try again\n")
                       break     
                   elif table== "no":
                      print("\n Try again, focus carefully.")
                      self.file.write("wrong choice. please try again\n")
                   else:
                     print("\n Invalid choice. please try again.")
                     self.file.write("Invalid choice. please try again\n")
                     
                    
            elif self.location== "backyard":
                while True:
                   garden=input("\n There are three trees in the garden. You will look for a tree with a phrase written on it. Tree 1  or  Tree 2  or  Tree 3: ").strip().lower()
                   self.file.write(f"Location: backyard, Input: {garden}\n")
                   if garden== "tree 1":
                      print("\n Wrong tree.")
                   elif garden== "tree 2":
                      print("\n Wrong tree.")
                   elif garden== "tree 3":
                       while True:
                          mnt=input("\n ****The mountain is the endpoint****. You will go to the mountain. Type 'OK' to continue: ").strip().lower()
                          self.file.write(f"Player selection: tree 3, Input: {mnt}\n")
                          if mnt== "ok":
                             self.move("mountain")
                             break
                          else:
                             print("\n Invalid choice. please try again.")
                             self.file.write("wrong choice. please try again\n")
                       break    
                   else:
                      print("\n Invalid choice. please try again.")
                      self.file.write("Invalid choice. please try again\n")
                      
                      
            elif self.location== "mountain":
                while True:
                   rock=input("\n On the mountain, there is a large rock engraved with the phrase: 'The final distination is the symbol you arranged at the railway station in Bulgaria'. Type 'Let's go' to head there: ").strip().lower()
                   self.file.write(f"Location: mountain, Input: {rock}\n")
                   if rock== "let's go":
                      print("\n Exellent")
                      self.move("large rock")
                      break
                   else:
                     print("\n Invalid choice. please try again.")
                     self.file.write("Invalid choice. please try again\n") 
                    
            elif self.location== "large rock":
                while True:
                   secret_code=input("\n Now you will gather all the hints and clues you have collected to form the secret code to unlock the electronic gate in the rock and claim the tresure. Remember the symbol engraved on the pistol; It will help you arrange the codes: ")
                   self.file.write(f"Location: Large Rock, Input: {secret_code}\n")  # Logs secret code attempt
                   if secret_code== "TR-1967-Φ34-VED":
                      print("******Congratulations on your victory! You have finally obtained the tresure, and your father is proud of you.******")
                      self.file.write("Player won the game!\n")  # Log game win
                      break
                   else:
                      print("\n Try again, focus carefully.")
                      self.file.write("Incorrect secret code attempt\n")  # Logs incorrect code
                break
                    
        self.file.close()    

# Start the game       
player_name=input("\n Enter your name: ")
game= Game(player_name)
game.play()