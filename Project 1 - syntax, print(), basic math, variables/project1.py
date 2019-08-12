#! python3

lovely_loveseat_description = '''
    Lovely Loveseat, or so you thought when you first bought it. The Shady Merchant seemed friendly enough, you suppose.
     Peculiar though - bulging eyes and pale skin, an odd gait, and the most horrendous smell of rotting fish. You 
     bought it on your trip through the East Coast, in an old, newly-revived fishing town called Ipswich. All the people
      there looked fairly similar, so you thought it had to be genetic or the result of some infectious disease. You 
      wrapped your dad\'s old Yankees Scarf around your mouth and got out of there as soon as the Bus arrived. Every 
      night, though, you can swear you still Smell the rotting fish, still Hear the shuffling, plodding Footsteps 
      through your Attic. And even worse, you\'re sure of the Whispers you Hear; of the sounds, words, and images human 
      minds were never meant to comprehend. You can\'t wait to sell them all. Tufted polyester blend on wood. 32 inches 
      high x 40 inches wide x 30 inches deep. Red or white. \n
      '''

lovely_loveseat_price = 254.00

stylish_settee_description = '''
    Stylish Settee. Faux leather on birch, covered in wizard stickers and martini stains. Reminds you of your mom: her 
    inebriation, her revolting taste in literature AND decor. You have no idea why you bought them from her, or why she
     had so many in the first place. You\'re glad she\'s dead. 29.50 inches high x 54.75 inches wide x 28 inches deep.
      Black with decals and stains. \n
      '''

stylish_settee_price = 180.50

luxurious_lamp_description = '''
    Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. I used 50 of these to burn down high school.
     Yeah, that was me. \n
     '''

luxurious_lamp_price = 52.15

sales_tax = 0.088

customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization = lovely_loveseat_description + luxurious_lamp_description
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print('Customer One Items: \n')
print(customer_one_itemization)

if customer_one_total > round(customer_one_total, 2):
    customer_one_total += 0.01
print('Customer One Total: ${:0.2f}\n'.format(customer_one_total))
print('You were helped today by: Cthulhu')
print('Have a nice day, and go fuck yourself!')