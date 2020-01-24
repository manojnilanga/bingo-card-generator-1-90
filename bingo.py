from PIL import Image, ImageDraw, ImageFont
import random

if __name__ == '__main__':

    font = ImageFont.truetype("arial.ttf", 18)
    pages = 2

    for m in range(0,pages):
        bingopage=[]
        
        for i in range (0,6):
            height = 451
            width = 151
            image = Image.new(mode='L', size=(height, width), color=255)

            # Draw some lines
            draw = ImageDraw.Draw(image)
 
            y_start = 0
            y_end = image.height
            step_size = int(image.width / 9)

            for x in range(0, image.width, step_size):
                line = ((x, y_start), (x, y_end))
                draw.line(line, fill=128)

            x_start = 0
            x_end = image.width
            step_size = int(image.height / 3)

            for y in range(0, image.height, step_size):
                line = ((x_start, y), (x_end, y))
                draw.line(line, fill=128)

            del draw

            ran15 = random.sample(range(1, 90), 15)
            print(ran15)

            for j in range(0,3):
                ran5=ran15[j*5:j*5+5]
                ran5.append(-1)
                ran5.append(-1)
                ran5.append(-1)
                ran5.append(-1)
                random.shuffle(ran5)
                print(ran5)
                for k in range(0,9):
                    if(ran5[k]==-1):
                        continue
                    d =ImageDraw.Draw(image)
                    d.text((k*50+14,j*50+14),str(ran5[k]),font=font)

            bingopage.append(image)

        dst = Image.new(mode='L', size=(1050, 650), color=255)
        dst.paste(bingopage[0], (50, 50))
        dst.paste(bingopage[1], (550, 50))
        dst.paste(bingopage[2], (50, 250))
        dst.paste(bingopage[1], (550, 250))
        dst.paste(bingopage[0], (50, 450))
        dst.paste(bingopage[1], (550, 450))

        dst.save(str(m+1)+'.png')
    
    