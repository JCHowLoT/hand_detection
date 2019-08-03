import xml.dom.minidom

def load_xml(path):
    DOMTree = xml.dom.minidom.parse(path)
    collection = DOMTree.documentElement
    objects=collection.getElementsByTagName("object")
    objects_num=len(objects)
    # print(objects_num)
    for object in objects:
        bndbox = object.getElementsByTagName('bndbox')[0]
        xmin = bndbox.getElementsByTagName('xmin')[0]
        xmin_data = xmin.childNodes[0].data
        ymin = bndbox.getElementsByTagName('ymin')[0]
        ymin_data = ymin.childNodes[0].data
        xmax = bndbox.getElementsByTagName('xmax')[0]
        xmax_data = xmax.childNodes[0].data
        ymax = bndbox.getElementsByTagName('ymax')[0]
        ymax_data = ymax.childNodes[0].data

    return  [int(xmin_data), int(ymin_data), int(xmax_data), int(ymax_data)]

# a = load_xml('/home/j/dataset/01_hand_detaction/xml_r1000_n357/depth_0.xml')
# print(a)