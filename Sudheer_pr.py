# Name : Sudheer Singh Chauhan
# Collage : lovely professional university
# mobile no.: 9889158953
# Email : g7sudheer@gmail.com


#  creating dictionary 
products_list = {
    'Leather':[1100,18,1],
    'Umbrella': [900,12,2],
    'Cigarette': [200,28,3],
    'Honey':[100,0,4]

}
lst=[]
total_price = 0
for i in products_list.values():
    products_price = i[0]*i[2]
    # taking gst amount of from the dictionary
    lst.append(i[1])

    # 5 % discount on amount of more than 500
    if i[0] >= 500:
        products_price = products_price - (0.05 * products_price)
    products_price = products_price + (i[1]*products_price)
    total_price += products_price
    
print("Total amount is :", total_price)
print("Max GST is on :", max(lst))


