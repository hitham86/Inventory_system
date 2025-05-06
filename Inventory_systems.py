import csv
import datetime
import pathlib



INVENTORY = "./inventory.csv"
INVALID = "./invalid.txt"
LOGS = "./logs.csv"


class DataError(Exception):
    def __init__(self, message):
        self.message = message


class RiskError(Exception):
    def __init__(self, message):
        self.message = message


def validator(sequence):
    with open(INVALID, "r") as f:
        contents = f.read().split("\n")
        sequence_check = sequence.split(" ")
        for word in sequence_check:
            if word.upper() in contents:
                raise RiskError("input not valid!")
    return sequence


def open_file():
    with open(INVENTORY, "r") as f:
        reader = csv.DictReader(f)
        complete_products = []
        product_names = []
        for product in reader:
            complete_products.append(product)
            product_names.append(product["item"])
        if not complete_products or not product_names:
            raise DataError("Data not found!")
    return complete_products, product_names


def write(complete_products):
    with open(INVENTORY, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["item", "price", "quantity"])
        writer.writeheader()
        writer.writerows(complete_products)


def logger(event):
    with open(LOGS, "r+", newline="") as f:
        contents = f.read()
        writer = csv.DictWriter(f, fieldnames=["event type", "date"])
        if not contents:
            writer.writeheader()
            writer.writerow({"event type": event, "date": datetime.datetime.now()})
        else:
            writer.writerow({"event type": event, "date": datetime.datetime.now()})


def add_product():
    complete_products, product_names = open_file()
    product = validator(input("please enter the name of your product: "))
    if product not in product_names:
        price = float(input("please enter the price: "))
        quantity = float(input("please enter the quantity: "))
        complete_products.append({"item": product, "price": price, "quantity": quantity})
        write(complete_products)
        print("product successfully added!")
    else:
        print("product already exists!")
    logger("add_product")


def show_complete():
    print(open_file()[0])
    logger("show_complete")


def update():
    complete_products, product_names = open_file()
    product = validator(input("please enter the name of the product to update: "))
    if product in product_names:
        price = float(input("please enter the price: "))
        quantity = float(input("please enter the quantity: "))
        for index, item in enumerate(complete_products):
            if item["item"] == product:
                complete_products[index] = {"item": product, "price": price, "quantity": quantity}
                write(complete_products)
                print("product successfully updated")
    else:
        print("cannot update product that doesnt exist!")
    logger("update")


def delete():
    complete_products, product_names = open_file()
    product = validator(input("please enter a product to delete: "))
    if product in product_names:
        complete_products = [full_product for full_product in complete_products if full_product["item"] != product]
        write(complete_products)
        print("product deleted successfully")
    else:
        print("product does not exist!")
    logger("delete")


def search():
    complete_products, product_names = open_file()
    product = validator(input("please enter a product to find: "))
    if product in product_names:
        for full_product in complete_products:
            if full_product["item"] == product:
                print(f"Product: {full_product['item']}")
                print(f"Price: ${float(full_product['price']):,.2f}")
                print(f"Quantity: {full_product['quantity']}")
    logger("search")


def main():
        options = {
            1: ["add products", add_product],
            2: ["show complete", show_complete],
            3: ["update", update],
            4: ["delete", delete],
            5: ["search", search],
            6: ["quit"]
        }

        for _ in range(35):
            try:
                print("select a following option")
                for key, value in options.items():
                    print(f"{key} {value[0]}")
                selection = int(input(">>>: "))
                if selection == 6:
                    break
                else:
                    options[selection][1]()
                    print()
            except (FileNotFoundError, ValueError, DataError, RiskError) as e:
                print("\n======================================================")
                print(e)
                print("======================================================\n")


if __name__ == '__main__':
    main()