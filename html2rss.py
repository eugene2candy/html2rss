#!/usr/bin/python

import re
import urllib



sourceUrl = "unittest1.html"
startString = '<table border="1">'
fluxTitle = "Html2Rss Unit Test 1"
fluxDescription = "This is a unit test flux"

#available items
# - title
# - desc
# - url

itemRegex = "<td>(?P<title>.*?)</td>.*\n.*<td>(?P<url>.*?)</td>"




# get the source page
f = urllib.urlopen(sourceUrl)
data = f.read()
f.close()

# check items whith the regex
pattern = re.compile(itemRegex)
iterator = pattern.finditer(data, re.MULTILINE)


# write resulting rss file
print "Content-type: text/html\n"
print '<?xml version="1.0"?>'
print '<rss version="2.0">'
print '    <channel>'
print '        <title>' + fluxTitle + '</title>'
print '        <description>' + fluxDescription + '</description>'
#print '        <lastBuildDate>Sat, 07 Sep 2002 00:00:01 GMT</lastBuildDate>
print '        <link>', sourceUrl, '</link>'

for item in iterator:
    groupDict = item.groupdict()
    print '        <item>'
    if 'url' in groupDict:
        print '            <title>' + groupDict['title'] + '</title>'
    else:
        print '            <title>Unknown Title</title>'
    if 'desc' in groupDict:
        print '            <description>' + groupDict['desc'] + '</description>'
    else:
        print '            <description>No description</description>'
    if 'url' in groupDict:
        print '            <link>' + groupDict['url'] + '</link>'
    print '        </item>'
        
print '    </channel>'
print '</rss>'





