from . import AbstractFilter


class WatermarkFilter(AbstractFilter):

    def __init__(self, image, left=None, right=None, top=None, bottom=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.image = image
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        image = json_object['image']
        left = json_object.get('left')
        right = json_object.get('right')
        top = json_object.get('top')
        bottom = json_object.get('bottom')
        watermark_filter = WatermarkFilter(
            image=image, left=left, right=right, top=top, bottom=bottom, id_=id_)
        return watermark_filter