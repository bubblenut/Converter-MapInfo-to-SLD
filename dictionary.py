styleHeading = '''<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor version="1.0.0"
                       xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"
                       xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
                       xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <NamedLayer>
    <Name>All Layers</Name>
    <UserStyle>
      <Title>Styles for TestoreWGS</Title>'''


styleFooting = '''</UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>'''


filterHeading = '''
        <ogc:Filter>
          <ogc:PropertyIsEqualTo>
            <ogc:PropertyName>style</ogc:PropertyName>
            <ogc:Literal>'''

filterFooting = '''</ogc:Literal>
          </ogc:PropertyIsEqualTo>
        </ogc:Filter>'''


penDict = {1: [],
           2: ['''<LineSymbolizer>
          <Stroke>
            <CssParameter name="stroke">''',
               'color',
               '''</CssParameter>
            <CssParameter name="stroke-width">'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
        </LineSymbolizer>'''],
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
         </LineSymbolizer>'''],
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
         </LineSymbolizer>'''],
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
         </LineSymbolizer>'''],
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
         </LineSymbolizer>'''],
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
         </LineSymbolizer>'''],
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
         </LineSymbolizer>'''],
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
         </LineSymbolizer>'''],
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
         </LineSymbolizer>'''
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
         </LineSymbolizer>'''],
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
         </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>       
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
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
          </LineSymbolizer>'''],
           59: ['''          <LineSymbolizer>
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
            </Stroke>
          </LineSymbolizer>''',
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
        <CssParameter name="stroke-width">2</CssParameter>
      </Stroke>
    </Mark>
    <Size>30</Size>
    <Rotation>
      <ogc:Function name="endAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>'''],
           60: ['''          <LineSymbolizer>
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
            </Stroke>
          </LineSymbolizer>''',
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
        <CssParameter name="stroke-width">2</CssParameter>
      </Stroke>
    </Mark>
    <Size>30</Size>
    <Rotation>
      <ogc:Function name="startAngle">
        <ogc:PropertyName>pg_geom</ogc:PropertyName>
      </ogc:Function>
    </Rotation>
  </Graphic>
</PointSymbolizer>''']


           }

brushDict = {
    2: 1,
    3: 11,
    4: 16,
    5: 19,
    6: 24,
    7: 31,
    8: 34,
    12: 2,
    13: 3,
    14: 4,
    15: 5,
    16: 6,
    17: 7,
    18: 8,
    19: 9,
    20: 10,
    21: 11,
    22: 12,
    23: 13,
    24: 14,
    25: 15,
    26: 16,
    27: 17,
    28: 18,
    29: 19,
    30: 20,
    31: 21,
    32: 22,
    33: 23,
    34: 24,
    35: 25,
    36: 26,
    37: 27,
    38: 28,
    39: 29,
    40: 30,
    41: 31,
    42: 32,
    43: 33,
    44: 34,
    45: 35,
    46: 36,
    47: 37,
    48: 38,
    49: 39,
    50: 40,
    51: 41,
    52: 42,
    53: 43,
    54: 44,
    55: 45,
    56: 46,
    57: 47,
    58: 48,
    59: 49,
    60: 50,
    61: 51,
    62: 52,
    63: 53,
    64: 54,
    65: 55,
    66: 56,
    67: 57,
    68: 58,
    69: 59,
    70: 60,
    71: 61
}
