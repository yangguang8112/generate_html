from PIL import ImageFont, ImageDraw, Image
import os

def get_max_size(image_list):
    max_size = (0, 0)
    for image in image_list:
        img = Image.open(image)
        if img.size > max_size:
            max_size = img.size
    return max_size

def get_size(image_list):
    image_size = []
    for image in image_list:
        img = Image.open(image)
        image_size.append(img.size)
    return image_size

def addText(pil_obj, text, pos=(10,10)):
    font = ImageFont.truetype('./fonts/DejaVuSans-Bold.ttf', 64)
    draw = ImageDraw.Draw(pil_obj)
    draw.text(pos, text, fill= (0, 0, 0), font=font)
    return


LOWER_CASE = 'abcdefghijklmnopqrstuvwxyz'
SAVE_QUALITY = 50

def concat_images(image_list, res_file, COL, ROW):
    UNIT_WIDTH_SIZE, UNIT_HEIGHT_SIZE = get_max_size(image_list)
    image_objs = []
    for index in range(COL*ROW):
        img_obj = Image.open(image_list[index])
        addText(img_obj, LOWER_CASE[index])
        image_objs.append(img_obj)
    target = Image.new('RGBA', (UNIT_WIDTH_SIZE * COL, UNIT_HEIGHT_SIZE * ROW)) #创建成品图的画布
    #第一个参数RGB表示创建RGB彩色图，第二个参数传入元组指定图片大小，第三个参数可指定颜色，默认为黑色
    for row in range(ROW):
        for col in range(COL):
            #对图片进行逐行拼接
            #paste方法第一个参数指定需要拼接的图片，第二个参数为二元元组（指定复制位置的左上角坐标）
            #或四元元组（指定复制位置的左上角和右下角坐标）
            target.paste(image_objs[COL*row+col], (0 + UNIT_WIDTH_SIZE*col, 0 + UNIT_HEIGHT_SIZE*row))
    # target.save(res_file, quality=SAVE_QUALITY) #成品图保存
    target.save(res_file) #成品图保存



def merge_fig1(fig_file_list, out_path):
    # fig_file_list = [
    # 'img/figure1_QualityControl/A.png',
    # 'img/figure1_QualityControl/B.png',
    # 'img/figure1_QualityControl/C.filter.png',
    # 'img/figure1_QualityControl/C.nofilter.png',
    # 'img/figure1_QualityControl/D.png']
    a, b, c1, c2, d = fig_file_list
    fig_objs = []
    for fig_file in fig_file_list:
        fig_objs.append(Image.open(fig_file))
    a, b, c1, c2, d = fig_objs

    # size = [(1950, 1560), (1950, 1560), (2340, 1560), (2340, 1560), (480, 480)]
    a_size, b_size, c1_size, c2_size, d_size = get_size(fig_file_list)

    c1_size = (a_size[0], int(c1_size[1] * a_size[0] / c1_size[0]))
    c2_size = (a_size[0], int(c2_size[1] * a_size[0] / c2_size[0]))
    # print(c1_size, c2_size)
    c1 = c1.resize(c1_size, Image.ANTIALIAS)
    c2 = c2.resize(c2_size, Image.ANTIALIAS)

    d_size = (d_size[0] * 3, d_size[1] * 3)
    d = d.resize(d_size, Image.ANTIALIAS)

    addText(a, 'a')
    addText(b, 'b')
    addText(c1, 'c')
    addText(d, 'd')


    # ROW, COL = 2, 2
    # UNIT_WIDTH_SIZE, UNIT_HEIGHT_SIZE = a_size
    target = Image.new('RGBA', (a_size[0] + b_size[0], a_size[1] + c1_size[1] + c2_size[1]))

    target.paste(a, (0, 0))
    target.paste(b, (a_size[0], 0))
    target.paste(c1, (60, a_size[1]))
    target.paste(c2, (60, a_size[1]+c1_size[1]))
    target.paste(d, (a_size[0]+350, a_size[1] + 350))

    target.save(out_path + "/fig1.png")

def merge_fig2(fig_file_list, out_path):
    concat_images(fig_file_list, out_path + "/fig2.png", 2, 2)

