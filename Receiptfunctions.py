def Receipt():
textReceipt.delete("1.0", END)
x = random.randint(10908, 500876)
randomRef = str(x)
Receipt_Ref.set("Bill" + randomRef)


textReceipt.insert(END, 'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t' + Date_of_Order.get() + '\n')
textReceipt.insert(END, 'Unit\t\t\t\t'+"Total of Unit \n")
textReceipt.insert(END, 'Cocktail:\t\t\t\t\t' + cocktail.get() + '\n')
textReceipt.insert(END, 'Iced Tea:\t\t\t\t\t' + iced_tea.get()+'\n')
textReceipt.insert(END, 'Hot Chocolate:\t\t\t\t\t' + hot_chocolate.get()+'\n')
textReceipt.insert(END, 'Orange Juice:\t\t\t\t\t' + orange_juice.get()+'\n')
textReceipt.insert(END, 'Milk Shake:\t\t\t\t\t' + milkshake.get()+'\n')
textReceipt.insert(END, 'Mountain Dew:\t\t\t\t\t' + mountain_dew.get()+'\n')
textReceipt.insert(END, 'Sting:\t\t\t\t\t' + sting.get()+'\n')
textReceipt.insert(END, 'Cobra:\t\t\t\t\t' + cobra.get()+'\n')
textReceipt.insert(END, 'Fried Chicken:\t\t\t\t\t' + fried_chicken.get()+'\n')
textReceipt.insert(END, 'Kare Kare:\t\t\t\t\t' + kare_kare.get()+'\n')
textReceipt.insert(END, 'Crispy Pata:\t\t\t\t\t' + crispy_pata.get()+'\n')
textReceipt.insert(END, 'Sinigang baboy:\t\t\t\t\t' + sinigang_baboy.get()+'\n')
textReceipt.insert(END, 'Sinigang Hipon:\t\t\t\t\t' + sinigang_hipon.get()+'\n')
textReceipt.insert(END, 'Bicol Express:\t\t\t\t\t' + bicol_express.get()+'\n')
textReceipt.insert(END, 'Asparagus Tofu:\t\t\t\t\t' + asparagus_tofu.get()+'\n')
textReceipt.insert(END, 'Chicken Sisig:\t\t\t\t\t' + chicken_sisig.get()+'\n')
textReceipt.insert(END, 'Total of Drinks:\t\t\t\t' + Total_of_Drinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
textReceipt.insert(END, 'Total of Foods:\t\t\t\t' + Total_of_Food.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
textReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")