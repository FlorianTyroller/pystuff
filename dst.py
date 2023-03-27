def get_correct_channel(axis, coding_pin, connector_pin):
    if axis == ax_from_dir(dir=coding_pin):
        return "alpha"
    elif axis == ax_from_dir(dir=connector_pin):
        return "beta"
    else:
        return "gamma"

def ax_from_dir(dir):
    if dir in ["front", "back"]:
        return "X"
    elif dir in ["left", "right"]:
        return "Y"
    elif dir in ["up", "down"]:
        return "Z"

# example usage
print(get_correct_channel("X", "back", "right"), " == alpha, input: X, back, right")
print(get_correct_channel("Z", "back", "right"), " == gamma, input: Z, back, right")

print(get_correct_channel("Y", "front", "left"), " == beta, input: Y, front, left")
print(get_correct_channel("Z", "front", "left"), " == gamma, input: Z, front, left")

print(get_correct_channel("Z", "front", "down"), " == beta, input: Z, front, down")
print(get_correct_channel("Y", "front", "down"), " == gamma, input: Y, front, down")

print(get_correct_channel("Y", "left", "down"), " == alpha, input: Y, left, down")
print(get_correct_channel("X", "left", "down"), " == gamma, input: X, left, down")

print(get_correct_channel("X", "front", "down"), " == alpha, input: X, front, down")
print(get_correct_channel("Y", "front", "down"), " == gamma, input: Y, front, down")

print(get_correct_channel("Z", "down", "front"), " == alpha, input: Z, down, front")
print(get_correct_channel("Y", "down", "front"), " == gamma, input: Y, down, front")

print(get_correct_channel("Z", "down", "left"), " == alpha, input: Z, down, left")
print(get_correct_channel("X", "down", "left"), " == gamma, input: X, down, left")

print(get_correct_channel("X", "left", "front"), " == beta, input: X, left, front")
print(get_correct_channel("X", "front", "left"), " == alpha, input: X, front, left")


print(get_correct_channel("Y", "left", "front"), " == alpha, input: Y, left, front")
print(get_correct_channel("Y", "front", "left"), " == beta, input: Y, front, left")
