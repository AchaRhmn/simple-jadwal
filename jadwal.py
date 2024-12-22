# dictionary jadwal
hari = {'senin    ':'kuliah algoritma & jaringan',
            'selasa   ':'kuliah basisdata & MTK',
            'rabu     ':'kuliah algoritma',
            'kamis    ':'kuliah desain web & PBD',
            'jumat    ':'Libur',
            'sabtu    ':'Libur',
            'minggu   ':'Libur'}

# perulangan tampilan opsi
while True :
      j = "\n\nprogram jadwal python\n"
      j = j.upper()
      print(j)
      print("Pilih opsi :")

      print("1. tampilkan jadwal")
      print("2. edit jadwal")
      print("3. reset jadwal")
      p = input("\npilih opsi (1/2/3): ")

      pilih = {'1': 'tampilkan jadwal', '2': 'edit jadwal', '3': 'reset jadwal'}

    # definisi key dari input user
      if p in pilih :
          keyp = pilih[p]

    # tampil jadwal
      if keyp == 'tampilkan jadwal' :
        for i in hari :
           print(('{: <10}'.format(i)), "  :", hari[i])

    # edit jadwal
      elif keyp == 'edit jadwal' :

        e = input("pilih hari : ")

        # ngilangin spacing
        h = {k.strip(): v for k, v in hari.items()}
        hari = h

        # process edit
        if e in h :
          print("\n",e, "  :", hari[e])

          edit = input(" edit jadwal : ")
          hari[e] = edit
          print("\n",e, "  :", hari[e])

        else :
          print("invalid")

    # reset jadwal
      elif keyp == 'reset jadwal' :
        print("\njadwal berhasil di reset")
        hari = {'senin    ':'kuliah algoritma & jaringan',
                'selasa   ':'kuliah basisdata & MTK',
                'rabu     ':'kuliah algoritma',
                'kamis    ':'kuliah desain web & PBD',
                'jumat    ':'Libur',
                'sabtu    ':'Libur',}


        for i in hari :
           print(('{: <10}'.format(i)), "  :", hari[i])

    # else invalid
      else :
        print("invalid")

        