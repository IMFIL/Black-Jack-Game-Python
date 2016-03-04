import random
global DD



class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit= suit

    def __repr__(self):
        return "Card("+self.rank+","+self.suit+")"


    
class Deck:
    rank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suit = [ "\u2660","\u2661","\u2662","\u2663"]

    def __init__(self):
        self.deck = []
        for i in Deck.rank:
            for j in Deck.suit:
                self.deck.append(Card(i,j))

        self.deck *= 3
        random.shuffle(self.deck)


    def deal_player (self):
        
        return self.deck.pop()

    def deal_dealer(self):
        
        return self.deck.pop()
    


def play_dealer():
    Sum = 0
    Current = DD.deal_dealer()
    print ("Dealer has:",Current)
    

    if Current.rank == "J" or Current.rank == "Q" or Current.rank == "K":
        Sum += 10
    elif Current.rank == "A":
         if Sum + 11 <= 21:
            Sum +=11
         else:
            Sum += 1
    else:
        Sum += int(Current.rank)

    

    Player = play_player()

    
    
    while Sum < 17 and Sum != 21:
             Current = DD.deal_dealer()
             print ("Dealer has:",Current)
             
             
             if Current.rank == "J" or Current.rank == "Q" or Current.rank == "K":
                 Sum += 10
             elif Current.rank == "A":
                 if Sum + 11 <= 21:
                     Sum +=11
                 else:
                     Sum += 1
             else:
                 Sum += int(Current.rank)

    if Sum > 21 and Player > 21:
         print ("You have won even if you passed 21, the dealer did as well")
         return 1
        
    if Player > 21:
        print ("You lost, since you passed 21 and the dealer did not")
        return 0

    elif Sum > Player and Sum <= 21 :
         print ("You have lost the dealer had",Sum,"and you had",Player)
         return 0
    elif Sum == Player:
         print("Same number, no loss no win")
         return 2
    else:
         print ("You have won",Player,"V.S",Sum)
         return 1
    





def play_player():
    money= 0
    A = 0
    for i in range(2):
        Current = DD.deal_player()
        print ("Your card: ",Current)
        if Current.rank == "J" or Current.rank == "Q" or Current.rank == "K":
            money += 10
        elif Current.rank == "A":
             A = eval(input("Choose between 1 and 11:"))
             while A != 1 and A != 11:
                 A= eval(input("Choose between 1 and 11:"))
             money += A
        else:
            money += int(Current.rank)
        
    A = 0
    HoS = input("Hit or Stay: ")

            

    if HoS.upper() == "STAY":
        return money

    if HoS.upper() == "HIT":
        while money < 21 and HoS.upper() == "HIT":
                Current = DD.deal_player()
                print ("Your card:",Current)
    
                if Current.rank == "J" or Current.rank == "Q" or Current.rank == "K":
                     money += 10
                elif Current.rank == "A":
                     A = eval(input("Choose between 1 and 11:"))
                     while A != 1 and A != 11:
                           A = eval(input("Choose between 1 and 11:"))
                     money+=A
                else:
                     money += int(Current.rank)
                
                if money > 21:
                    print ("You passed 21")

                else:
                    HoS = input("Hit or Stay: ")
            


        return money
                    

                
                
                  
        
DD = Deck()
print ("Welcome to the virtual black jack game, where you either win the double of your bet or lose all, press enter to continue")
input()
Token = eval(input("How much money do you want to play with (max:100) (min:20) : "))
while Token < 20 or Token > 100:
    Token = eval(input("How much money do you want to play with (max:100) (min:20) : "))
    

while Token >= 20 :
    while True:
        try:
            Bet = eval(input("How much are you betting (min:20) : "))
            break
        except NameError:
            print("Enter a number please")
        except SyntaxError:
            print("You have to enter something")

    while Bet < 20 or Bet > Token  :
        print("Please bet an appropriate ammount")
        while True:
            try:
                Bet = eval(input("How much are you betting (min:20) : "))
                break
            except NameError:
                print("Enter a number please")
            except SyntaxError:
                print("You have to enter something")


    result = play_dealer()

    if result == 0:
        Token-=Bet

    if result == 1:
        Token += Bet*2 - Bet


    if len(DD.deck) <= 10:
        DD = Deck()


    print ("You have:",Token,"remaning")
        

        

    

    
    

        






    
