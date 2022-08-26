styleHeading = '''<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor version="1.0.0"
                       xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"
                       xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
                       xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <NamedLayer>
    <Name>_STYLE_</Name>
    <UserStyle>
      <Title>_STYLE_</Title>'''


styleFooting = '''</UserStyle>
</NamedLayer>
</StyledLayerDescriptor>'''


filterHeading = '''        <ogc:Filter>
          <ogc:PropertyIsEqualTo>
            <ogc:PropertyName>g_style</ogc:PropertyName>
            <ogc:Literal>'''

filterFooting = '''</ogc:Literal>
          </ogc:PropertyIsEqualTo>
        </ogc:Filter>\n'''


penDict = {0: ['''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',
               'color',
               '''</CssParameter>
            <CssParameter name="stroke-width">''',
               'width',
               '''</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
            2: ['''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',
               'color',
               '''</CssParameter>
            <CssParameter name="stroke-width">''',
               'width',
               '''</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           3: ['''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',
               'color',
               '''</CssParameter>
            <CssParameter name="stroke-width">''',
               'width',
               '''</CssParameter>
            <CssParameter name="stroke-dasharray">1 2</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           4: ['''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',
               'color',
               '''</CssParameter>
            <CssParameter name="stroke-width">''',
               'width',
               '''</CssParameter>
            <CssParameter name="stroke-dasharray">2 2</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           5: ['''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',
               'color',
               '''</CssParameter>
            <CssParameter name="stroke-width">''',
               'width',
               '''</CssParameter>
            <CssParameter name="stroke-dasharray">4 2</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           6: ['''        <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
               'color',
               '''</CssParameter>
            <CssParameter name="stroke-width">''',
               'width',
               '''</CssParameter>
            <CssParameter name="stroke-dasharray">8 2</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           7: ['''        <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
               'color',
               '''</CssParameter>
            <CssParameter name="stroke-width">''',
               'width',
               '''</CssParameter>
            <CssParameter name="stroke-dasharray">16 3</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           8: ['''        <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
               'color',
               '''</CssParameter>
            <CssParameter name="stroke-width">''',
               'width',
               '''</CssParameter>
            <CssParameter name="stroke-dasharray">31 8</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           9: ['''        <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
               'color',
               '''</CssParameter>
            <CssParameter name="stroke-width">''',
               'width',
               '''</CssParameter>
            <CssParameter name="stroke-dasharray">5 5</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           10: ['''        <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
            <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
            <CssParameter name="stroke-dasharray">1 7</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           11: ['''        <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
            <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
            <CssParameter name="stroke-dasharray">4 8</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           12: ['''        <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
            <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
            <CssParameter name="stroke-dasharray">8 8</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           13: ['''        <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
            <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
            <CssParameter name="stroke-dasharray">16 16</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           14: ['''        <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
            <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
            <CssParameter name="stroke-dasharray">11 5 1 5</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           15: ['''        <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
            <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
            <CssParameter name="stroke-dasharray">17 3 1 3</CssParameter>
          </Stroke>
        </LineSymbolizer>\n'''],
           16: ['''        <LineSymbolizer>
<Stroke>
  <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
             <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
             <CssParameter name="stroke-dasharray">18 3 4 3</CssParameter>
           </Stroke>
         </LineSymbolizer>\n'''],
           17: ['''        <LineSymbolizer>
<Stroke>
  <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
             <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
             <CssParameter name="stroke-dasharray">32 12 6 12</CssParameter>
           </Stroke>
         </LineSymbolizer>\n'''],
           18: ['''        <LineSymbolizer>
<Stroke>
  <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
             <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
             <CssParameter name="stroke-dasharray">32 6 4 6 4 6</CssParameter>
           </Stroke>
         </LineSymbolizer>\n'''],
           19: ['''        <LineSymbolizer>
<Stroke>
  <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
             <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
             <CssParameter name="stroke-dasharray">32 6 4 6 4 6 4 6</CssParameter>
           </Stroke>
         </LineSymbolizer>\n'''],
           20: ['''        <LineSymbolizer>
<Stroke>
  <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
             <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
             <CssParameter name="stroke-dasharray">11 5 1 5 1 5</CssParameter>
           </Stroke>
         </LineSymbolizer>\n'''],
           21: ['''        <LineSymbolizer>
<Stroke>
  <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
             <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
             <CssParameter name="stroke-dasharray">20 4 1 4 1 4</CssParameter>
           </Stroke>
         </LineSymbolizer>\n'''],
           22: ['''        <LineSymbolizer>
<Stroke>
  <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
             <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
             <CssParameter name="stroke-dasharray">20 4 1 4 1 4 1 4</CssParameter>
           </Stroke>
         </LineSymbolizer>\n'''],
           23: ['''        <LineSymbolizer>
<Stroke>
  <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
             <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
             <CssParameter name="stroke-dasharray">6 2 1 2</CssParameter>
           </Stroke>
         </LineSymbolizer>\n'''
                ],
           24: ['''        <LineSymbolizer>
<Stroke>
  <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
             <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
             <CssParameter name="stroke-dasharray">6 2 1 2 1 2</CssParameter>
           </Stroke>
         </LineSymbolizer>\n'''],
           25: ['''        <LineSymbolizer>
<Stroke>
  <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
             <CssParameter name="stroke-width">''',
                'width',
                '''</CssParameter>
             <CssParameter name="stroke-dasharray">10 2 1 2 4 2 1 2</CssParameter>
           </Stroke>
         </LineSymbolizer>\n'''],
           26: ['''          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#66</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#67</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           27: ['''          <LineSymbolizer>
  <Stroke>
    <GraphicStroke>
      <Graphic>
        <Mark>
          <WellKnownName>ttf://Line_Styles#66</WellKnownName>
          <Fill>
            <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#68</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           28: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#66</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#69</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           29: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#66</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#70</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           32: ['''          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#71</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           34: ['''          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#73</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           37: ['''          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#74</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           39: ['''          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#75</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           42: ['''          <LineSymbolizer>
  <Stroke>
    <GraphicStroke>
      <Graphic>
        <Mark>
          <WellKnownName>ttf://Line_Styles#77</WellKnownName>
          <Fill>
            <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           44: ['''          <LineSymbolizer>
  <Stroke>
    <GraphicStroke>
      <Graphic>
        <Mark>
          <WellKnownName>ttf://Line_Styles#79</WellKnownName>
          <Fill>
            <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           46: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#80</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           45: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#78</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           48: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#66</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n''',
        '''       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#81</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           49: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#66</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#82</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           51: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#66</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#84</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           52: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#85</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           53: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#86</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           54: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#43</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#87</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           55: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#43</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#88</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           57: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#87</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           59: ['''          <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
    <CssParameter name="stroke-width">2</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
           '''        <PointSymbolizer>
  <Geometry>
    <ogc:Function name="endPoint">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Geometry>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#76</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',
           'color',
           '''</CssParameter>
      </Fill>
      <Stroke>
        <CssParameter name="stroke">''',
           'color',
           '''</CssParameter>
      </Stroke>
    </Mark>
    <Rotation>
      <ogc:Function name="endAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>\n'''],
           60: ['''          <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
    <CssParameter name="stroke-width">2</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
           '''<PointSymbolizer>
  <Geometry>
    <ogc:Function name="startPoint">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Geometry>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#89</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',
           'color',
           '''</CssParameter>
      </Fill>
      <Stroke>
        <CssParameter name="stroke">''',
           'color',
           '''</CssParameter>
      </Stroke>
    </Mark>
    <Rotation>
      <ogc:Function name="startAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>\n'''],
           61: ['''          <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
    <CssParameter name="stroke-width">2</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
           '''<PointSymbolizer>
  <Geometry>
    <ogc:Function name="startPoint">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Geometry>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#89</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',
           'color',
           '''</CssParameter>
      </Fill>
      <Stroke>
        <CssParameter name="stroke">''',
           'color',
           '''</CssParameter>
      </Stroke>
    </Mark>
    <Rotation>
      <ogc:Function name="startAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>\n''',
           '''<PointSymbolizer>
  <Geometry>
    <ogc:Function name="endPoint">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Geometry>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#76</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',
           'color',
           '''</CssParameter>
      </Fill>
      <Stroke>
        <CssParameter name="stroke">''',
           'color',
           '''</CssParameter>
      </Stroke>
    </Mark>
    <Rotation>
      <ogc:Function name="endAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>\n'''],
           62: ['''          <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
    <CssParameter name="stroke-width">2</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
           '''<PointSymbolizer>
  <Geometry>
    <ogc:Function name="startPoint">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Geometry>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#90</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',
           'color',
           '''</CssParameter>
      </Fill>
      <Stroke>
        <CssParameter name="stroke">''',
           'color',
           '''</CssParameter>
      </Stroke>
    </Mark>
    <Rotation>
      <ogc:Function name="startAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>\n'''],
           63: ['''          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#62</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',

                'color',

                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n''',

                '''          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#63</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',

                '#ffffff',

                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           66: ['''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',

                'color',

                '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
            <CssParameter name="stroke-dashoffset">10</CssParameter>
          </Stroke>
        </LineSymbolizer>\n''',

                '''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',

                'color',

                '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
          </Stroke>
        </LineSymbolizer>\n''',

                '''         <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',
                'color',

            '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
            <CssParameter name="stroke-dashoffset">10</CssParameter>
          </Stroke>
        </LineSymbolizer>\n''',

                '''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',

                'color',

                '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
          </Stroke>
        </LineSymbolizer>\n''',

                '''        <LineSymbolizer>
          <Stroke>
          <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
          <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
          </Stroke>
          <PerpendicularOffset>5</PerpendicularOffset>
        </LineSymbolizer>\n''',

                '''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',

                'color',

                '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
          </Stroke>
          <PerpendicularOffset>-5</PerpendicularOffset>
        </LineSymbolizer>\n''',

           '''<PointSymbolizer>
  <Geometry>
    <ogc:Function name="startPoint">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Geometry>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#93</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',

           'color',

           '''</CssParameter>
      </Fill>
      <Stroke>
        <CssParameter name="stroke">''',

           'color',

           '''</CssParameter>
      </Stroke>
    </Mark>
    <Rotation>
      <ogc:Function name="startAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>\n''',

           '''<PointSymbolizer>
  <Geometry>
    <ogc:Function name="endPoint">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Geometry>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#93</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',

           'color',

           '''</CssParameter>
      </Fill>
      <Stroke>
        <CssParameter name="stroke">''',

           'color',

           '''</CssParameter>
      </Stroke>
    </Mark>
    <Rotation>
      <ogc:Function name="endAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>\n'''],
    65: ['''          <LineSymbolizer>
                       <Stroke>
                         <GraphicStroke>
                           <Graphic>
                             <Mark>
                               <WellKnownName>ttf://Line_Styles#94</WellKnownName>
                               <Fill>
                                 <CssParameter name="fill">''',

         '#000000',

         '''</CssParameter>
             </Fill>
           </Mark>
         </Graphic>
       </GraphicStroke>
     </Stroke>
   </LineSymbolizer>\n''',

         '''          <LineSymbolizer>
     <Stroke>
       <GraphicStroke>
         <Graphic>
           <Mark>
             <WellKnownName>ttf://Line_Styles#95</WellKnownName>
             <Fill>
               <CssParameter name="fill">''',

         'color',

         '''</CssParameter>
             </Fill>
           </Mark>
         </Graphic>
       </GraphicStroke>
     </Stroke>
   </LineSymbolizer>\n''',

         '''<PointSymbolizer>
<Geometry>
  <ogc:Function name="startPoint">
    <ogc:PropertyName>pg_geom</ogc:PropertyName>
  </ogc:Function>
</Geometry>
<Graphic>
  <Mark>
    <WellKnownName>ttf://Line_Styles#96</WellKnownName>
    <Fill>
      <CssParameter name="fill">''',

         '#000000',

         '''</CssParameter>
    </Fill>
  </Mark>
  <Rotation>
    <ogc:Function name="startAngle">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Rotation>
</Graphic>
</PointSymbolizer>\n''',

         '''<PointSymbolizer>
<Geometry>
  <ogc:Function name="endPoint">
    <ogc:PropertyName>pg_geom</ogc:PropertyName>
  </ogc:Function>
</Geometry>
<Graphic>
  <Mark>
    <WellKnownName>ttf://Line_Styles#96</WellKnownName>
    <Fill>
      <CssParameter name="fill">''',

         '#000000',

         '''</CssParameter>
    </Fill>
  </Mark>
  <Rotation>
    <ogc:Function name="endAngle">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Rotation>
</Graphic>
</PointSymbolizer>\n'''],

           64: ['''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',

                'color',

                '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
            <CssParameter name="stroke-dashoffset">10</CssParameter>
          </Stroke>
        </LineSymbolizer>\n''',

                '''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',

                'color',

                '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
          </Stroke>
        </LineSymbolizer>\n''',

                '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
            <CssParameter name="stroke-dashoffset">10</CssParameter>
          </Stroke>
        </LineSymbolizer>\n''',

                '''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',

                'color',

                '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
          </Stroke>
        </LineSymbolizer>\n''',

                '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
            <CssParameter name="stroke-dashoffset">10</CssParameter>
          </Stroke>
          <PerpendicularOffset>5</PerpendicularOffset
        </LineSymbolizer>\n''',

                '''        <LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',

                'color',

                '''</CssParameter>
            <CssParameter name="stroke-width">2</CssParameter>
            <CssParameter name="stroke-dasharray">10 10</CssParameter>
          </Stroke>
          <PerpendicularOffset>-5</PerpendicularOffset>
        </LineSymbolizer>\n''',

           '''<PointSymbolizer>
  <Geometry>
    <ogc:Function name="startPoint">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Geometry>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#93</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',

           'color',

           '''</CssParameter>
      </Fill>
      <Stroke>
        <CssParameter name="stroke">''',

           'color',

           '''</CssParameter>
      </Stroke>
    </Mark>
    <Rotation>
      <ogc:Function name="startAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>\n''',

           '''<PointSymbolizer>
  <Geometry>
    <ogc:Function name="endPoint">
      <ogc:PropertyName>pg_geom</ogc:PropertyName>
    </ogc:Function>
  </Geometry>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#93</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',

           'color',

           '''</CssParameter>
      </Fill>
      <Stroke>
        <CssParameter name="stroke">''',

           'color',

           '''</CssParameter>
      </Stroke>
    </Mark>
    <Rotation>
      <ogc:Function name="endAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>\n'''],
           68: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#97</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#98</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],

           69: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#99</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#98</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
           72: ['''          <LineSymbolizer>
<Stroke>
  <GraphicStroke>
    <Graphic>
      <Mark>
        <WellKnownName>ttf://Line_Styles#101</WellKnownName>
        <Fill>
          <CssParameter name="fill">''',
                '#0',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">5 10</CssParameter>
            </Stroke>
          </LineSymbolizer>       
          <LineSymbolizer>
            <Stroke>
                      <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
            <CssParameter name="stroke-dasharray">10 5</CssParameter>
            <CssParameter name="stroke-dashoffset">5</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           73:  ['''          <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">''',
                 'color',
           '''</CssParameter>
              <CssParameter name="stroke-width">4</CssParameter>
              <CssParameter name="stroke-linecap">round</CssParameter>
            </Stroke>
          </LineSymbolizer>\n''',
                 '''          <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">''', 'color', '''</CssParameter>
              <CssParameter name="stroke-width">2</CssParameter>
              <CssParameter name="stroke-linecap">round</CssParameter> 
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n''',
          '''         <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">#ffffff</CssParameter>
              <CssParameter name="stroke-width">2</CssParameter>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           74: ['''          <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
                    <CssParameter name="stroke-width">4</CssParameter>
                    <CssParameter name="stroke-linecap">round</CssParameter>
                  </Stroke>
                </LineSymbolizer>\n''',
                '''          <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">2</CssParameter>
    <CssParameter name="stroke-linecap">round</CssParameter> 
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
                '''         <LineSymbolizer>
                   <Stroke>
                     <CssParameter name="stroke">#999999</CssParameter>
                     <CssParameter name="stroke-width">2</CssParameter>
                     <CssParameter name="stroke-dasharray">10 10</CssParameter>
                     <CssParameter name="stroke-dashoffset">10</CssParameter>
                   </Stroke>
                 </LineSymbolizer>\n'''],
           75: ['''          <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">2</CssParameter>
    <CssParameter name="stroke-linecap">round</CssParameter> 
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
                '''         <LineSymbolizer>
                   <Stroke>
                     <CssParameter name="stroke">#999999</CssParameter>
                     <CssParameter name="stroke-width">2</CssParameter>
                     <CssParameter name="stroke-dasharray">10 10</CssParameter>
                     <CssParameter name="stroke-dashoffset">10</CssParameter>
                   </Stroke>
                 </LineSymbolizer>\n'''],
           76: ['''          <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
                    <CssParameter name="stroke-width">4</CssParameter>
                    <CssParameter name="stroke-linecap">round</CssParameter>
                  </Stroke>
                </LineSymbolizer>\n''',
                '''          <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">2</CssParameter>
    <CssParameter name="stroke-linecap">round</CssParameter> 
    <CssParameter name="stroke-dasharray">20 20</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
                '''         <LineSymbolizer>
                   <Stroke>
                     <CssParameter name="stroke">#999999</CssParameter>
                     <CssParameter name="stroke-width">2</CssParameter>
                     <CssParameter name="stroke-dasharray">20 20</CssParameter>
                     <CssParameter name="stroke-dashoffset">20</CssParameter>
                   </Stroke>
                 </LineSymbolizer>\n'''],
           77: ['''          <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''',
                'color',
                '''</CssParameter>
                    <CssParameter name="stroke-width">4</CssParameter>
                    <CssParameter name="stroke-linecap">round</CssParameter>
                  </Stroke>
                </LineSymbolizer>\n''',
                '''          <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">2</CssParameter>
    <CssParameter name="stroke-linecap">round</CssParameter> 
    <CssParameter name="stroke-dasharray">15 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
                '''         <LineSymbolizer>
                   <Stroke>
                     <CssParameter name="stroke">#999999</CssParameter>
                     <CssParameter name="stroke-width">2</CssParameter>
                     <CssParameter name="stroke-dasharray">10 15</CssParameter>
                     <CssParameter name="stroke-dashoffset">15</CssParameter>
                   </Stroke>
                 </LineSymbolizer>\n'''],

            78: [ '''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">1</CssParameter>
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n'''
                    ,'''       
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#103</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
        79: [ '''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">1</CssParameter>
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
'''       <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#104</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
        80: [ '''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">8</CssParameter>
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
'''       <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#105</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
        81:['''          <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">#0</CssParameter>
              <CssParameter name="stroke-width">0.3</CssParameter>
            </Stroke>
          </LineSymbolizer>
          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#106</WellKnownName>
                    <Stroke>
                      <CssParameter name="stroke">#0</CssParameter>
                    </Stroke>
                  </Mark>
                  <Size>20</Size>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 60</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
           82: ['''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">#0</CssParameter>
    <CssParameter name="stroke-width">10</CssParameter>
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
    <CssParameter name="stroke-dashoffset">10</CssParameter>    
  </Stroke>
</LineSymbolizer>\n''',
                '''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">4.5</CssParameter>
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
    <CssParameter name="stroke-dashoffset">10</CssParameter>    
  </Stroke>
</LineSymbolizer>\n'''],
        83: [ '''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">8</CssParameter>
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
'''       <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#108</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                'color',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
        84: [ '''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">10</CssParameter>
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
'''       <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#109</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',
                '#000000',
                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
        85: [ '''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">12</CssParameter>
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
'''         <LineSymbolizer>
            <Stroke>
               <CssParameter name="stroke-width">4.5</CssParameter>
              <CssParameter name="stroke-dasharray">10 10</CssParameter>
              <CssParameter name="stroke-dashoffset">10</CssParameter>
            </Stroke>
          </LineSymbolizer>\n'''],
        86: [ '''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">1</CssParameter>
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
'''<PointSymbolizer>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#110</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',
           'color',
           '''</CssParameter>
      </Fill>
    </Mark>
  </Graphic>
</PointSymbolizer>\n'''],
        87: [ '''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">3.5</CssParameter>
    <CssParameter name="stroke-dasharray">10 10</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
'''<PointSymbolizer>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#114</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',
           'color',
           '''</CssParameter>
      </Fill>
    </Mark>
  </Graphic>
</PointSymbolizer>\n'''],
        88: ['''          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#107</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''',

                '#000000',

                '''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n''',

                '''          <LineSymbolizer>
            <Stroke>
              <GraphicStroke>
                <Graphic>
                  <Mark>
                    <WellKnownName>ttf://Line_Styles#94</WellKnownName>
                    <Fill>
                      <CssParameter name="fill">''','color','''</CssParameter>
                    </Fill>
                  </Mark>
                </Graphic>
              </GraphicStroke>
            </Stroke>
          </LineSymbolizer>\n'''],
        89: [ '''         <LineSymbolizer>
  <Stroke>
    <CssParameter name="stroke">''', 'color', '''</CssParameter>
    <CssParameter name="stroke-width">1</CssParameter>
    <CssParameter name="stroke-dasharray">10 2</CssParameter>
  </Stroke>
</LineSymbolizer>\n''',
'''<PointSymbolizer>
  <Graphic>
    <Mark>
      <WellKnownName>ttf://Line_Styles#114</WellKnownName>
      <Fill>
        <CssParameter name="fill">''',
           'color',
           '''</CssParameter>
      </Fill>
    </Mark>
  </Graphic>
</PointSymbolizer>\n''']}


brushDictSimple = ['''          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">''',
                   'colorMain',
                   '''</CssParameter>
            </Fill>
          </PolygonSymbolizer>\n''']


brushDict = [''' <PolygonSymbolizer>
  <Fill>
	<CssParameter name="fill">''',
             'colorBg',
             '''</CssParameter>
  </Fill>
</PolygonSymbolizer>\n''',
             ''' <PolygonSymbolizer>
  <Fill>
    <GraphicFill>
      <Graphic>
      <ExternalGraphic>\n''',
             'pattern',
             '''        \n<Format>image/svg+xml</Format>
     </ExternalGraphic>
      <Size>2</Size>
    </Graphic>
   </GraphicFill>
  </Fill>
</PolygonSymbolizer>\n''']


brushPattern = {
    '1': 1,
    '2': 1,
    '3': 11,
    '4': 16,
    '5': 19,
    '6': 24,
    '7': 31,
    '8': 34,
    '12': 2,
    '13': 3,
    '14': 4,
    '15': 5,
    '16': 6,
    '17': 7,
    '18': 8,
    '19': 9,
    '20': 10,
    '21': 11,
    '22': 12,
    '23': 13,
    '24': 14,
    '25': 15,
    '26': 16,
    '27': 17,
    '28': 18,
    '29': 19,
    '30': 20,
    '31': 21,
    '32': 22,
    '33': 23,
    '34': 24,
    '35': 25,
    '36': 26,
    '37': 27,
    '38': 28,
    '39': 29,
    '40': 30,
    '41': 31,
    '42': 32,
    '43': 33,
    '44': 34,
    '45': 35,
    '46': 36,
    '47': 37,
    '48': 38,
    '49': 39,
    '50': 40,
    '51': 41,
    '52': 42,
    '53': 43,
    '54': 44,
    '55': 45,
    '56': 46,
    '57': 47,
    '58': 48,
    '59': 49,
    '60': 50,
    '61': 51,
    '62': 52,
    '63': 53,
    '64': 54,
    '65': 55,
    '66': 56,
    '67': 57,
    '68': 58,
    '69': 59,
    '70': 60,
    '71': 61
}

symbolDictTTF = ['''          <PointSymbolizer>
            <Graphic>
              <Mark>
                <WellKnownName>ttf://''', 'fontname', '#', 'shape', '''</WellKnownName>
                <Fill>
                  <CssParameter name="fill">''', 'color', '''</CssParameter>
                </Fill>
              </Mark>
              <Size>''', 'size', '''</Size>
                            <Rotation>
                <ogc:PropertyName>g_rotation</ogc:PropertyName>
              </Rotation>
            </Graphic>
          </PointSymbolizer>\n''']

xmlDict = ['''<style>
  <id>StyleInfoImpl--''','layer','''_Style_info</id>
  <name>''','layer','''</name>
  <workspace>
    <id>WorkspaceInfoImpl-38b00827:181428e4c9d:-7ffc</id>
  </workspace>
  <format>sld</format>
  <languageVersion>
    <version>1.0.0</version>
  </languageVersion>
  <filename>''','layer','''_Style.sld</filename>
  <dateCreated>''','date','''</dateCreated>
</style>''']

emerencyStyle = ''