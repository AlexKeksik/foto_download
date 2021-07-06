from simple_image_download import simple_image_download as simp
response = simp.simple_image_download
print(f"Напишите какие фото искать:")
str = str(input())
print(f"Сколько скачивать изображений?:")
all = int(input())

response().download(str, all)
