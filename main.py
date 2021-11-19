from strgen import StringGenerator

print(StringGenerator("[\l\d]{64}").render_list(1,unique=True))
