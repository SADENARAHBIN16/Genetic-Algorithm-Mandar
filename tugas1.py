
import random

DATA_KATA = [
    "MATTAMA",
    "MATTUJU",
    "MATTUNU",
    "MATTANA",
    "MATTARE",
    "MATTAKE",
    "MATTALA",
    "MATTAPA",
    "MATINDO",
    "MATTEMA"
]

TARGET_KATA = "MATTARO"

generasi_awal = DATA_KATA[:]
nilai_fitness = []
peluang = []
rentang = []

induk_1 = ""
induk_2 = ""
anak_1 = ""
anak_2 = ""
anak_mutasi = ""

def nilai(kata):
    cocok = sum(1 for a,b in zip(kata,TARGET_KATA) if a==b)
    return cocok/len(TARGET_KATA), cocok

def lihat_kamus():
    print("\n=== DATA KAMUS ===")
    for no,k in enumerate(DATA_KATA,1):
        print(f"{no}. {k}")

def pencarian():
    k=input("Masukkan kata : ").upper()
    print("Kata ditemukan." if k in DATA_KATA else "Kata tidak ditemukan.")

def evaluasi_fitness():
    global nilai_fitness
    nilai_fitness=[]
    total=0
    print("\n=== EVALUASI FITNESS ===")
    for i,k in enumerate(generasi_awal,1):
        f,c=nilai(k)
        nilai_fitness.append(f)
        total+=f
        print(f"I{i} {k} | Benar={c} | Fitness={f:.4f}")
    print("Total Fitness =",round(total,4))

def seleksi_parent():
    global peluang,rentang,induk_1,induk_2
    if not nilai_fitness:
        evaluasi_fitness()
    total=sum(nilai_fitness)
    peluang=[]; rentang=[]
    kum=0
    print("\n=== SELEKSI ROULETTE ===")
    for i,f in enumerate(nilai_fitness):
        p=f/total
        awal=kum
        kum+=p
        peluang.append(p); rentang.append((awal,kum))
        print(f"I{i+1} P={p:.4f} Interval=({awal:.4f}-{kum:.4f})")
    for r,nm in [(random.random(),"1"),(random.random(),"2")]:
        print(f"Random {nm} = {r:.4f}")
        for idx,(a,b) in enumerate(rentang):
            if a<=r<=b:
                if nm=="1": induk_1=generasi_awal[idx]
                else: induk_2=generasi_awal[idx]
                break
    print("Induk 1 :",induk_1)
    print("Induk 2 :",induk_2)

def persilangan():
    global anak_1,anak_2
    cut=4
    anak_1=induk_1[:cut]+induk_2[cut:]
    anak_2=induk_2[:cut]+induk_1[cut:]
    print("\n=== CROSSOVER ===")
    print("Anak 1 :",anak_1)
    print("Anak 2 :",anak_2)

def proses_mutasi():
    global anak_mutasi
    huruf=list(anak_2)
    salah=[i for i,h in enumerate(huruf) if h!=TARGET_KATA[i]]
    print("\n=== MUTASI ===")
    if not salah:
        anak_mutasi="".join(huruf)
        print("Tidak perlu mutasi.")
        return
    pos=random.choice(salah)
    print("Sebelum :", "".join(huruf))
    huruf[pos]=TARGET_KATA[pos]
    anak_mutasi="".join(huruf)
    f,c=nilai(anak_mutasi)
    print("Sesudah :",anak_mutasi)
    print("Fitness :",round(f,4),"Benar:",c)

def evaluasi_generasi():
    f1,_=nilai(anak_1)
    f2,_=nilai(anak_mutasi)
    print("\n=== GENERASI BARU ===")
    print(anak_1,f1)
    print(anak_mutasi,f2)
    print("TARGET BERHASIL DITEMUKAN" if anak_mutasi==TARGET_KATA else "Belum mencapai target.")

while True:
    print("\n1.Lihat Kamus\n2.Cari Kata\n3.Hitung Fitness\n4.Populasi\n5.Tampilkan Fitness\n6.Roulette\n7.Crossover\n8.Mutasi\n9.Generasi Baru\n10.Keluar")
    p=input("Pilih menu : ")
    if p=="1": lihat_kamus()
    elif p=="2": pencarian()
    elif p=="3": evaluasi_fitness()
    elif p=="4":
        for i,k in enumerate(generasi_awal,1): print(i,k)
    elif p=="5": evaluasi_fitness()
    elif p=="6": seleksi_parent()
    elif p=="7": persilangan()
    elif p=="8": proses_mutasi()
    elif p=="9": evaluasi_generasi()
    elif p=="10":
        print("Program selesai."); break
    else:
        print("Pilihan tidak valid.")
