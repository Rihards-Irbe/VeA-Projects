import pandas as pd

noklusetas_vertibas = True
try:
    try:
        distance_xlsx = pd.read_excel("distances.xlsx", header=None)
        attalumi = distance_xlsx.iloc[1:, 1:].values.tolist()

        pilsetas = distance_xlsx.iloc[0, 1:].tolist()
        noklusetas_vertibas = False
    except FileNotFoundError:
        kluda = "Excel failu nevarēja atrast, tāpēc attalumi un pilsetas sastāv no noklusējamām vērtībām"
except ModuleNotFoundError:
    kluda = "Bibliotēka, kas nolasa datus no xlsx faila nav pievienota, tāpēc attalumi un pilsetas sastāv no noklusējamām vērtībām"

if(noklusetas_vertibas):
    print(kluda)
    attalumi = [
        [0, 293, 344, 125, 78, 273, 109, 214, 184, 426, 396, 228, 332, 461, 270, 119, 58, 457, 166, 175, 335, 369, 166, 421, 274, 237, 403, 386, 283, 333],
        [293, 0, 50, 207, 259, 63, 255, 117, 106, 184, 220, 126, 115, 211, 46, 351, 299, 278, 167, 173, 174, 97, 201, 261, 31, 174, 135, 115, 168, 85],
        [344, 50, 0, 257, 309, 113, 305, 167, 156, 196, 260, 176, 155, 223, 96, 401, 349, 285, 217, 223, 214, 109, 251, 301, 81, 224, 147, 103, 218, 133],
        [125, 207, 257, 0, 56, 152, 72, 90, 63, 313, 275, 107, 243, 340, 189, 168, 96, 336, 45, 54, 214, 282, 45, 300, 188, 106, 320, 300, 162, 212],
        [78, 259, 309, 56, 0, 204, 83, 142, 115, 365, 327, 159, 295, 392, 241, 145, 58, 388, 85, 106, 266, 334, 98, 352, 240, 160, 372, 352, 214, 264],
        [273, 63, 113, 152, 204, 0, 200, 62, 51, 211, 218, 55, 115, 238, 54, 296, 244, 279, 112, 118, 157, 133, 146, 243, 39, 119, 171, 151, 105, 109],
        [109, 255, 305, 72, 83, 200, 0, 138, 119, 361, 323, 155, 291, 388, 237, 98, 52, 384, 105, 82, 262, 330, 54, 348, 236, 132, 368, 348, 210, 260],
        [214, 117, 167, 90, 142, 62, 138, 0, 19, 223, 185, 17, 153, 250, 99, 234, 182, 246, 50, 56, 124, 192, 84, 210, 98, 57, 230, 210, 72, 122],
        [184, 106, 156, 63, 115, 51, 119, 19, 0, 242, 204, 36, 172, 269, 88, 215, 155, 265, 23, 47, 143, 181, 78, 229, 87, 67, 219, 199, 91, 111],
        [426, 184, 196, 313, 365, 211, 361, 223, 242, 0, 53, 206, 95, 30, 228, 457, 405, 87, 273, 279, 103, 87, 307, 93, 183, 234, 78, 125, 155, 290],
        [396, 220, 260, 275, 327, 218, 323, 185, 204, 53, 0, 168, 104, 82, 237, 419, 367, 59, 235, 241, 65, 142, 269, 55, 192, 196, 133, 180, 117, 301],
        [228, 126, 176, 107, 159, 55, 155, 17, 36, 206, 168, 0, 136, 233, 108, 251, 199, 229, 67, 73, 107, 188, 101, 193, 89, 74, 226, 211, 55, 131],
        [332, 115, 155, 243, 295, 115, 291, 153, 172, 95, 104, 136, 0, 122, 132, 387, 335, 163, 203, 209, 61, 51, 237, 147, 87, 164, 89, 96, 85, 194],
        [461, 211, 223, 340, 392, 238, 388, 250, 269, 30, 82, 233, 122, 0, 255, 484, 432, 98, 300, 306, 130, 114, 334, 122, 210, 261, 85, 132, 182, 317],
        [270, 46, 96, 189, 241, 54, 237, 99, 88, 228, 237, 108, 132, 255, 0, 333, 281, 296, 149, 155, 192, 141, 183, 278, 45, 153, 179, 159, 163, 62],
        [219, 351, 401, 168, 145, 296, 98, 234, 215, 457, 419, 251, 387, 484, 333, 0, 91, 480, 201, 178, 358, 426, 150, 444, 332, 228, 464, 444, 306, 356],
        [58, 299, 349, 96, 58, 244, 52, 182, 155, 405, 367, 199, 335, 432, 281, 91, 0, 428, 137, 132, 306, 374, 104, 392, 280, 182, 412, 392, 254, 304],
        [457, 278, 285, 336, 388, 279, 384, 246, 265, 87, 59, 229, 163, 98, 296, 280, 428, 0, 296, 302, 126, 176, 330, 44, 251, 257, 167, 214, 178, 362],
        [166, 167, 217, 45, 85, 112, 105, 50, 23, 273, 235, 67, 203, 300, 149, 201, 137, 296, 0, 57, 174, 242, 64, 260, 148, 87, 280, 260, 122, 172],
        [175, 173, 223, 54, 106, 118, 82, 56, 47, 279, 241, 73, 209, 306, 155, 178, 132, 302, 57, 0, 180, 248, 28, 266, 154, 62, 286, 266, 128, 178],
        [335, 174, 214, 214, 266, 157, 262, 124, 143, 103, 65, 107, 61, 130, 192, 358, 306, 126, 174, 180, 0, 113, 208, 90, 147, 135, 151, 158, 56, 238],
        [369, 97, 109, 282, 334, 133, 330, 192, 181, 87, 142, 188, 51, 114, 141, 426, 374, 176, 242, 248, 113, 0, 276, 199, 105, 116, 38, 45, 137, 190],
        [166, 201, 251, 45, 98, 146, 54, 84, 78, 307, 269, 101, 237, 334, 183, 150, 104, 330, 64, 28, 208, 276, 0, 294, 182, 79, 314, 294, 156, 206],
        [421, 261, 301, 300, 352, 243, 348, 210, 229, 93, 55, 193, 147, 122, 278, 444, 392, 44, 260, 266, 90, 199, 294, 0, 233, 221, 173, 220, 142, 326],
        [274, 31, 81, 188, 240, 39, 236, 98, 87, 183, 192, 89, 87, 210, 45, 332, 280, 251, 148, 154, 147, 105, 182, 233, 0, 155, 143, 123, 139, 107],
        [237, 174, 224, 106, 160, 119, 132, 57, 67, 234, 196, 74, 164, 261, 153, 228, 182, 257, 87, 62, 135, 216, 79, 221, 155, 0, 254, 267, 79, 179],
        [403, 135, 147, 320, 372, 171, 368, 230, 219, 78, 133, 226, 89, 85, 179, 464, 412, 167, 280, 286, 151, 38, 314, 173, 143, 254, 0, 47, 175, 228],
        [386, 115, 103, 300, 352, 151, 348, 210, 199, 125, 180, 211, 96, 132, 159, 444, 392, 214, 260, 266, 158, 45, 294, 220, 123, 267, 47, 0, 182, 212],
        [283, 168, 218, 162, 214, 105, 210, 72, 91, 155, 117, 55, 85, 182, 163, 306, 254, 178, 122, 128, 56, 137, 156, 142, 139, 79, 175, 182, 0, 186],
        [333, 85, 133, 212, 264, 109, 260, 122, 111, 290, 301, 131, 194, 317, 62, 356, 304, 362, 172, 178, 238, 190, 206, 326, 107, 179, 228, 212, 186, 0],
        [0, 290, 340, 125, 78, 235, 110, 203, 184, 426, 388, 220, 350, 453, 272, 119, 58, 447, 163, 175, 327, 365, 162, 413, 271, 231, 403, 383, 275, 295]
    ]

    pilsetas = ["Ventspils", "Valmiera", "Valka", "Tukums", "Talsi", "Sigulda",
                "Saldus", "Salaspils", "Riga", "Rezekne", "Preili", "Ogre",
                "Madone", "Ludza", "Limbaži", "Liepaja", "Kuldiga", "Kraslava",
                "Jurmala", "Jelgava", "Jekabpils", "Gulbene", "Dobele", "Daugavpils",
                "Cesis", "Bauska", "Balvi", "Aluksne", "Aizkraukle", "Ainaži"]
    
