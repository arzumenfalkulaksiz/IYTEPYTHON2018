text = """As described previously, the captured views provide us two important data: 1) silhouettes of the object from different views, which define the visual hull of the object, and 2) ray-ray correspondences before and after rays intersecting with the object, which correlate to light refraction paths and surface geometry details."""
x=text.replace(",","")
y=x.replace(":","")
z=y.replace("1)","")
t=z.replace("2)","")
print(t)