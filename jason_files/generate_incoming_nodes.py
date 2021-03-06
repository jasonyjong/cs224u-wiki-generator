#!/usr/bin/python

import glob, re, json, os, time
import xml.etree.cElementTree as etree

def add_link(title, link, link_map):
    if link in link_map:
        link_map[link].append(title)
    else:
        link_map[link] = [title]

def h():
    return os.path.abspath(os.path.dirname(__file__))

def income():
    namespace = "{http://www.mediawiki.org/xml/export-0.8/}"
    link_map = {}
    source_dir = '../jason_files/500MB_FILES'
    out_dir = '../jason_files/INCOMING_LINKS'
    if not os.path.exists(out_dir):
    	os.makedirs(out_dir)
    
    abs_dir_input = os.path.join(source_dir, '500MB_*.xml')
    for fn in glob.glob(abs_dir_input):
	    f = open(fn, 'r')
	    xml = f.read()
	    root = etree.fromstring(xml)
	    for page in root.findall('.//{0}page'.format(namespace)):
	        title = [w.text for w in page.findall('.//{0}title'.format(namespace))]
	        title = [w.replace(' ', '_') for w in title]
	        text = [w.text for w in page.findall('.//{0}text'.format(namespace))]
	        for ttl in title:
	            for txt in text:
	                for link in re.findall('\[\[(.*?)\]\]', txt):
                            #print "Hey"
	                    add_link(ttl, link, link_map)
	                  
    abs_dir_output = os.path.join(h(), out_dir, 'IL_'+str(int(time.time())) + '.xml')
	
    with open(os.path.abspath(abs_dir_output), 'wb') as local_file:
        local_file.write(json.dumps(link_map))
        

    return link_map
