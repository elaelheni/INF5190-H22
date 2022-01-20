def open_file(num_client):
    output = open(num_client+".txt", "w")
    output.write("Client numéro %s\n\n" %num_client)
    output.write( "%-12s %-14s %4s %8s %10s\n" %(" ", "No de produit", "Qte", "Prix", "Total (tx)"))
    return output

def close_file(file, total_price, qty):
    discount = (total_price * 0.15) if qty > 100 else 0
    file.write("\nTotal avant rabais : %.2f\n" %total_price)
    file.write("Rabais : %.2f\n" %discount)
    file.write("Total : %.2f" %(total_price - discount))
    file.close()


