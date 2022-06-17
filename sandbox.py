from pysld.style import StyleSld

# Simple style for polygon feature
simple_sld = StyleSld(style_name='polygonStyle', geom_type='polygon', fill_color='#ffffff', stroke_color='#333333')
simple_sld_style = simple_sld.generate_simple_style()
print(simple_sld_style)

