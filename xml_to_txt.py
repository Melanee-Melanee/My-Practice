import os
import xml.etree.ElementTree as ET

def convert_xml_to_txt(xml_dir, txt_dir):
    if not os.path.exists(txt_dir):
        os.makedirs(txt_dir)

    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith('.xml'):
            tree = ET.parse(os.path.join(xml_dir, xml_file))
            root = tree.getroot()

            txt_file = os.path.join(txt_dir, xml_file.replace('.xml', '.txt'))
            with open(txt_file, 'w') as f:
                for obj in root.findall('object'):
                    bbox = obj.find('bndbox')
                    text = obj.find('name').text
                    x_min = bbox.find('xmin').text
                    y_min = bbox.find('ymin').text
                    x_max = bbox.find('xmax').text
                    y_max = bbox.find('ymax').text
                    f.write(f"{x_min} {y_min} {x_max} {y_max} {text}\n")

# Example usage
xml_dir = '/home/melanee/Downloads/xml_annotations'
txt_dir = '/home/melanee/Downloads/txt_annotations'

convert_xml_to_txt(xml_dir, txt_dir)
