meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "OTW": "Menuju suatu tempat"
            }

while True:
    word = input('Kata apa yang anda tidak mengerti(gunakan huruf kapital!)')
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Kata tersebut tidak ada di dalam kamus')
        
