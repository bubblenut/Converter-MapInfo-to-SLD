<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor version="1.0.0"
                       xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"
                       xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
                       xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <NamedLayer>
    <Name>All Layers</Name>
    <UserStyle>
      <Title>Styles for TestoreWGS</Title>
<FeatureTypeStyle>
<Rule>

        <ogc:Filter>
          <ogc:PropertyIsEqualTo>
            <ogc:PropertyName>g_style</ogc:PropertyName>
            <ogc:Literal>m_w_mir_okean_g_&lt;MI_STYLE&gt;Pen(1,2,13027829) Brush(2,12179455,16777215)&lt;/MI_STYLE&gt;</ogc:Literal>
          </ogc:PropertyIsEqualTo>
        </ogc:Filter>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#b9d7ff</CssParameter>
            </Fill>
          </PolygonSymbolizer>
        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">#c6c9f5</CssParameter>
            <CssParameter name="stroke-width">1</CssParameter>
          </Stroke>
        </LineSymbolizer>
</Rule>
</FeatureTypeStyle>
</UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
