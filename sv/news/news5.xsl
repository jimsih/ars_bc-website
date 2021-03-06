<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:variable name="lang">sv</xsl:variable>
<xsl:variable name="number">5</xsl:variable><!--CHANGE THIS NUMBER FOR DIFFERENT NEWS-->
<xsl:template match="/">
  <html>
    <head>
    </head>
    <body>
    <xsl:for-each select="root/news">
      <xsl:sort select="date/year" data-type="number" order="descending"/>
      <xsl:sort select="date/month" data-type="number" order="ascending"/>
      <xsl:sort select="date/day" data-type="number" order="ascending"/>
      <xsl:sort select="date/hour" data-type="number" order="ascending"/>
      <xsl:sort select="date/minute" data-type="number" order="ascending"/>
    <xsl:if test="position()=$number">
    <div class="padding">
      <h2><xsl:value-of select="title[@lang=$lang]"/></h2>
      <div class="ingress"><p><xsl:value-of select="ingress[@lang=$lang]"/></p></div>
      <figure class="newsimage">
        <img width="100%">
          <xsl:attribute name="src">
            <xsl:text>../../pictures/</xsl:text><xsl:value-of select="image"/>
          </xsl:attribute>
        </img>
        <figcaption><xsl:value-of select="legend[@lang=$lang]"/></figcaption>
      </figure>
      <xsl:for-each select="p">
      <p class="text"><xsl:value-of select="."/></p>
      </xsl:for-each>
    </div>
    </xsl:if>
    </xsl:for-each>
    </body>
  </html>
</xsl:template>
</xsl:stylesheet>