def merge_fig3(fig_file_list, out_path):
    # fig_file_list = [
    # "img/figure3_scRNA-seq/A.png",
    # "img/figure3_scRNA-seq/B.png",
    # "img/figure3_scRNA-seq/C-double.png",
    # "img/figure3_scRNA-seq/D.png",]
    a, b, c, d = fig_file_list

    fig_objs = []
    for fig_file in fig_file_list:
        fig_objs.append(Image.open(fig_file))

    a, b, c, d = fig_objs

    # size [(1950, 1560), (1950, 1560), (3120, 1170), (3900, 1560)]
    a_size, b_size, c_size, d_size = get_size(fig_file_list)

    c_size = (a_size[0] + b_size[0], int(c_size[1] * (a_size[0] + b_size[0]) / c_size[0]))
    c = c.resize(c_size, Image.ANTIALIAS)

    addText(a, 'a')
    addText(b, 'b')
    addText(c, 'c')
    addText(c, 'd', (1560, 10))
    addText(d, 'e')

    WIDTH = max(a_size[0]+b_size[0], c_size[0], d_size[0])
    HEIGHT = max(a_size[1], b_size[1]) + c_size[1] + d_size[1]
    # target = Image.new('RGBA', (d_size[0], a_size[1] + c_size[1] + d_size[1]))
    target = Image.new('RGBA', (WIDTH, HEIGHT))

    target.paste(a, (0, 0))
    target.paste(b, (a_size[0], 0))
    target.paste(c, (0, a_size[1]))
    target.paste(d, (0, a_size[1] + c_size[1]))

    target.save(out_path + "/fig3.png")

def merge_by_width(fig1, fig2):
    # 输入图片size元组
    if fig1[0] > fig2[0]:
        big_fig = fig1
        small_fig = fig2
        flag = 1
    else:
        big_fig = fig2
        small_fig = fig1
        flag = 0
    resize = (big_fig[0], int(small_fig[1] * big_fig[0] / small_fig[0]))
    return resize, flag

def merge_by_height(fig1, fig2):
    if fig1[1] > fig2[1]:
        big_fig = fig1
        small_fig = fig2
        flag = 1
    else:
        big_fig = fig2
        small_fig = fig1
        flag = 0
    resize = (int(small_fig[0] * big_fig[1] / small_fig[1]), big_fig[1])
    return resize, flag

def merge_fig3_new_new(fig_file_list, out_path):

    fig_objs = []
    for fig_file in fig_file_list:
        fig_objs.append(Image.open(fig_file))
    
    a, b, c, d = fig_objs

    a_size, b_size, c_size, d_size = get_size(fig_file_list)
    resize, flag = merge_by_width(a_size, d_size)
    # print(a_size, d_size)
    # print(resize, flag)
    if flag == 1:
        a_size = resize
    else:
        d_size = resize
    a_and_d_size = (a_size[0], a_size[1]+d_size[1])
    b_size = (int(b_size[0] * a_and_d_size[1] / b_size[1]), a_and_d_size[1])
    a_d_b_size = (a_size[0]+b_size[0], a_and_d_size[1])
    # tag e
    c_resize = (a_d_b_size[0], int(c_size[1] * a_d_b_size[0] / c_size[0]))
    e_tag_pos = (int(1843 * c_resize[0] / c_size[0]), int(60 * c_resize[1] / c_size[1]))
    c_size = c_resize
    a = a.resize(a_size, Image.ANTIALIAS)
    b = b.resize(b_size, Image.ANTIALIAS)
    c = c.resize(c_size, Image.ANTIALIAS)
    d = d.resize(d_size, Image.ANTIALIAS)
    addText(a, 'a')
    addText(b, 'b')
    addText(d, 'c')
    addText(c, 'd')
    addText(c, 'e', e_tag_pos)
    WIDTH = a_size[0] + b_size[0]
    HEIGHT = a_size[1] + d_size[1] + c_size[1]
    target = Image.new('RGBA', (WIDTH, HEIGHT))

    target.paste(a, (0, 0))
    target.paste(b, (a_size[0], 0))

    target.paste(d, (0, a_size[1]))
    target.paste(c, (0, max(a_size[1]+d_size[1], b_size[1])))

    target.save(out_path + "/fig3.png")



