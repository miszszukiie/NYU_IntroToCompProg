# Helen Li
# April 22, 2015
# Assignment #8: Part #2

counter = 0

product_names = ["hamburger"]*10 + ["cheeseburger"]*5 + ["small fries"]*20
product_costs = [0.99]*10 + [1.29]*5 + [1.49]*20
new_product_names = []

while True:
  again = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port, or (q)uit: ")
  if again == "s":
    name = input("Enter a product name: ")
    if name in product_names:
      x = product_names.index(name)
      print ("We sell", name, "at", product_costs[x], "per unit")
      for a in product_names:
        if a == name:
          counter += 1

      print ("We currently have", counter, "in stock")
      counter = 0
      print ()
    else:
      print ("Sorry, we don't sell", name)
      print()
  elif again == "l":
    print (format("Product", "<20s"), format("Price", "<13s"), format("Quantity", "<13s"))
    while True:
      for b in product_names:
        if b not in new_product_names:
          new_product_names.append(b)
      break
    for k in new_product_names:
      if k in product_names:
        m = product_names.index(k)
        for n in product_names:
          if n == k:
            counter += 1
        print (format(k, "<20s"), format(product_costs[m], "<13.2f"), format(counter, "<13d"))
        counter = 0
    print ()
  elif again == "a":
    while True:
      name = input("Enter a new product name: ")

      if name in product_names:
        print ("Sorry, we already sell that product. Try again.")
      else:
        while True:
          cost = float(input("Enter a product cost: "))
          if cost > 0:
            break
          else:
            print ("Invalid cost. Try again.")
        while True:
          quantity = int(input("How many of these products do we have? "))
          if quantity > 0:
            print ("Product added!")
            print ()
            break
          else:
            print ("Invalid quantity. Try again.")
        adding = 0
        while adding < quantity:
          product_names.append(name)
          adding += 1
        adding2 = 0
        while adding2 < quantity:
          product_costs.append(cost)
          adding2 += 1
        break
  elif again == "r":
    name = input("Enter a product name: ")
    if name not in product_names:
      print ("Product doesn't exist. Can't remove.")
      print ()
    else:
      while name in product_names:
        y = product_names.index(name)
        z = product_costs[y]
        product_costs.remove(z)
        product_names.remove(name)
      print ("Product removed!")
      print ()
  elif again == "u":
    name1 = input("Enter a product name: ")
    if name1 not in product_names:
      print ("Product doesn't exist. Can't update.")
      print ()
    else:
      print ("What would you like to update?")
      update = input("(n)ame, (c)ost, or (q)uantity: ")
      if update == "n":
        while True:
          name = input("Enter a new name: ")
          if name in product_names:
            print ("Duplicate name!")
          else:
            while name1 in product_names:
              u = product_names.index(name1)
              product_names[u] = name

            print ("Product name has been updated")
            print ()
            break
        if name1 in new_product_names:
          w = new_product_names.index(name1)
          new_product_names[w] = name
      elif update == "c":
        while True:
          cost = float(input("Enter a new cost: "))
          if cost > 0:
            for j in range (0, len(product_names)):
              v = product_names[j]
              if v == name1:
                product_costs[j] = cost
            print ("Product cost has been updated")
            print ()
            break
          else:
            print ("Invalid cost. Try again.")
      elif update == "q":
        while True:
          quantity = int(input("Enter a new quantity: "))
          if quantity > 0:
            for c in product_names:
              if c == name1:
                counter += 1
            if counter > quantity:
              while counter > quantity:
                d = product_names.index(name1)
                e = product_costs[d]
                product_costs.remove(e)
                product_names.remove(name1)
                counter -= 1
              print ("Product quantity has been updated.")
              print ()
              counter = 0
              break
            elif counter < quantity:
              while counter < quantity:
                f = product_names.index(name1)
                g = product_costs[f]
                product_costs.append(g)
                product_names.append(name1)
                counter += 1
              print ("Product quantity has been updated.")
              print ()
              counter = 0
              break
            
          else:
            print ("Invalid quantity")
      else:
        print ("Invalid option")
        print ()
  elif again == "e":
    p = format(sum(product_costs), ".2f")
    t = max(product_costs)
    r = min(product_costs)
    s = product_costs.index(t)
    i = product_names[s]
    q = product_costs.index(r)
    l = product_names[q]
    print (format("Most expensive product:", "<30s"), t, " (", i, ")", sep="")
    print (format("Least expensive product:", "<30s"), r, " (", l, ")", sep="")
    print (format("Total value of all products:", "<30s"), p, sep="")
    print ()
      
  elif again == "q":
    print ("See you soon!")
    break
  else:
    print ("Invalid option. Try again.")
    print ()