def mansCels(pilseta_no: str, pilseta_uz: str) -> dict:

    apskatitas = [False, False, False, False, False, False,
                  False, False, False, False, False, False,
                  False, False, False, False, False, False,
                  False, False, False, False, False, False,
                  False, False, False, False, False, False]
    isakaisNoSak = [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                    float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                    float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                    float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                    float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
    isakaisCels = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    N = len(apskatitas)

    if(pilseta_no and pilseta_uz in pilsetas):
        sakumPunkts = pilsetas.index(pilseta_no)
        beiguPunkts = pilsetas.index(pilseta_uz)
    else:
        return_dict = {
            "Error: ": "Dotā pilsēta nav pareizi uzrakstīta vai neeksistē attālumu masīvā"
        }
        return return_dict
    
    isakaisNoSak[sakumPunkts] = 0

    apskatesPunkts = sakumPunkts
    for reizes in range(0, N):
        for iPunkts in range(0, N):
            if not apskatitas[iPunkts]:
                if isakaisNoSak[iPunkts] > (attalumi[apskatesPunkts][iPunkts] + isakaisNoSak[apskatesPunkts]):
                    isakaisNoSak[iPunkts] = attalumi[apskatesPunkts][iPunkts] + isakaisNoSak[apskatesPunkts]
                    isakaisCels[iPunkts] = isakaisCels[apskatesPunkts].copy()
                    isakaisCels[iPunkts].append(apskatesPunkts)
        apskatitas[apskatesPunkts] = True
        
        minDist = float('inf')
        minIndex = -1
        for i in range(0, N):
            if (not apskatitas[i]) and isakaisNoSak[i] < minDist:
                minDist = isakaisNoSak[i]
                minIndex = i
        apskatesPunkts = minIndex

    isakaisCels[beiguPunkts].append(beiguPunkts)

    pilsetu_marsruts = []
    for city in isakaisCels[beiguPunkts]:
        pilsetu_marsruts.append(pilsetas[city])

    return_dict = {
        "Apraksts: ": f'Īsākā distance no {pilsetas[sakumPunkts]} līdz {pilsetas[beiguPunkts]} : {isakaisNoSak[beiguPunkts]} Km',
        "Pilsētu maršruts: ": pilsetu_marsruts
    }

    return return_dict

def iestatit_neparvaramus_attalumus(mas: list) -> list:
    for i in range(len(mas)):
        for x in range(len(mas[i])):
            if(mas[i][x] > 100):
                mas[i][x] = float('inf')
        
    return mas

print(mansCels("Ventspils", "Riga"))
attalumi = iestatit_neparvaramus_attalumus(attalumi)
print(mansCels("Ventspils", "Riga"))
