import subprocess

from xml import etree

class Varnish(object):
    def __init__(self, agentConfig, checksLogger, rawConfig):
        self.agentConfig = agentConfig
        self.checksLogger = checksLogger
        self.rawConfig = rawConfig
    
    def run(self):
        stats = {}
        varnishstat = subprocess.Popen(
            ['varnishstat','-x'],
            stdout=subprocess.PIPE,
        )
        stats_xml = etree.parse(varnishstat.stdout)
        
        for stat_node in stats_xml.findall('stat'):
            label = stat_node.findtext('description')
            value = stat_node.findtext('value')
            stats[label] = value
        
        return stats