# position = 289326

def taxicab(position):
    layer = 1
    size = 1

    while size <= position:
        layer += 2
        size = layer**2

    return (layer - ((size - position) % layer) -1)

result = taxicab(32)

print(result)