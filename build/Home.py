from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label
import pymysql

class MainApp:
    
    def connect_to_database(self):
        self.mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="# Your sql password ",
            database="# Your own database "
        )
        self.cursor = self.mydb.cursor()
    
    def fetch_data(self):
        query = "SELECT `nama barang`, `stok barang`, `harga barang` FROM `database toko` ORDER BY `id` DESC LIMIT 9"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


    def __init__(self, root):
        self.root = root
        self.connect_to_database()
        self.data = self.fetch_data()
        self.root.geometry("1280x720")
        # Center the window on the screen
        window_width = 1280
        window_height = 720

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)

        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.configure(bg="#144272")

        self.root.resizable(False, False)

        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path(r"E:\CRUD Python-MySQL Warung\build\assets\frame4")

        self.canvas = Canvas(
            self.root,
            bg="#144272",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.create_background()
        self.create_buttons()
        self.create_text_elements()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def create_background(self):
        # Create all background rectangles
        self.canvas.create_rectangle(0.0, 0.0, 111.0, 720.0, fill="#E2DAD6", outline="")
        self.canvas.create_rectangle(123.0, 0.0, 1270.0, 183.0, fill="#E2DAD6", outline="")
        self.canvas.create_rectangle(121.0, 202.0, 1274.0, 691.0, fill="#D9D9D9", outline="")
        self.canvas.create_rectangle(123.0, 206.0, 1270.0, 254.0, fill="#134B70", outline="")
        self.canvas.create_rectangle(123.0, 254.0, 1270.0, 302.0, fill="#508C9B", outline="")
        self.canvas.create_rectangle(123.0, 302.0, 1270.0, 350.0, fill="#134B70", outline="")
        self.canvas.create_rectangle(123.0, 348.0, 1270.0, 396.0, fill="#508C9B", outline="")
        self.canvas.create_rectangle(123.0, 396.0, 1270.0, 444.0, fill="#134B70", outline="")
        self.canvas.create_rectangle(123.0, 444.0, 1270.0, 492.0, fill="#508C9B", outline="")
        self.canvas.create_rectangle(123.0, 492.0, 1270.0, 540.0, fill="#134B70", outline="")
        self.canvas.create_rectangle(123.0, 540.0, 1270.0, 588.0, fill="#508C9B", outline="")
        self.canvas.create_rectangle(123.0, 0.0, 1270.0, 60.0, fill="#DFD3C3", outline="")
        self.canvas.create_rectangle(123.0, 588.0, 1270.0, 636.0, fill="#134B70", outline="")
        self.canvas.create_rectangle(123.0, 636.0, 1270.0, 684.0, fill="#508C9B", outline="")
        self.canvas.create_rectangle(543.9999786688425, 188.0, 558.0, 690.0, fill="#D9D9D9", outline="")
        self.canvas.create_rectangle(820.9999786688425, 188.0, 835.0, 690.0, fill="#D9D9D9", outline="")

    def create_buttons(self):
        # Create buttons
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_main_app,
            relief="flat"
        )
        button_1.image = button_image_1  # Keep a reference to avoid garbage collection
        button_1.place(x=0.0, y=0.0, width=111.0, height=71.5)

        button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_create,
            relief="flat"
        )
        button_2.image = button_image_2
        button_2.place(x=0.0, y=102.0, width=111.0, height=111.0)

        button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_read,
            relief="flat"
        )
        button_3.image = button_image_3
        button_3.place(x=0.0, y=251.0, width=111.0, height=111.0)

        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_update,
            relief="flat"
        )
        button_4.image = button_image_4
        button_4.place(x=0.0, y=400.0, width=111.0, height=111.0)

        button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_delete,
            relief="flat"
        )
        button_5.image = button_image_5
        button_5.place(x=0.0, y=549.0, width=111.0, height=111.0)

    def create_text_elements(self):
        # Create text elements on canvas
        self.canvas.create_text(632.0, 7.0, anchor="nw", text="HOME", fill="#000000", font=("Nunito Bold", 40 * -1))

        self.canvas.create_rectangle(166.0, 68.0, 632.0, 174.0, fill="#DFD3C3", outline="")
        self.canvas.create_rectangle(761.0, 68.0, 1227.0, 174.0, fill="#DFD3C3", outline="")

        self.canvas.create_text(177.0, 76.0, anchor="nw", text="Banyak \nBarang:", fill="#000000", font=("Nunito Bold", 32 * -1))
        self.canvas.create_text(782.0, 76.0, anchor="nw", text="Jumlah \nStok:", fill="#000000", font=("Nunito Bold", 32 * -1))
        self.canvas.create_text(236.0, 214.0, anchor="nw", text="NAMA BARANG", fill="#FFFFFF", font=("Nunito Bold", 24 * -1))
        self.canvas.create_text(586.0, 214.0, anchor="nw", text="STOK BARANG", fill="#FFFFFF", font=("Nunito Bold", 24 * -1))
        self.canvas.create_text(927.0, 214.0, anchor="nw", text="HARGA BARANG", fill="#FFFFFF", font=("Nunito Bold", 24 * -1))

        # Mengambil jumlah barang dan stok dari database
        total_items = len(self.data)
        total_stocks = sum([item[1] for item in self.data])
        
        # Menampilkan jumlah barang dan stok
        self.canvas.create_text(450.0, 83.0, anchor="nw", text=total_items, fill="#000000", font=("Nunito Bold", 48 * -1))
        self.canvas.create_text(1055.0, 81.0, anchor="nw", text=total_stocks, fill="#000000", font=("Nunito Bold", 48 * -1))
        
        # Menampilkan barang, stok, dan harga
        for i, item in enumerate(self.data):
            self.canvas.create_text(135.0, 265.0 + i * 46, anchor="nw", text=item[0], fill="#FFFFFF", font=("Nunito Bold", 24 * -1))
            self.canvas.create_text(566.0, 262.0 + i * 49, anchor="nw", text=item[1], fill="#FFFFFF", font=("Nunito Bold", 24 * -1))
            self.canvas.create_text(844.0, 258.0 + i * 49, anchor="nw", text=f"Rp. {item[2]:,.2f}", fill="#FFFFFF", font=("Nunito Bold", 24 * -1))
        
        # Jika ada slot kosong, tampilkan "---"
        for i in range(len(self.data), 9):
            self.canvas.create_text(166.0, 265.0 + i * 46, anchor="nw", text="---", fill="#FFFFFF", font=("Nunito Bold", 24 * -1))
            self.canvas.create_text(566.0, 262.0 + i * 49, anchor="nw", text="---", fill="#FFFFFF", font=("Nunito Bold", 24 * -1))
            self.canvas.create_text(927.0, 258.0 + i * 49, anchor="nw", text="---", fill="#FFFFFF", font=("Nunito Bold", 24 * -1))


    def open_main_app(self):
        self.root.destroy()  # Menutup jendela saat ini
        root = Tk()
        MainApp(root)  # Menginisialisasi GUI dari kelas MainApp
        root.mainloop()

    def open_create(self):
        self.root.destroy()
        root = Tk()
        Create(root)
        root.mainloop

    def open_read(self):
        self.root.destroy()
        root = Tk()
        Read(root)  # Menginisialisasi GUI dari kelas Read
        root.mainloop()

    def open_update(self):
        self.root.destroy()
        root = Tk()
        Update(root)  # Menginisialisasi GUI dari kelas Update
        root.mainloop()

    def open_delete(self):
        self.root.destroy()
        root = Tk()
        Delete(root)  # Menginisialisasi GUI dari kelas Delete
        root.mainloop()

    def close_connection(self):
        self.cursor.close()
        self.mydb.close()


