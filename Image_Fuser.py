# function to alternate pixels of 4 images into one
# FYI - Takes a long time to complete
def imagefuse():
    from PIL import Image
    im1 = Image.open('IMG_20181106_153928 copy.jpg')
    pixelMap1 = im1.load()
    im2 = Image.open('IMG_20181106_153939 copy.jpg')
    pixelMap2 = im2.load()
    im3 = Image.open('IMG_20181106_154048 copy.jpg')
    pixelMap3 = im3.load()
    im4 = Image.open('IMG_20181106_154140 copy.jpg')
    pixelMap4 = im4.load()
    imga = Image.new(im2.mode, (2 * min(im3.size[0], im4.size[0], im1.size[0], im2.size[0]),
                                2 * min(im3.size[1], im4.size[1], im1.size[1], im2.size[1])))
    pixelsNew = imga.load()
    for i in range(imga.size[0]):
        for j in range(imga.size[1]):
            ma = min(im3.size[0], im4.size[0], im1.size[0], im2.size[0])
            mb = min(im3.size[1], im4.size[1], im1.size[1], im2.size[1])
            if j < mb:
                if i < ma:
                    pixelsNew[i, j] = pixelMap2[i, j]
                else:
                    pixelsNew[i, j] = pixelMap1[i - ma, j]
            else:
                if i < ma:
                    pixelsNew[i, j] = pixelMap3[i, j - mb]
                else:
                    pixelsNew[i, j] = pixelMap4[i - ma, j - mb]
    imga.show()


imagefuse()