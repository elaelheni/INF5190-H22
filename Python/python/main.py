from file.file import *
from utils.taxes import calculate_tax
from utils.filewriter import open_file, close_file

file = open("input")
lines = file.readlines()
qty : int = 0
total_price : int = 0
items : list[File] = []
num_produit : int = 0


if __name__ == "__main__":
    for index, line in enumerate(lines):
        string = line.rstrip("\n").split(" ")
        item = File(*string)
        total = (float(item.price) * float(item.qte)) * calculate_tax(item.tax)
        qty = qty + int(item.qte)
        if index == 0:
            output = open_file(item.num_client)

        if index > 0 and item.num_client != items[index -1].num_client:
            close_file(output, total_price, qty)
            total_price = qty = num_produit = 0

            output = open_file(item.num_client)

        output.write("%-12s %-14s %4s %8s %10.2f\n" % ("Produit #" + str(num_produit +1), item.num_produit, item.qte, item.price, total))
        total_price += total
        num_produit += 1
        items.append(item)
    close_file(output, total_price, qty)

    

