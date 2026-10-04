<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="4.2.3" styleCategories="Symbology">
  <renderer-v2 type="categorizedSymbol" attr="iucn" enableorderby="1" symbollevels="1" forceraster="0">
    <categories>
      <category symbol="0" value="EN" label="Genting (EN)" render="true"/>
      <category symbol="1" value="VU" label="Rentan (VU)" render="true"/>
      <category symbol="2" value="NT" label="Hampir terancam (NT)" render="true"/>
      <category symbol="3" value="LC" label="Risiko rendah (LC)" render="true"/>
    </categories>
    <symbols>
    <symbol name="0" type="marker" alpha="1" clip_to_extent="1" force_rhr="0">
      <layer class="SimpleMarker" enabled="1" locked="0" pass="3">
        <Option type="Map">
          <Option name="color" type="QString" value="213,94,0,255"/>
          <Option name="name" type="QString" value="circle"/>
          <Option name="outline_color" type="QString" value="17,24,39,255"/>
          <Option name="outline_width" type="QString" value="0.3"/>
          <Option name="size" type="QString" value="4.2"/>
        </Option>
      </layer>
    </symbol>
    <symbol name="1" type="marker" alpha="1" clip_to_extent="1" force_rhr="0">
      <layer class="SimpleMarker" enabled="1" locked="0" pass="2">
        <Option type="Map">
          <Option name="color" type="QString" value="230,159,0,255"/>
          <Option name="name" type="QString" value="circle"/>
          <Option name="outline_color" type="QString" value="17,24,39,255"/>
          <Option name="outline_width" type="QString" value="0.3"/>
          <Option name="size" type="QString" value="3.6"/>
        </Option>
      </layer>
    </symbol>
    <symbol name="2" type="marker" alpha="1" clip_to_extent="1" force_rhr="0">
      <layer class="SimpleMarker" enabled="1" locked="0" pass="1">
        <Option type="Map">
          <Option name="color" type="QString" value="86,180,233,255"/>
          <Option name="name" type="QString" value="circle"/>
          <Option name="outline_color" type="QString" value="17,24,39,255"/>
          <Option name="outline_width" type="QString" value="0.3"/>
          <Option name="size" type="QString" value="3.0"/>
        </Option>
      </layer>
    </symbol>
    <symbol name="3" type="marker" alpha="1" clip_to_extent="1" force_rhr="0">
      <layer class="SimpleMarker" enabled="1" locked="0" pass="0">
        <Option type="Map">
          <Option name="color" type="QString" value="153,153,153,255"/>
          <Option name="name" type="QString" value="circle"/>
          <Option name="outline_color" type="QString" value="17,24,39,255"/>
          <Option name="outline_width" type="QString" value="0.3"/>
          <Option name="size" type="QString" value="1.8"/>
        </Option>
      </layer>
    </symbol>
    </symbols>
    <orderby><orderByClause asc="1" nullsFirst="1">CASE "iucn" WHEN 'EN' THEN 4 WHEN 'VU' THEN 3 WHEN 'NT' THEN 2 ELSE 1 END</orderByClause></orderby>
  </renderer-v2>
</qgis>
