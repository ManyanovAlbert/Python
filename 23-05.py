from PIL import Image, ImageDraw

def board(num, size):
    img = Image.new('RGB', (num * size, num * size), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)


    for i in range(num):
        for j in range(num):

            if (i + j) % 2 == 0:
                color = (0, 0, 0)  # Чёрный
            else:
                color = (255, 255, 255)  # Белый

            # Draw the cell
            draw.rectangle([i * size, j * size, (i + 1) * size, (j + 1) * size], fill=color)


    img.save('checkerboard.png')


board(8, 50)