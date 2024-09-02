#AI solving 2x2 rubic
#Q learning
import numpy as np
#budowanie środowiska

# Defined all walls
face_1 = np.array(np.zeros((2,2)))
face_2 = np.array(np.zeros((2,2)))
face_3 = np.array(np.zeros((2,2)))
face_4 = np.array(np.zeros((2,2)))
face_5 = np.array(np.zeros((2,2)))
face_6 = np.array(np.zeros((2,2)))

#Mapping
colors_to_numbers = {
    'W': 0, # White
    'Y': 1, # Yellow
    'R': 2, # Red
    'G': 3, # Green
    'B': 4, # Blue
    'O': 5  # Orage
}

numbers_to_colors = {color: number for number, color in colors_to_numbers.items()}


#stany

#nagrody