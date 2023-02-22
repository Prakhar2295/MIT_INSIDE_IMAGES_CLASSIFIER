from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

class mitinside:
    def __init__(self,filename):
        self.filename = filename

    def predictionmitinside(self):

        ##load model
        model = load_model("artifacts/model/model_at_Sun_Feb_19_21_19_18_2023_.h5")

        imagename = self.filename
        test_image = image.load_img(imagename,target_size =(224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        if result[0][0] == 1:
            prediction = "airport_inside"
            return [{"image": prediction}]
        elif result[0][1] == 1:
            prediction = "artstudio"
            return [{"image": prediction}]
        elif result[0][2] == 1:
            prediction = "auditorium"
            return [{"image": prediction}]
        elif result[0][3] == 1:
            prediction = "bakery"
            return [{"image": prediction}]
        elif result[0][4] == 1:
            prediction = "bar"
            return [{"image": prediction}]
        elif result[0][5] == 1:
            prediction = "bedroom"
            return [{"image": prediction}]
        elif result[0][6] == 1:
            prediction = "bookstore"
            return [{"image": prediction}]
        elif result[0][7] == 1:
            prediction = "bowling"
            return [{"image": prediction}]
        elif result[0][8] == 1:
            prediction = "buffet"
            return [{"image": prediction}]
        elif result[0][9] == 1:
            prediction = "casino"
            return [{"image": prediction}]
        elif result[0][10] == 1:
            prediction = "children_room"
            return [{"image": prediction}]
        elif result[0][11] == 1:
            prediction = "church_inside"
            return [{"image": prediction}]
        elif result[0][12] == 1:
            prediction = "classroom"
            return [{"image": prediction}]
        elif result[0][13] == 1:
            prediction = "cloister"
            return [{"image": prediction}]
        elif result[0][14] == 1:
            prediction = "closet"
            return [{"image": prediction}]
        elif result[0][15] == 1:
            prediction = "clothingstore"
            return [{"image": prediction}]
        elif result[0][16] == 1:
            prediction = "computerroom"
            return [{"image": prediction}]
        elif result[0][17] == 1:
            prediction = "concert_hall"
            return [{"image": prediction}]
        elif result[0][18] == 1:
            prediction = "corridor"
            return [{"image": prediction}]
        elif result[0][19] == 1:
            prediction = "deli"
            return [{"image": prediction}]
        elif result[0][20] == 1:
            prediction = "dentaloffice"
            return [{"image": prediction}]
        elif result[0][21] == 1:
            prediction = "dining_room"
            return [{"image": prediction}]
        elif result[0][22] == 1:
            prediction = "elevator"
            return [{"image": prediction}]
        elif result[0][23] == 1:
            prediction = "fastfood_restaurant"
            return [{"image": prediction}]
        elif result[0][24] == 1:
            prediction = "florist"
            return [{"image": prediction}]
        elif result[0][25] == 1:
            prediction = "gameroom"
            return [{"image": prediction}]
        elif result[0][26] == 1:
            prediction = "garage"
            return [{"image": prediction}]
        elif result[0][27] == 1:
            prediction = "greenhouse"
            return [{"image": prediction}]
        elif result[0][28] == 1:
            prediction = "grocerystore"
            return [{"image": prediction}]
        elif result[0][29] == 1:
            prediction = "gym"
            return [{"image": prediction}]
        elif result[0][30] == 1:
            prediction = "hairsalon"
            return [{"image": prediction}]
        elif result[0][31] == 1:
            prediction = "hospitalroom"
            return [{"image": prediction}]
        elif result[0][32] == 1:
            prediction = "inside_bus"
            return [{"image": prediction}]
        elif result[0][33] == 1:
            prediction = "inside_subway"
            return [{"image": prediction}]
        elif result[0][34] == 1:
            prediction = "jewelleryshop"
            return [{"image": prediction}]
        elif result[0][35] == 1:
            prediction = "kindergarden"
            return [{"image": prediction}]
        elif result[0][36] == 1:
            prediction = "kitchen"
            return [{"image": prediction}]
        elif result[0][37] == 1:
            prediction = "laboratorywet"
            return [{"image": prediction}]
        elif result[0][38] == 1:
            prediction = "laundromat"
            return [{"image": prediction}]
        elif result[0][39] == 1:
            prediction = "library"
            return [{"image": prediction}]
        elif result[0][40] == 1:
            prediction = "livingroom"
            return [{"image": prediction}]
        elif result[0][41] == 1:
            prediction = "lobby"
            return [{"image": prediction}]
        elif result[0][42] == 1:
            prediction = "locker_room"
            return [{"image": prediction}]
        elif result[0][43] == 1:
            prediction = "mall"
            return [{"image": prediction}]
        elif result[0][44] == 1:
            prediction = "meeting_room"
            return [{"image": prediction}]
        elif result[0][45] == 1:
            prediction = "movietheater"
            return [{"image": prediction}]
        elif result[0][46] == 1:
            prediction = "museum"
            return [{"image": prediction}]
        elif result[0][47] == 1:
            prediction = "nursery"
            return [{"image": prediction}]
        elif result[0][48] == 1:
            prediction = "office"
            return [{"image": prediction}]
        elif result[0][49] == 1:
            prediction = "operating_room"
            return [{"image": prediction}]
        elif result[0][50] == 1:
            prediction = "pantry"
            return [{"image": prediction}]
        elif result[0][51] == 1:
            prediction = "poolinside"
            return [{"image": prediction}]
        elif result[0][52] == 1:
            prediction = "prisoncell"
            return [{"image": prediction}]
        elif result[0][53] == 1:
            prediction = "restaurant"
            return [{"image": prediction}]
        elif result[0][54] == 1:
            prediction = "restaurant_kit"
            return [{"image": prediction}]
        elif result[0][55] == 1:
            prediction = "shoeshop"
            return [{"image": prediction}]
        elif result[0][56] == 1:
            prediction = "stairscase"
            return [{"image": prediction}]
        elif result[0][57] == 1:
            prediction = "studiomusic"
            return [{"image": prediction}]
        elif result[0][58] == 1:
            prediction = "subway"
            return [{"image": prediction}]
        elif result[0][59] == 1:
            prediction = "toystore"
            return [{"image": prediction}]
        elif result[0][60] == 1:
            prediction = "trainstation"
            return [{"image": prediction}]
        elif result[0][61] == 1:
            prediction = "tv_studio"
            return [{"image": prediction}]
        elif result[0][62] == 1:
            prediction = "videostore"
            return [{"image": prediction}]
        elif result[0][63] == 1:
            prediction = "waitingroom"
            return [{"image": prediction}]
        elif result[0][64] == 1:
            prediction = "warehouse"
            return [{"image": prediction}]
        else :
            prediction = "winecellar"
            return [{"image": prediction}]

output = mitinside("data/auditorium/01_gd_amphi_statues_1__1.jpg")
s= output.predictionmitinside()
print(s)        
                                    





        