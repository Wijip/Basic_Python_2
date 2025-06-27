def show_menu():
    print("\nMenu:")
    print("1. Lihat catatan")
    print("2. Tambah catatan")
    print("3. Hapus catatan")
    print("4. Edit catatan")
    print("0. Keluar")


def view_notes(filename):
    print("\n--- Daftar Catatan ---")
    with open(filename, "r") as f:
        lines = f.readlines()
        if lines:
            for idx, note in enumerate(lines, start=1):
                print(f"{idx}. {note.strip()}")
        else:
            print("Belum ada catatan.")


def add_note(filename):
    note = input("Masukkan catatan baru: ")
    with open(filename, "a") as f:
        f.write(note + "\n")
    print("Catatan berhasil ditambahkan.")


def delete_note(filename):
    view_notes(filename)
    index = int(input("Masukkan nomor catatan yang akan dihapus: ")) - 1
    with open(filename, "r") as f:
        lines = f.readlines()
    if 0 <= index < len(lines):
        lines.pop(index)
        with open(filename, "w") as f:
            for line in lines:
                f.write(line)
        print("Catatan berhasil dihapus.")
    else:
        print("Nomor catatan tidak valid.")


def edit_note(filename):
    view_notes(filename)
    index = int(input("Masukkan nomor catatan yang akan diubah: ")) - 1
    with open(filename, "r") as f:
        lines = f.readlines()
    if 0 <= index < len(lines):
        new_note = input("Masukkan catatan baru: ")
        lines[index] = new_note + "\n"
        with open(filename, "w") as f:
            for line in lines:
                f.write(line)
        print("Catatan berhasil diubah.")
    else:
        print("Nomor catatan tidak valid.")


def main():
    filename = "notes.txt"

    # Pastikan file sudah ada (jika tidak, buat file kosong)
    with open(filename, "a"):
        pass

    while True:
        show_menu()
        choice = input("Pilih menu (1-5): ")
        if choice == "1":
            view_notes(filename)
        elif choice == "2":
            add_note(filename)
        elif choice == "3":
            delete_note(filename)
        elif choice == "4":
            edit_note(filename)
        elif choice == "0":
            print("Keluar program.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
