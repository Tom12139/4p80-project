# new image struct
# label+1024*R+1024*G+1024*B
# 1024*3+1=3073

class ImageStruct:
    def __init__(self, label, r, g, b):
        self.label = label
        self.r = r
        self.g = g
        self.b = b

    def to_value(self):
        # 计算结构的值：label + 1024 * R + 1024 * G + 1024 * B
        return self.label + 1024 * self.r + 1024 * self.g + 1024 * self.b

# 示例用法
image = ImageStruct(label=1, r=255, g=255, b=255)
value = image.to_value()
print(value)  # 输出结构的值


