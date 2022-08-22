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
            <ogc:Literal>m_w_mir_strany_g_&lt;MI_STYLE&gt;Pen(1,2,10658435) Brush(2,12829635,16777215)&lt;/MI_STYLE&gt;</ogc:Literal>
          </ogc:PropertyIsEqualTo>
        </ogc:Filter>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#c3c3c3</CssParameter>
            </Fill>
          </PolygonSymbolizer>
        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">#a2a283</CssParameter>
            <CssParameter name="stroke-width">1</CssParameter>
          </Stroke>
        </LineSymbolizer>
</Rule>
</FeatureTypeStyle>
</UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
