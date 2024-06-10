class tower:
    def __init__(self, x, y, brightness):
        self.x = x
        self.y = y
        self.brightness = brightness 
    
def find_rest_spots(current_stop, previous_stop, max_distance, rests_quantity, towers, rest_spots):
    rest_val = ""

    if (previous_stop != None):
        if (towers[current_stop].brightness > towers[previous_stop].brightness):
            rests_quantity += 1
            rest_spots[-1] += "*"
    
    if (current_stop == len(towers) - 1):
        return rests_quantity
    
    max_less_than_current_brightness = 0
    max_less_than_current_brightness_index = 0
    max_brightness = 0
    max_brightness_index = 0

    for i in range(max_distance):
        if (current_stop + i + 1 >= len(towers)):
            break

        if (towers[current_stop + i + 1].brightness < towers[current_stop].brightness):
            if (towers[current_stop + i + 1].brightness > max_less_than_current_brightness):
                max_less_than_current_brightness = towers[current_stop + i + 1].brightness
                max_less_than_current_brightness_index = current_stop + i + 1
        
        if (towers[current_stop + i + 1].brightness > max_brightness):
            max_brightness = towers[current_stop + i + 1].brightness
            max_brightness_index = current_stop + i + 1

    if (max_less_than_current_brightness > 0):
        index = max_less_than_current_brightness_index
    else:
        index = max_brightness_index
    
    rest_spots.append(str(index))
    return find_rest_spots(index, current_stop, max_distance, rests_quantity, towers, rest_spots)