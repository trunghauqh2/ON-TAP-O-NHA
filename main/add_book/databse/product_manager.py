
# =================================
# QUAN LY SAN PHAM CUA HANG QUAN AO
# =================================

products = []


def add_product():
    print("\n===== THEM SAN PHAM =====")

    product_id = input("Ma san pham: ")
    name = input("Ten san pham: ")
    price = float(input("Gia san pham: "))
    quantity = int(input("So luong: "))

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)

    print("Them san pham thanh cong!")


def show_products():
    print("\n===== DANH SACH SAN PHAM =====")

    if len(products) == 0:
        print("Chua co san pham nao!")
        return

    for product in products:
        print("-------------------------")
        print("Ma:", product["id"])
        print("Ten:", product["name"])
        print("Gia:", product["price"])
        print("So luong:", product["quantity"])


def search_product():
    keyword = input("Nhap ten san pham can tim: ")

    found = False

    for product in products:
        if keyword.lower() in product["name"].lower():
            print("Tim thay:", product["name"])
            print("Gia:", product["price"])
            print("So luong:", product["quantity"])
            found = True

    if not found:
        print("Khong tim thay san pham!")


def main():
    while True:
        print("\n===== FASHION STORE =====")
        print("1. Them san pham")
        print("2. Xem danh sach san pham")
        print("3. Tim kiem san pham")
        print("0. Thoat")

        choice = input("Lua chon cua ban: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            show_products()

        elif choice == "3":
            search_product()

        elif choice == "0":
            print("Ket thuc chuong trinh!")
            break

        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()
