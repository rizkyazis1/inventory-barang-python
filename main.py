import csv
import os

FILE_CSV = "barang.csv"

#linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def cari(self, key, value):
        current = self.head

        while current:
            if str(current.data[key]).lower() == str(value).lower():
                return current

            current = current.next

        return None

    def hapus(self, id_barang):
        current = self.head
        previous = None

        while current:
            if current.data["id"] == id_barang:

                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next

                return True

            previous = current
            current = current.next

        return False

    def to_list(self):
        data = []
        current = self.head

        while current:
            data.append(current.data)
            current = current.next

        return data

#queue

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def tampil(self):
        if not self.data:
            print("Riwayat kosong")
            return

        print("\n=== RIWAYAT ===")
        for i, item in enumerate(self.data, 1):
            print(f"{i}. {item}")

#CSV

def load_data(ll):
    if not os.path.exists(FILE_CSV):

        with open(FILE_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nama", "stok", "harga"])

        return

    with open(FILE_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            ll.tambah({
                "id": row["id"],
                "nama": row["nama"],
                "stok": int(row["stok"]),
                "harga": int(row["harga"])
            })


def save_data(ll):
    with open(FILE_CSV, "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=["id", "nama", "stok", "harga"]
        )

        writer.writeheader()

        for item in ll.to_list():
            writer.writerow(item)

#CRUD

def tambah(ll, q):
    id_barang = input("ID : ")

    if ll.cari("id", id_barang):
        print("ID sudah ada")
        return

    data = {
        "id": id_barang,
        "nama": input("Nama Barang : "),
        "stok": int(input("Stok Barang : ")),
        "harga": int(input("Harga Barang : "))
    }

    ll.tambah(data)
    q.enqueue(data["nama"])

    save_data(ll)

    print("Data berhasil ditambah")


def tampil(ll):
    data = ll.to_list()

    if not data:
        print("Data kosong")
        return

    print("\nID Barang | Nama Barang | Stok Barang | Harga Barang")
    print("-" * 40)

    for item in data:
        print(
            item["id"],
            item["nama"],
            item["stok"],
            item["harga"]
        )


def cari(ll):
    nama = input("Nama barang : ")

    node = ll.cari("nama", nama)

    if node:
        print(node.data)
    else:
        print("Tidak ditemukan")


def edit(ll):
    id_barang = input("ID Barang : ")

    node = ll.cari("id", id_barang)

    if not node:
        print("Tidak ditemukan")
        return

    node.data["nama"] = input("Nama baru : ")
    node.data["stok"] = int(input("Stok baru : "))
    node.data["harga"] = int(input("Harga baru : "))

    save_data(ll)

    print("Data berhasil diubah")


def hapus(ll):
    id_barang = input("ID barang : ")

    if ll.hapus(id_barang):
        save_data(ll)
        print("Data berhasil dihapus")
    else:
        print("Data tidak ditemukan")

#sorting (bubble sort)

def sorting(ll):
    data = ll.to_list()

    for i in range(len(data)):
        for j in range(len(data)-1-i):

            if data[j]["stok"] > data[j+1]["stok"]:
                data[j], data[j+1] = data[j+1], data[j]

    print("\n=== HASIL SORTING STOK ===")

    for item in data:
        print(item)

#MAIN

def main():

    inventory = LinkedList()
    riwayat = Queue()

    load_data(inventory)

    while True:
        print("===== INVENTORY BARANG =====")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Cari Barang")
        print("4. Edit Barang")
        print("5. Hapus Barang")
        print("6. Sorting Barang")
        print("7. Riwayat Barang Masuk")
        print("8. Keluar")

        pilih = input("Pilih : ")

        if pilih == "1":
            tambah(inventory, riwayat)

        elif pilih == "2":
            tampil(inventory)

        elif pilih == "3":
            cari(inventory)

        elif pilih == "4":
            edit(inventory)

        elif pilih == "5":
            hapus(inventory)

        elif pilih == "6":
            sorting(inventory)

        elif pilih == "7":
            riwayat.tampil()

        elif pilih == "8":
            break

        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()