class Create:
    def connect_to_database(self):
        self.mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="# Your sql password ",
            database="# Your own database "
        )
        self.cursor = self.mydb.cursor()

    def fetch_data(self):
        query = "SELECT `nama barang`, `stok barang`, `harga barang` FROM `database toko` ORDER BY `id` DESC LIMIT 9"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def __init__(self, root):
        self.root = root
        self.connect_to_database()
        self.data = self.fetch_data()

        self.root.geometry("1280x720")
        # Center the window on the screen
        window_width = 1280
        window_height = 720

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)

        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.configure(bg="#144272")

        self.canvas = Canvas(
            self.root,
            bg="#144272",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            0.0,
            0.0,
            111.0,
            720.0,
            fill="#E2DAD6",
            outline=""
        )

        self.setup_buttons()
        self.setup_ui_elements()

        self.root.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"E:\CRUD Python-MySQL Warung\build\assets\frame2")
        return ASSETS_PATH / Path(path)
    
    def open_main_app(self):
        self.root.destroy()  # Menutup jendela saat ini
        root = Tk()
        MainApp(root)  # Menginisialisasi GUI dari kelas MainApp
        root.mainloop()

    def open_create(self):
        self.root.destroy()
        root = Tk()
        Create(root)
        root.mainloop

    def open_read(self):
        self.root.destroy()
        root = Tk()
        Read(root)  # Menginisialisasi GUI dari kelas Read
        root.mainloop()

    def open_update(self):
        self.root.destroy()
        root = Tk()
        Update(root)  # Menginisialisasi GUI dari kelas Update
        root.mainloop()

    def open_delete(self):
        self.root.destroy()
        root = Tk()
        Delete(root)  # Menginisialisasi GUI dari kelas Delete
        root.mainloop()

    def insert_data(self):
        nama_barang = self.entry_1.get()
        stok_barang = self.entry_2.get()
        harga_barang = self.entry_3.get()

        if nama_barang and stok_barang and harga_barang:
            try:
                query = "INSERT INTO `database toko` (`nama barang`, `stok barang`, `harga barang`) VALUES (%s, %s, %s)"
                self.cursor.execute(query, (nama_barang, stok_barang, harga_barang))
                self.mydb.commit()

                # Reset input fields
                self.entry_1.delete(0, 'end')
                self.entry_2.delete(0, 'end')
                self.entry_3.delete(0, 'end')

                # Display success message
                self.canvas.create_text(
                    177.0,
                    570.0,
                    anchor="nw",
                    text="Data telah dibuat",
                    fill="red",
                    font=("Nunito Bold", 14 * -1)
                )

            except Exception as e:
                print(f"Error: {e}")
                self.mydb.rollback()
        else:
            print("Data harus diisi")
    
    def setup_buttons(self):
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_main_app,
            relief="flat"
        )
        button_1.image = button_image_1  # Keep a reference to avoid garbage collection
        button_1.place(x=0.0, y=0.0, width=111.0, height=71.5)

        button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_create,
            relief="flat"
        )
        button_2.image = button_image_2
        button_2.place(x=0.0, y=102.0, width=111.0, height=111.0)

        button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_read,
            relief="flat"
        )
        button_3.image = button_image_3
        button_3.place(x=0.0, y=251.0, width=111.0, height=111.0)

        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_update,
            relief="flat"
        )
        button_4.image = button_image_4
        button_4.place(x=0.0, y=400.0, width=111.0, height=111.0)

        button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_delete,
            relief="flat"
        )
        button_5.image = button_image_5
        button_5.place(x=0.0, y=549.0, width=111.0, height=111.0)

        button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.insert_data,
            relief="flat"
        )
        button_6.image = button_image_6
        button_6.place(x=560.0, y=590.0, width=242.0, height=65.0)
    
    def setup_ui_elements(self):
        self.canvas.create_rectangle(
            0.0,
            0.0,
            111.0,
            720.0,
            fill="#E2DAD6",
            outline="")

        self.canvas.create_rectangle(
            123.0,
            0.0,
            1270.0,
            183.0,
            fill="#E2DAD6",
            outline="")

        self.canvas.create_rectangle(
            123.0,
            0.0,
            1270.0,
            60.0,
            fill="#DFD3C3",
            outline="")

        self.canvas.create_text(
            479.0,
            4.0,
            anchor="nw",
            text="TAMBAH BARANG",
            fill="#000000",
            font=("Nunito Bold", 40 * -1)
        )

        self.canvas.create_rectangle(
            166.0,
            68.0,
            632.0,
            174.0,
            fill="#DFD3C3",
            outline="")

        self.canvas.create_rectangle(
            761.0,
            68.0,
            1227.0,
            174.0,
            fill="#DFD3C3",
            outline="")


        self.canvas.create_text(
            177.0,
            76.0,
            anchor="nw",
            text="Banyak \nBarang:",
            fill="#000000",
            font=("Nunito Bold", 32 * -1)
        )

        self.canvas.create_text(
            782.0,
            76.0,
            anchor="nw",
            text="Jumlah \nStok:",
            fill="#000000",
            font=("Nunito Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            134.0,
            213.0,
            1260.0,
            687.0,
            fill="#D9D9D9",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            690.0,
            333.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Nunito",14),
        )
        self.entry_1.place(
            x=180.0,
            y=306.0,
            width=1026.0,
            height=52.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            690.0,
            436.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Nunito",14),
        )
        self.entry_2.place(
            x=180.0,
            y=409.0,
            width=1026.0,
            height=52.0
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_3 = self.canvas.create_image(
            690.0,
            333.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Nunito",14),
        )
        self.entry_3.place(
            x=180.0,
            y=508.0,
            width=1026.0,
            height=52.0
        )

        self.canvas.create_rectangle(
            179.0,
            359.0,
            1168.0,
            360.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            179.0,
            462.0,
            1165.0,
            463.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            179.0,
            562.0,
            1165.0,
            563.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            179.0,
            270.0,
            anchor="nw",
            text="MASUKAN NAMA BARANG YANG AKAN DITAMBAHKAN:",
            fill="#000000",
            font=("Nunito Bold", 20 * -1)
        )

        self.canvas.create_text(
            179.0,
            373.0,
            anchor="nw",
            text="MASUKAN JUMLAH STOK YANG AKAN DITAMBAHKAN:",
            fill="#000000",
            font=("Nunito Bold", 20 * -1)
        )

        self.canvas.create_text(
            179.0,
            472.0,
            anchor="nw",
            text="MASUKAN HARGA BARANG YANG AKAN DITAMBAHKAN:",
            fill="#000000",
            font=("Nunito Bold", 20 * -1)
        )
        
        # Mengambil jumlah barang dan stok dari database
        total_items = len(self.data)
        total_stocks = sum([item[1] for item in self.data])  # item[1] adalah `stok barang`
        # Menampilkan jumlah barang dan stok
        self.canvas.create_text(
            450.0, 
            83.0, 
            anchor="nw", 
            text=total_items, 
            fill="#000000", 
            font=("Nunito Bold", 48 * -1))
        self.canvas.create_text(
            1055.0, 
            81.0, 
            anchor="nw", 
            text=total_stocks, 
            fill="#000000", 
            font=("Nunito Bold", 48 * -1))

    def close_connection(self):
        self.cursor.close()
        self.mydb.close()


class Read:
    def connect_to_database(self):
        self.mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="# Your sql password ",
            database="# Your own database "
        )
        self.cursor = self.mydb.cursor()

    def fetch_data(self):
        query = "SELECT `nama barang`, `stok barang`, `harga barang` FROM `database toko` ORDER BY `id` DESC LIMIT 9"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def __init__(self, root):
        self.root = root
        self.connect_to_database()
        self.data = self.fetch_data()
        self.root.geometry("1280x720")
        # Center the window on the screen
        window_width = 1280
        window_height = 720

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)

        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.configure(bg="#144272")

        self.canvas = Canvas(
            self.root,
            bg="#144272",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            0.0,
            0.0,
            111.0,
            720.0,
            fill="#E2DAD6",
            outline=""
        )

        self.setup_buttons()
        self.setup_ui_elements()

        self.root.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"E:\CRUD Python-MySQL Warung\build\assets\frame3")
        return ASSETS_PATH / Path(path)
    
    def open_main_app(self):
        self.root.destroy()  # Menutup jendela saat ini
        root = Tk()
        MainApp(root)  # Menginisialisasi GUI dari kelas MainApp
        root.mainloop()

    def open_create(self):
        self.root.destroy()
        root = Tk()
        Create(root)
        root.mainloop

    def open_read(self):
        self.root.destroy()
        root = Tk()
        Read(root)  # Menginisialisasi GUI dari kelas Read
        root.mainloop()

    def open_update(self):
        self.root.destroy()
        root = Tk()
        Update(root)  # Menginisialisasi GUI dari kelas Update
        root.mainloop()

    def open_delete(self):
        self.root.destroy()
        root = Tk()
        Delete(root)  # Menginisialisasi GUI dari kelas Delete
        root.mainloop()
    
    def show_search_result(self, message):
        # Hapus hasil pencarian sebelumnya (jika ada)
        for widget in self.root.place_slaves():
            if isinstance(widget, Label) and widget.winfo_y() > 436:
                widget.destroy()

        # Tampilkan hasil pencarian baru
        result_label = Label(self.root, 
                             text=message, 
                             bg="#D9D9D9", 
                             fg="red", 
                             font=("Nunito Bold", 14), 
                             anchor="w"
                             )
        result_label.place(x=180, 
                           y=450, 
                           width=1026, 
                           height=52)

    def search_item(self):
        # Ambil nama barang dari entry
        item_name = self.entry_1.get()
        
        # Query untuk mencari barang berdasarkan nama
        query = "SELECT `nama barang`, `stok barang`, `harga barang` FROM `database toko` WHERE `nama barang` = %s"
        self.cursor.execute(query, (item_name,))
        result = self.cursor.fetchone()
        
        # Jika barang ditemukan, tampilkan informasi
        if result:
            item_name, stock, price = result
            message = f"{item_name} memiliki stok {stock} seharga {price}/pcs"
        else:
            message = f"Barang dengan nama {item_name} tidak ditemukan."
        
        # Tampilkan hasil pencarian
        self.show_search_result(message)
    
    def setup_buttons(self):
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_main_app,
            relief="flat"
        )
        button_1.image = button_image_1  # Keep a reference to avoid garbage collection
        button_1.place(x=0.0, y=0.0, width=111.0, height=71.5)

        button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_create,
            relief="flat"
        )
        button_2.image = button_image_2
        button_2.place(x=0.0, y=102.0, width=111.0, height=111.0)

        button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.image = button_image_3
        button_3.place(x=0.0, y=251.0, width=111.0, height=111.0)

        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_update,
            relief="flat"
        )
        button_4.image = button_image_4
        button_4.place(x=0.0, y=400.0, width=111.0, height=111.0)

        button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_delete,
            relief="flat"
        )
        button_5.image = button_image_5
        button_5.place(x=0.0, y=549.0, width=111.0, height=111.0)

        button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.search_item,
            relief="flat"
        )
        button_6.image = button_image_6
        button_6.place(x=569.0, y=542.0, width=242.0, height=65.0)

    def setup_ui_elements(self):
        self.canvas.create_rectangle(
            123.0,
            0.0,
            1270.0,
            183.0,
            fill="#E2DAD6",
            outline=""
        )

        self.canvas.create_rectangle(
            123.0,
            0.0,
            1270.0,
            60.0,
            fill="#DFD3C3",
            outline=""
        )

        self.canvas.create_text(
            554.0,
            4.0,
            anchor="nw",
            text="CARI BARANG",
            fill="#000000",
            font=("Nunito Bold", 40 * -1)
        )

        self.canvas.create_rectangle(
            166.0,
            68.0,
            632.0,
            174.0,
            fill="#DFD3C3",
            outline=""
        )

        self.canvas.create_rectangle(
            761.0,
            68.0,
            1227.0,
            174.0,
            fill="#DFD3C3",
            outline=""
        )

        self.canvas.create_text(
            177.0,
            76.0,
            anchor="nw",
            text="Banyak \nBarang:",
            fill="#000000",
            font=("Nunito Bold", 32 * -1)
        )

        self.canvas.create_text(
            782.0,
            76.0,
            anchor="nw",
            text="Jumlah \nStok:",
            fill="#000000",
            font=("Nunito Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            134.0,
            213.0,
            1260.0,
            687.0,
            fill="#D9D9D9",
            outline=""
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png")
        )
        self.entry_bg_1 = self.canvas.create_image(
            690.0,
            409.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Nunito", 14)
        )
        self.entry_1.place(
            x=177.0,
            y=382.0,
            width=1026.0,
            height=52.0
        )

        self.canvas.create_rectangle(
            179.0,
            435.0,
            1168.0,
            436.0,
            fill="#000000",
            outline=""
        )

        self.canvas.create_text(
            180.0,
            346.0,
            anchor="nw",
            text="MASUKAN NAMA BARANG YANG AKAN DICARI:",
            fill="#000000",
            font=("Nunito Bold", 20 * -1)
        )

        # Mengambil jumlah barang dan stok dari database
        total_items = len(self.data)
        total_stocks = sum([item[1] for item in self.data])
        
        # Menampilkan jumlah barang dan stok
        self.canvas.create_text(
            450.0, 
            83.0, 
            anchor="nw", 
            text=total_items, 
            fill="#000000", 
            font=("Nunito Bold", 48 * -1))
        self.canvas.create_text(
            1055.0, 
            81.0, 
            anchor="nw", 
            text=total_stocks, 
            fill="#000000", 
            font=("Nunito Bold", 48 * -1))

class Update:
    def connect_to_database(self):
        self.mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="# Your sql password ",
            database="# Your own database "
        )
        self.cursor = self.mydb.cursor()

    def fetch_data(self):
        query = "SELECT `nama barang`, `stok barang`, `harga barang` FROM `database toko` ORDER BY `id` DESC LIMIT 9"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def __init__(self, root):
        self.root = root
        self.connect_to_database()
        self.data = self.fetch_data()
        self.root.geometry("1280x720")
        self.error_label = None
        # Center the window on the screen
        window_width = 1280
        window_height = 720

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)

        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.configure(bg="#144272")

        self.canvas = Canvas(
            self.root,
            bg="#144272",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            0.0,
            0.0,
            111.0,
            720.0,
            fill="#E2DAD6",
            outline=""
        )

        self.setup_buttons()
        self.setup_ui_elements()

        self.root.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"E:\CRUD Python-MySQL Warung\build\assets\frame1")
        return ASSETS_PATH / Path(path)
    
    def open_main_app(self):
        self.root.destroy()  # Menutup jendela saat ini
        root = Tk()
        MainApp(root)  # Menginisialisasi GUI dari kelas MainApp
        root.mainloop()

    def open_create(self):
        self.root.destroy()
        root = Tk()
        Create(root)
        root.mainloop

    def open_read(self):
        self.root.destroy()
        root = Tk()
        Read(root)  # Menginisialisasi GUI dari kelas Read
        root.mainloop()

    def open_update(self):
        self.root.destroy()
        root = Tk()
        Update(root)  # Menginisialisasi GUI dari kelas Update
        root.mainloop()

    def open_delete(self):
        self.root.destroy()
        root = Tk()
        Delete(root)  # Menginisialisasi GUI dari kelas Delete
        root.mainloop()

    def update_data(self):
        nama_barang = self.entry_1.get()
        stok_barang = self.entry_2.get()
        harga_barang = self.entry_3.get()

        if nama_barang and stok_barang and harga_barang:
            try:
                # Check if the item exists
                check_query = "SELECT * FROM `database toko` WHERE `nama barang` = %s"
                self.cursor.execute(check_query, (nama_barang,))
                result = self.cursor.fetchone()
                if result:
                    query = "UPDATE `database toko` SET `stok barang` = %s, `harga barang` = %s WHERE `nama barang` = %s"
                    self.cursor.execute(query, (stok_barang, harga_barang, nama_barang))
                    self.mydb.commit()

                    # Reset input fields
                    self.entry_1.delete(0, 'end')
                    self.entry_2.delete(0, 'end')
                    self.entry_3.delete(0, 'end')

                    # Remove any previous error message
                    if self.error_label:
                        self.canvas.delete(self.error_label)
                        self.error_label = None

                    # Display success message
                    self.error_label = self.canvas.create_text(
                        177.0,
                        570.0,
                        anchor="nw",
                        text="Barang berhasil DIUPDATE",
                        fill="red",
                        font=("Nunito Bold", 14 * -1)
                    )
                else:
                    # Display error message if item not found
                    if self.error_label:
                        self.canvas.delete(self.error_label)
                    self.error_label = self.canvas.create_text(
                        177.0,
                        570.0,
                        anchor="nw",
                        text="ERROR!! Nama barang tidak ditemukan",
                        fill="red",
                        font=("Nunito Bold", 14 * -1)
                    )
            except Exception as e:
                print(f"Error: {e}")
                self.mydb.rollback()
        else:
            # Display error message if fields are empty
            if self.error_label:
                self.canvas.delete(self.error_label)
            self.error_label = self.canvas.create_text(
                177.0,
                570.0,
                anchor="nw",
                text="ERROR!! Entry kosong atau nama barang tidak ditemukan",
                fill="red",
                font=("Nunito Bold", 14 * -1)
            )

    def setup_buttons(self):
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_main_app,
            relief="flat"
        )
        button_1.image = button_image_1  # Keep a reference to avoid garbage collection
        button_1.place(x=0.0, y=0.0, width=111.0, height=71.5)

        button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_create,
            relief="flat"
        )
        button_2.image = button_image_2
        button_2.place(x=0.0, y=102.0, width=111.0, height=111.0)

        button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_read,
            relief="flat"
        )
        button_3.image = button_image_3
        button_3.place(x=0.0, y=251.0, width=111.0, height=111.0)

        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_update,
            relief="flat"
        )
        button_4.image = button_image_4
        button_4.place(x=0.0, y=400.0, width=111.0, height=111.0)

        button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_delete,
            relief="flat"
        )
        button_5.image = button_image_5
        button_5.place(x=0.0, y=549.0, width=111.0, height=111.0)

        button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.update_data,
            relief="flat"
        )
        button_6.image = button_image_6
        button_6.place(x=560.0, y=604.0, width=242.0, height=65.0)

    def setup_ui_elements(self):
        self.canvas.create_rectangle(
            123.0,
            0.0,
            1270.0,
            183.0,
            fill="#E2DAD6",
            outline="")

        self.canvas.create_rectangle(
            123.0,
            0.0,
            1270.0,
            60.0,
            fill="#DFD3C3",
            outline="")

        self.canvas.create_text(
            479.0,
            4.0,
            anchor="nw",
            text="UPDATE BARANG",
            fill="#000000",
            font=("Nunito Bold", 40 * -1)
        )

        self.canvas.create_rectangle(
            166.0,
            68.0,
            632.0,
            174.0,
            fill="#DFD3C3",
            outline="")

        self.canvas.create_rectangle(
            761.0,
            68.0,
            1227.0,
            174.0,
            fill="#DFD3C3",
            outline="")

        self.canvas.create_text(
            177.0,
            76.0,
            anchor="nw",
            text="Banyak \nBarang:",
            fill="#000000",
            font=("Nunito Bold", 32 * -1)
        )

        self.canvas.create_text(
            782.0,
            76.0,
            anchor="nw",
            text="Jumlah \nStok:",
            fill="#000000",
            font=("Nunito Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            134.0,
            213.0,
            1260.0,
            687.0,
            fill="#D9D9D9",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            690.0,
            333.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Nunito",14),
        )
        self.entry_1.place(
            x=180.0,
            y=306.0,
            width=1026.0,
            height=52.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            690.0,
            436.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Nunito",14),
        )
        self.entry_2.place(
            x=180.0,
            y=409.0,
            width=1026.0,
            height=52.0
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_3 = self.canvas.create_image(
            690.0,
            333.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Nunito",14),
        )
        self.entry_3.place(
            x=180.0,
            y=508.0,
            width=1026.0,
            height=52.0
        )

        self.canvas.create_rectangle(
            179.0,
            359.0,
            1168.0,
            360.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            179.0,
            462.0,
            1165.0,
            463.0,
            fill="#000000",
            outline="")
        
        self.canvas.create_rectangle(
            179.0,
            562.0,
            1165.0,
            563.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            179.0,
            253.0,
            anchor="nw",
            text="MASUKAN NAMA BARANG YANG AKAN DIUPDATE",
            fill="#000000",
            font=("Nunito Bold", 20 * -1)
        )

        self.canvas.create_text(
            179.0,
            278.0,
            anchor="nw",
            text="(NAMA BARANG HARUS SESUAI DENGAN NAMA DI DATABASE):",
            fill="red",
            font=("Nunito Bold", 12)
        )

        self.canvas.create_text(
            177.0,
            373.0,
            anchor="nw",
            text="MASUKAN JUMLAH STOK YANG AKAN DIUPDATE:",
            fill="#000000",
            font=("Nunito Bold", 20 * -1)
        )

        self.canvas.create_text(
            179.0,
            472.0,
            anchor="nw",
            text="MASUKAN HARGA BARANG YANG AKAN DIUPDATE:",
            fill="#000000",
            font=("Nunito Bold", 20 * -1)
        )
        
        # Mengambil jumlah barang dan stok dari database
        total_items = len(self.data)
        total_stocks = sum([item[1] for item in self.data])  # item[1] adalah stok barang
        # Menampilkan jumlah barang dan stok
        self.canvas.create_text(
            450.0, 
            83.0, 
            anchor="nw", 
            text=total_items, 
            fill="#000000", 
            font=("Nunito Bold", 48 * -1))
        self.canvas.create_text(
            1055.0, 
            81.0, 
            anchor="nw", 
            text=total_stocks, 
            fill="#000000", 
            font=("Nunito Bold", 48 * -1))

    def close_connection(self):
        self.cursor.close()
        self.mydb.close()

class Delete:
    def connect_to_database(self):
        self.mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="# Your sql password ",
            database="# Your own database "
        )
        self.cursor = self.mydb.cursor()

    def fetch_data(self):
        query = "SELECT `nama barang`, `stok barang`, `harga barang` FROM `database toko` ORDER BY `id` DESC LIMIT 9"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def __init__(self, root):
        self.root = root
        self.connect_to_database()
        self.data = self.fetch_data()
        self.root.geometry("1280x720")
        # Center the window on the screen
        window_width = 1280
        window_height = 720

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)

        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.configure(bg="#144272")

        self.canvas = Canvas(
            self.root,
            bg="#144272",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            0.0,
            0.0,
            111.0,
            720.0,
            fill="#E2DAD6",
            outline=""
        )

        self.setup_buttons()
        self.setup_ui_elements()

        self.root.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"E:\CRUD Python-MySQL Warung\build\assets\frame0")
        return ASSETS_PATH / Path(path)
    
    def open_main_app(self):
        self.root.destroy()  # Menutup jendela saat ini
        root = Tk()
        MainApp(root)  # Menginisialisasi GUI dari kelas MainApp
        root.mainloop()

    def open_create(self):
        self.root.destroy()
        root = Tk()
        Create(root)
        root.mainloop

    def open_read(self):
        self.root.destroy()
        root = Tk()
        Read(root)  # Menginisialisasi GUI dari kelas Read
        root.mainloop()

    def open_update(self):
        self.root.destroy()
        root = Tk()
        Update(root)  # Menginisialisasi GUI dari kelas Update
        root.mainloop()

    def open_delete(self):
        self.root.destroy()
        root = Tk()
        Delete(root)  # Menginisialisasi GUI dari kelas Delete
        root.mainloop()

    def tampilan_peringatan(self, message):
        # Hapus hasil pencarian sebelumnya (jika ada)
        for widget in self.root.place_slaves():
            if isinstance(widget, Label) and widget.winfo_y() > 436:
                widget.destroy()

        # Tampilkan hasil pencarian baru
        result_label = Label(self.root, 
                             text=message, 
                             bg="#D9D9D9", 
                             fg="red", 
                             font=("Nunito Bold", 14), 
                             anchor="w"
                             )
        result_label.place(x=180, 
                           y=450, 
                           width=1026, 
                           height=52)

    def hapus_item(self):
        # Ambil nama barang dari entry
        item_name = self.entry_1.get()
        
        # Query untuk menghapus barang berdasarkan nama
        query = "DELETE FROM `database toko` WHERE `nama barang` = %s"
        self.cursor.execute(query, (item_name,))
        self.mydb.commit()
        
        # Periksa berapa banyak baris yang terpengaruh
        if self.cursor.rowcount > 0:
            message = f"Data''{item_name}'' telah berhasil dihapus!"

            # menghapus entry user yang sebelumnya
            self.entry_1.delete(0, 'end')
        else:
            message = f"Barang dengan nama ''{item_name}'' tidak ditemukan."
            self.entry_1.delete(0, 'end')
        
        # Tampilkan pesan ke canvas (atau tempat lain yang sesuai dalam GUI Anda)
        self.canvas.create_text(
            177.0,
            441.0,
            anchor="nw",
            text=message,
            fill="red",
            font=("Nunito Bold", 14 * -1)
        )
    
    def setup_buttons(self):
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_main_app,
            relief="flat"
        )
        button_1.image = button_image_1  # Keep a reference to avoid garbage collection
        button_1.place(x=0.0, y=0.0, width=111.0, height=71.5)

        button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_create,
            relief="flat"
        )
        button_2.image = button_image_2
        button_2.place(x=0.0, y=102.0, width=111.0, height=111.0)

        button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_read,
            relief="flat"
        )
        button_3.image = button_image_3
        button_3.place(x=0.0, y=251.0, width=111.0, height=111.0)

        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_update,
            relief="flat"
        )
        button_4.image = button_image_4
        button_4.place(x=0.0, y=400.0, width=111.0, height=111.0)

        button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_delete,
            relief="flat"
        )
        button_5.image = button_image_5
        button_5.place(x=0.0, y=549.0, width=111.0, height=111.0)

        button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.hapus_item,
            relief="flat"
        )
        button_6.image = button_image_6
        button_6.place(x=569.0, y=542.0, width=242.0, height=65.0)
    
    def setup_ui_elements(self):
        self.canvas.create_rectangle(
            123.0,
            0.0,
            1270.0,
            183.0,
            fill="#E2DAD6",
            outline="")

        self.canvas.create_rectangle(
            123.0,
            0.0,
            1270.0,
            60.0,
            fill="#DFD3C3",
            outline="")

        self.canvas.create_rectangle(
            123.0,
            0.0,
            1270.0,
            183.0,
            fill="#E2DAD6",
            outline="")

        self.canvas.create_rectangle(
            123.0,
            0.0,
            1270.0,
            60.0,
            fill="#DFD3C3",
            outline="")

        self.canvas.create_text(
            479.0,
            4.0,
            anchor="nw",
            text="HAPUS DATA BARANG",
            fill="#000000",
            font=("Nunito Bold", 40 * -1)
        )

        self.canvas.create_rectangle(
            166.0,
            68.0,
            632.0,
            174.0,
            fill="#DFD3C3",
            outline="")

        self.canvas.create_rectangle(
            761.0,
            68.0,
            1227.0,
            174.0,
            fill="#DFD3C3",
            outline="")

        self.canvas.create_text(
            177.0,
            76.0,
            anchor="nw",
            text="Banyak \nBarang:",
            fill="#000000",
            font=("Nunito Bold", 32 * -1)
        )

        self.canvas.create_text(
            782.0,
            76.0,
            anchor="nw",
            text="Jumlah \nStok:",
            fill="#000000",
            font=("Nunito Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            134.0,
            213.0,
            1260.0,
            687.0,
            fill="#D9D9D9",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png")
        )
        self.entry_bg_1 = self.canvas.create_image(
            690.0,
            409.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Nunito", 14)
        )
        self.entry_1.place(
            x=177.0,
            y=382.0,
            width=1026.0,
            height=52.0
        )

        self.canvas.create_rectangle(
            179.0,
            435.0,
            1168.0,
            436.0,
            fill="#000000",
            outline=""
        )

        self.canvas.create_text(
            180.0,
            346.0,
            anchor="nw",
            text="MASUKAN NAMA BARANG YANG AKAN DIHAPUS:",
            fill="#000000",
            font=("Nunito Bold", 20 * -1)
        )

        # Mengambil jumlah barang dan stok dari database
        total_items = len(self.data)
        total_stocks = sum([item[1] for item in self.data])  # item[1] adalah stok barang
        # Menampilkan jumlah barang dan stok
        self.canvas.create_text(
            450.0, 
            83.0, 
            anchor="nw", 
            text=total_items, 
            fill="#000000", 
            font=("Nunito Bold", 48 * -1))
        self.canvas.create_text(
            1055.0, 
            81.0, 
            anchor="nw", 
            text=total_stocks, 
            fill="#000000", 
            font=("Nunito Bold", 48 * -1))

    def close_connection(self):
        self.cursor.close()
        self.mydb.close()

if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()