def merge_fig3_new(fig_file_list, out_path):
    # fig_file_list = [
    # "img/figure3_scRNA-seq/A.png",
    # "img/figure3_scRNA-seq/B.png",
    # "img/figure3_scRNA-seq/C-double.png",
    # "img/figure3_scRNA-seq/D.png",]
    a, b, c, d = fig_file_list

    fig_objs = []
    for fig_file in fig_file_list:
        fig_objs.append(Image.open(fig_file))

    a, b, c, d = fig_objs

    # size [(2340, 1560), (1560, 2340), (4680, 2340), (2340, 1560)]
    a_size, b_size, c_size, d_size = get_size(fig_file_list)

    # c_size = (a_size[0] + b_size[0], int(c_size[1] * (a_size[0] + b_size[0]) / c_size[0]))
    # c = c.resize(c_size, Image.ANTIALIAS)
    b_size = (int(b_size[0] * ((a_size[1] + d_size[1])/b_size[1])) , a_size[1] + d_size[1])
    b = b.resize(b_size, Image.ANTIALIAS)

    addText(a, 'a')
    addText(b, 'b')
    addText(d, 'c')
    addText(c, 'd')
    addText(c, 'e', (1843, 60))

    WIDTH = max(a_size[0]+b_size[0], d_size[0]+b_size[0], c_size[0])
    HEIGHT = max(a_size[1]+d_size[1], b_size[1]) + c_size[1]
    # target = Image.new('RGBA', (d_size[0], a_size[1] + c_size[1] + d_size[1]))
    target = Image.new('RGBA', (WIDTH, HEIGHT))

    target.paste(a, (0, 0))
    target.paste(b, (a_size[0], 0))

    target.paste(d, (0, a_size[1]))
    target.paste(c, (0, max(a_size[1]+d_size[1], b_size[1])))

    target.save(out_path + "/fig3.png")

def merge_fig4(fig_file_list, out_path):
    # fig_file_list = [
    # "img/figure4_FunctionalAnalysis/A.png",
    # "img/figure4_FunctionalAnalysis/B.png",
    # "img/figure4_FunctionalAnalysis/C.png",
    # "img/figure4_FunctionalAnalysis/D.png",]

    a, b, c, d = fig_file_list

    fig_objs = []
    for fig_file in fig_file_list:
        fig_objs.append(Image.open(fig_file))

    a, b, c, d = fig_objs

    # [(2340, 1560), (3120, 2340), (2340, 1950), (2340, 1950)]
    a_size, b_size, c_size, d_size = get_size(fig_file_list)

    addText(a, 'a')
    addText(b, 'b')
    addText(c, 'c')
    addText(d, 'd')

    target = Image.new('RGBA', (b_size[0] + d_size[0], b_size[1] + c_size[1]))

    target.paste(a, (0, 0))
    target.paste(b, (0, c_size[1]))
    target.paste(c, (b_size[0], 0))
    target.paste(d, (b_size[0], c_size[1]))

    target.save(out_path + "/fig4.png")

def merge_fig5(fig_file_list, out_path):
    # fig_file_list = [
    # "img/figure5_pseudotime/B.png",
    # "img/figure5_pseudotime/A.png",
    # "img/figure5_pseudotime/C.png",
    # "img/figure5_pseudotime/D.png",]
    a, b, c, d = fig_file_list

    fig_objs = []
    for fig_file in fig_file_list:
        fig_objs.append(Image.open(fig_file))

    a, b, c, d = fig_objs

    # [(2340, 1560), (2340, 1560), (2340, 3120), (2340, 2340)]
    a_size, b_size, c_size, d_size = get_size(fig_file_list)

    d_size = (int(d_size[0] * c_size[1] / d_size[1]), c_size[1])
    d = d.resize(d_size, Image.ANTIALIAS)

    addText(a, 'a')
    addText(b, 'b')
    addText(c, 'c')
    addText(d, 'd')

    target = Image.new('RGBA', (c_size[0] + d_size[0], b_size[1] + c_size[1]))

    target.paste(a, (0, 0))
    target.paste(b, (a_size[0] + 400, 0))
    target.paste(c, (0, a_size[1]))
    target.paste(d, (c_size[0], a_size[1]))

    target.save(out_path + "/fig5.png")

def merge_fig6(fig_file_list, out_path):
    concat_images(fig_file_list, out_path + "/fig6.png", 2, 1)


if __name__ == '__main__':
    # debug
    fig_file_list = [
        "final_cluster_umap.png",
        "All.cluster0_top12_markerUmap.png",
        "dotplot_and_barplot.png",
        "All.cluster0_top12_markerVln.png"
    ]
    merge_fig3_new_new(fig_file_list, "./")