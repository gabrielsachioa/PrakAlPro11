def bandingkan_anggota(tA):
    
    for anggota in tA:
        if anggota == tA[0]:
            return True
        else:
            return False

tA= (90, 90, 90, 90)
print(bandingkan_anggota(tA))