HEIGHT = 10
WEIGHT = 20
STEPS_COUNT = 30
ACTIVITY_TIME = 10


def stride_length():
    return HEIGHT / 4 + 0.37


def total_distance(length):
    return STEPS_COUNT * length


def walking_speed(distance):
    return distance * ACTIVITY_TIME


def burned_calories(speed):
    return 0.035 * WEIGHT + (speed ** 2 / HEIGHT) * 0.029 * WEIGHT


total_dist = total_distance(stride_length())
total_cal = burned_calories(walking_speed(total_dist))

print('Total walking distance :', total_dist, ', total burned calories: ', total_cal)
